#include "kernel/types.h"
#include "kernel/stat.h"
#include "user/user.h"
#include "kernel/sem.h"
#include "kernel/syscall.h"

int main(int argc, char *argv[])
{
    int sem_ping;
    int sem_pong;
    int rally = atoi(argv[1]);
    int pid = 0;
    int error = 0;

    sem_ping = sem_open(1);
    if (sem_ping == 0)
    {
        printf("Error al abrir semaforo ping \n");
        exit(-1);
    }
    sem_pong = sem_open(0);
    if (sem_pong == 0)
    {
        printf("Error al abrir semaforo pong \n");
        exit(-1);
    }

    pid = fork();

    if (pid < 0) {
        printf("Error al hacer fork\n");
        exit(-1);
    }
    //HIJO
    else if (pid == 0)
    {
        while(rally > 0)
        {
            rally--;
            error = sem_down(sem_pong);
            if (error == 0){
                printf("HIJO: Error al decrementar el semaforo del hijo\n");
                sem_close(sem_ping);
                sem_close(sem_pong);
                exit(-1);
            }
            printf("\tpong\n");

            error = sem_up(sem_ping);
            if (error == 0){
                printf("HIJO: Error al incrementar el semaforo del padre\n");
                sem_close(sem_ping);
                sem_close(sem_pong);
                exit(-1);
            }
            error = sem_down(sem_ping);
            if (error == 0){
                printf("HIJO: Error al decrementar el semaforo del padre\n");
                sem_close(sem_ping);
                sem_close(sem_pong);
                exit(-1);
            }
        }
        exit(0);
    }
    else
    //PADRE
    {
        while(rally > 0)
        {
            rally--;
            error = sem_down(sem_ping);
            if (error == 0){
                printf("PADRE: Error al decrementar el semaforo del padre\n");
                sem_close(sem_ping);
                sem_close(sem_pong);
                exit(-1);
            }
            printf("ping\n");
            error = sem_up(sem_pong);
            if (error == 0){
                printf("PADRE: Error al incrementar el semaforo del hijo\n");
                sem_close(sem_ping);
                sem_close(sem_pong);
                exit(-1);
            }
            error = sem_down(sem_pong);
            if (error == 0){
                printf("PADRE: Error al decrementar el semaforo del hijo\n");
                sem_close(sem_ping);
                sem_close(sem_pong);
                exit(-1);
            }
        }
        wait(0);
        int alert = 1; 
        error = sem_close(sem_ping);
        if (error == 0){
            printf("PADRE: Error al cerrar el semaforo padre\n");
            alert = 0;
        }
        error = sem_close(sem_pong);
        if (error == 0){
            printf("PADRE: Error al cerrar el semaforo padre\n");
            alert = 0;
        }
        if (alert == 0) exit(-1);
        exit(0);
    }
}
