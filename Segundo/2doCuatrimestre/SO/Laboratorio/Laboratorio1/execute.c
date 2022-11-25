#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <unistd.h>       /* Para execvp */
#include <sys/syscall.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <string.h>

#include "tests/syscall_mock.h"
#include "execute.h"
#include "command.h"
#include "builtin.h"
#include "parsing.h"

static void swap_fd_in(char *redir_in){
    int fd_in = open(redir_in,O_RDONLY, S_IRUSR | S_IWUSR);
    if(fd_in < 0){
        printf("mybash: %s: No existe el archivo o el directorio\n",redir_in);
        exit(EXIT_FAILURE);
    }else{
        dup2(fd_in,0);
        close(fd_in);
    }
}

static void swap_fd_out(char *redir_out){
    int fd_out = open(redir_out,O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    if(fd_out < 0){
        printf("Hubo error al abrir el archivo de escritura\n");
        exit(EXIT_FAILURE);
    }else{
        dup2(fd_out,1);
        close(fd_out);
    }
}


static char **scommand_argv(scommand cmd){
    unsigned int const length = scommand_length(cmd);
    char **argv = calloc(sizeof(char*),length+1u);
    char * aux = NULL;

    for (unsigned int i=0u; i<length;i++){
        aux = strdup(scommand_front(cmd));
        scommand_pop_front(cmd);
        argv[i] = aux;
    }
    argv[length] = NULL;
    return argv;
}

static unsigned int execute_single_command(pipeline apipe){
    assert(apipe!=NULL && pipeline_length(apipe)==1u);
    
    scommand cmd = NULL;
    char * redir_in = NULL;
    char * redir_out= NULL;
    bool pipe_wait = pipeline_get_wait(apipe);
    cmd = pipeline_front(apipe);
    if (strcmp(scommand_to_string(cmd),"^D") == 0) {
        printf("Saliendo...\n");
        exit(EXIT_SUCCESS);
    }

    if (builtin_is_internal(cmd)) {
        builtin_run(cmd);
    } else { 
        redir_in = scommand_get_redir_in(cmd);
        redir_out = scommand_get_redir_out(cmd);
        int pid = fork();
        if (pid < 0){
            printf("Error al crear al hijo\n");
            return EXIT_FAILURE;
        } 
        else if (pid == 0){ //PROCESO HIJO 
            /* Chequeo de entradas/salidas */
            if (redir_in != NULL) swap_fd_in(redir_in);
            if (redir_out != NULL) swap_fd_out(redir_out);
            char ** argv = scommand_argv(cmd);
            if (execvp(argv[0],argv)==-1) {
                printf("Orden no encontrada\n");
                exit(EXIT_FAILURE);
            }
            execvp(argv[0], argv);
        }
    }
    //PROCESO PADRE
    if(pipe_wait) wait(NULL);

    return EXIT_SUCCESS;
}

static unsigned int execute_multiple_commands(pipeline apipe){
    assert(apipe != NULL && pipeline_length(apipe) > 1);
    //Contador
    unsigned int count = 0;

    //Argumentos de los comandos
    char **argv = NULL;

    //Espera
    bool pipe_wait = pipeline_get_wait(apipe);

    //Cantidad de comandos
    unsigned int length = pipeline_length(apipe);
    unsigned int const total = length;

    //Comando a procesar, sus redirecciones y su pid
    scommand cmd;
    char * redir_in = NULL;
    char * redir_out = NULL;
    int pid;

    //Buffers
    //Matriz
    int **p = NULL;
    //Filas de la matriz
    p = calloc(total-1,sizeof(int *));
    //Columnas
    for (unsigned int i = 0; i < total-1; i++) p[i] = calloc(2,sizeof(int));
    
    //Ejecuto el primer comando
    cmd = pipeline_front(apipe);
    redir_in = scommand_get_redir_in(cmd);
    redir_out = scommand_get_redir_out(cmd);
    pipe(p[0]);
    pid = fork();

    //Fallo en el fork
    if (pid<0){
        printf("Error al crear al primer hijo\n");
        return EXIT_FAILURE;
    }
    //Proceso Hijo
    else if (pid == 0)
    {
        //Lo que se escriba en la salida estandar que se escriba en la salida del pipe
        dup2(p[0][1],1);
        //Cierro el fd duplicado
        close(p[0][1]);

        //Cierro la entrada del pipe
        close(p[0][0]);

        //Modifico la salida o la entrada del comando si es necesario
        if (redir_in != NULL) swap_fd_in(redir_in);
        if (redir_out != NULL) swap_fd_out(redir_out);

        //Agarro los argumentos del comando y lo ejecuto
        argv = scommand_argv(cmd);
        execvp(argv[0],argv);
        printf("Orden no encontrada\n");
        exit(EXIT_FAILURE);
    }
    //Proceso Padre
    //Cierro la salida del pipe anterior
    close(p[0][1]);

    //Quito un elemento a apipe y uso el siguiente comando
    pipeline_pop_front(apipe);
    length--;
    cmd = pipeline_front(apipe);
    redir_in = scommand_get_redir_in(cmd);
    redir_out = scommand_get_redir_out(cmd);

    //Repito hasta consumir todos los pipes
    while (length > 1 && count != total-2)
    {
        count++;
        pipe(p[count]);
        pid = fork();
        //Fallo en el fork
        if (pid<0){
            printf("Error al crear al hijo %d\n",count+1);
            return EXIT_FAILURE;
        }
        //Proceso hijo número Count + 1
        else if (pid == 0)
        {
            //Lo que se lea en la entrada estandar que sea la entrada del pipe anterior
            dup2(p[count-1][0],0);
            //Cierro el fd duplicado
            close(p[count-1][0]);

            //Lo que se escriba en la salida estandar que se escriba en la salida del pipe
            dup2(p[count][1],1);
            //Cierro el fd duplicado
            close(p[count][1]);

            //Cierro la entrada del pipe
            close(p[count][0]);

            //Modifico la salida o la entrada del comando si es necesario
            if (redir_in != NULL) swap_fd_in(redir_in);
            if (redir_out != NULL) swap_fd_out(redir_out);

            //Agarro los argumentos del comando y lo ejecuto
            argv = scommand_argv(cmd);
            execvp(argv[0],argv);
            printf("Orden no encontrada\n");
            exit(EXIT_FAILURE);
        }
        //Vuelo al Padre
        //Cierro los fd que quedaron abierto y no se usarán
        close(p[count-1][0]);
        close(p[count][1]);

        //Quito un elemento a apipe y uso el siguiente comando
        pipeline_pop_front(apipe);
        length--;
        cmd = pipeline_front(apipe);
        redir_in = scommand_get_redir_in(cmd);
        redir_out = scommand_get_redir_out(cmd);
    }

    //Ultimo comando
    pid = fork();

    //Fallo en el fork
    if (pid < 0){
        printf("Error al crear hijo %d\n",count+2);
        return EXIT_FAILURE;
    }
    //Proceso Hijo
    else if (pid == 0)
    {
        //Lo que se lea en la entrada estandar que sea la entrada del pipe
        dup2(p[count][0],0);
        //Cierro el fd duplicado
        close(p[count][0]);

        //Modifico la salida o la entrada del comando si es necesario
        if (redir_in != NULL) swap_fd_in(redir_in);
        if (redir_out != NULL) swap_fd_out(redir_out);

        //Agarro los argumentos del comando y lo ejecuto
        argv = scommand_argv(cmd);
        execvp(argv[0],argv);
        printf("Orden no encontrada\n");
        exit(EXIT_FAILURE);
    }
    //Vuelo al Padre
    //Cierro el último fd abierto
    close(p[count][0]);

    //Caso background
    if (pipe_wait) for (unsigned int i = 0; i < total; i++) wait(NULL);

    //Libero p
    for (unsigned int i = 0; i < total-1; i++) free(p[i]);
    free(p);

    return EXIT_SUCCESS;
}

void execute_pipeline(pipeline apipe){
    assert(apipe!=NULL);
    unsigned int length = pipeline_length(apipe);
    unsigned int error;
    if (length==1u) {
        error = execute_single_command(apipe);
    } 
    else if (length > 1u) error = execute_multiple_commands(apipe);
    else{
        printf("Error, no se puede enviar pipe vacio\n");
        error = EXIT_FAILURE;
    }
    if (error != EXIT_SUCCESS) printf("Error al ejecutar el comando, intente nuevamente\n");
    
}

//De esta forma no tenemos procesos zombies, pero usamos un wait en & y por lo tanto no devuelve 100%
//make test
// void execute_pipeline(pipeline apipe){
//     assert(apipe!=NULL);
//     unsigned int length = pipeline_length(apipe);
//     unsigned int error;
//     bool zombie = !pipeline_get_wait(apipe);
//     int pid = 1;
//     if (zombie) pid = fork();
//     if (!zombie || pid == 0){
//         if (length==1u) {
//             error = execute_single_command(apipe);
//         } 
//         else if (length > 1u) error = execute_multiple_commands(apipe);
//         else{
//             printf("Error, no se puede enviar pipe vacio\n");
//             error = EXIT_FAILURE;
//         }
//         if (error != EXIT_SUCCESS) printf("Error al ejecutar el comando, intente nuevamente\n");
//         if (zombie) exit(error);
//     }
//     else if(pid > 0){
//         wait(NULL);
//     }
// }