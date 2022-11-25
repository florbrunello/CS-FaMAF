#include <glib-2.0/glib.h>
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>  /* Para chdir */

#include "tests/syscall_mock.h"
#include "builtin.h"
#include "command.h"
#include "strextra.h"

static bool builtin_is_exit(scommand cmd){
    assert(cmd!=NULL);
    
    return (strcmp(scommand_front(cmd), "exit") == 0);
}

static bool builtin_is_cd(scommand cmd){
    assert(cmd!=NULL);

    return (strcmp(scommand_front(cmd), "cd") == 0);
}

static bool builtin_is_help(scommand cmd){
    assert(cmd!=NULL); 
    
    return(strcmp(scommand_front(cmd), "help")== 0);
}

bool builtin_is_internal(scommand cmd){
    assert(cmd!=NULL);
    
    return (builtin_is_exit(cmd) || builtin_is_cd(cmd) || builtin_is_help(cmd));
}

bool builtin_alone(pipeline p){
    assert(p!=NULL);
    
    unsigned int length = pipeline_length(p);
    bool is_internal = builtin_is_internal(pipeline_front(p));

    return (length == 1u && is_internal);
}

static void builtin_execute_cd(scommand cmd){
    assert(cmd!=NULL && builtin_is_cd(cmd));

    unsigned int length = scommand_length(cmd);

    if(length <= 2u){
        char* path = NULL; 
        unsigned int path_args = 0u; 
        int chdir_return = 0;   
        char *my_home = getenv("HOME");

        if(length > 1u){
            scommand_pop_front(cmd);
            path = scommand_front(cmd);
            path_args = strlen(path);            
        }

        if (path_args >= 2u){
            if(my_home!=NULL && path[0] == '~' && path[1] == '/'){ //Casos cd ~/Directorio
                chdir_return = chdir(strmerge(my_home,&path[1]));
            } else{
                chdir_return = chdir(path);
            }
        } else{
            if(path == NULL || strcmp(path,"") == 0 || path[0] == '~'){ //Casos cd, cd (con espacio) y cd ~
                if (my_home == NULL){
                        chdir_return = chdir("~");
                } else{
                        chdir_return = chdir(my_home);
                }
            } else {
                chdir_return = chdir(path);
            }
        }
        if(chdir_return!=0){
            printf("cd: No existe el directorio\n");
        }
    } else {
        printf("cd: Demasiados argumentos\n");
    }
}

static void print_help(void) {
    printf("Shell: mybash, versión 1.0.\nAutores: Florencia Brunello, "
     "Franco Bustos, Maria Emilia Caldara, Andrés Ferrero.\nLos comandos " 
     "internos son:\n\tcd [dir]:\n\t\tModifica el directorio de trabajo "
     "del shell.\n\t\tModifica el directorio actual a DIR. \n\t\tDIR por "
     "defecto es el valor de la variable de shell HOME.\n\thelp:\n\t\t"
     "Muetra información sobre la shell y sus autores,\n\t\tademás de una "
     "breve descripción de todos sus comandos internos.\n\texit:\n\t\t"
     "Sale del intérprete de ordenes.\n");
}

void builtin_run(scommand cmd) { 
    assert(builtin_is_internal(cmd));
    
    if (builtin_is_exit(cmd)) {
        exit(EXIT_SUCCESS);
    }
    else if (builtin_is_cd(cmd)) {
        builtin_execute_cd(cmd);
    } 
    else {
        print_help();
    }
}
