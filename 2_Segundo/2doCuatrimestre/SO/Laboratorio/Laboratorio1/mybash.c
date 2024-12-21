#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include "command.h"
#include "execute.h"
#include "parser.h"
#include "parsing.h"
#include "builtin.h"
#include "prompt.h"

int main(int argc, char *argv[]) {
    pipeline pipe;
    Parser input;
    bool garbage;  
    bool quit = false; 
    input = parser_new(stdin);
    while (!quit) {
        show_prompt();

        pipe = parse_pipeline(input);
        
        /* Si llegamos al final de un archivo hay que salir luego de ejecutar el comando */
        quit = parser_at_eof(input);
     
        if(pipe!=NULL){
            execute_pipeline(pipe);
            pipe = pipeline_destroy(pipe);
        }
        else {
            parser_garbage(input,&garbage);
        }
    }
    parser_destroy(input); input = NULL;
    return EXIT_SUCCESS;
}
