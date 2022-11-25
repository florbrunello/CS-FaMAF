#include <stdlib.h>
#include <stdbool.h>

#include "parsing.h"
#include "parser.h"
#include "command.h"

static scommand parse_scommand(Parser p) {
    scommand readen_cmd = scommand_new();
    arg_kind_t type; 
       
    char* read = NULL; 
    read = parser_next_argument(p,&type);
    
    if(read==NULL){
        return NULL; 
    }
    while(read!=NULL ){
        if(type==ARG_NORMAL){
            scommand_push_back(readen_cmd,read);
        }
        else if(type==ARG_INPUT){
            scommand_set_redir_in(readen_cmd,read);
        }
        else if(type==ARG_OUTPUT && read!=NULL){
            scommand_set_redir_out(readen_cmd,read);
        }
        read = parser_next_argument(p,&type);
        
        if((type == ARG_OUTPUT || type == ARG_INPUT) && read==NULL){
            printf("mybash: error sintáctico cerca del elemento inesperado 'newline'\n");
            readen_cmd = scommand_destroy(readen_cmd);
            return NULL;
        }
    }
    return readen_cmd;
}

pipeline parse_pipeline(Parser p) {
    pipeline result = pipeline_new();
    scommand cmd = NULL;
    bool error = false, another_pipe=true;

    bool background = true; 
    bool garbage = true;
    bool end_file = true; 
    char* trash = NULL; 

    cmd = parse_scommand(p);
    error = (cmd==NULL); // Comando inválido al empezar
    if (error){
        parser_garbage(p,&garbage); //Consumir todo lo que hay
        return NULL; 
    }
    while (another_pipe && !error){
        pipeline_push_back(result,cmd);
        parser_op_pipe(p,&another_pipe); 

        if(!another_pipe){ //Caso de OP_BACKGROUND al final 
            parser_op_background(p,&background);
            pipeline_set_wait(result,!background);
        }
        cmd = parse_scommand(p);
        if (cmd == NULL && another_pipe){
            printf("mybash: error sintáctico\n");
            result = pipeline_destroy(result);
            return NULL;
        }
        end_file = parser_at_eof(p);
        error = (cmd==NULL || end_file);    
    }
    parser_garbage(p,&garbage); //Consumir todo lo que hay
    trash = parser_last_garbage(p);
    if(garbage){
        printf("mybash: error sintáctico cerca del elemento inesperado '%s'\n", trash);
        result = pipeline_destroy(result);
        return NULL;
    }

    return result;
}