#include "types.h"
#include "param.h"
#include "memlayout.h"
#include "riscv.h"
#include "spinlock.h"
#include "proc.h"
#include "syscall.h"
#include "defs.h"
#include "sem.h"

int semaforos[TOTAL_SEM]={[0 ... TOTAL_SEM-1] = -1}; 
struct spinlock lock;

//Abre e inicializa un semáforo con un valor arbitrario “value”.
uint64 
sys_sem_open(void)
{  
    int value;
    argint(0,&value);
    initlock(&lock,"lock"); 

    uint64 pos=0;
    if (value >= 0){
        while (pos < TOTAL_SEM && semaforos[pos]!=CLOSED){
            pos++;
        }
        if (pos == TOTAL_SEM){ 
            printf("Error al abrir el semáforo. Se llegó al límite de semáforos abiertos\n"); 
            return 0;
        }
        else if(semaforos[pos]==CLOSED){
            acquire(&lock);
            semaforos[pos]=value;
            release(&lock);
            pos++;
            return pos; 
        }
        else
        {
            printf("Error inesperado al abrir el semáforo\n");
            return 0;
        }
    }
    else {
        printf("Error al abrir el semáforo. Argumento negativo \n"); 
        return 0;
    }
}

//Libera el semáforo “sem”.
uint64 
sys_sem_close(void)
{
    int sem;
    argint(0,&sem);
    sem--;

    if(!(0<=sem && sem<TOTAL_SEM)) return 0;
    semaforos[sem]=CLOSED; 
    return 1;
}

//Incrementa el semáforo ”sem” desbloqueando los procesos cuando su valor es 0.
uint64
sys_sem_up(void)
{
    int sem;
    argint(0,&sem);
    sem--;

    if((0<=sem && sem<TOTAL_SEM) && semaforos[sem]!=CLOSED){//Usamos como channel los punteros de semaforo, para que desbloquee los procesos que se encuentra en el mismo channel sem. 
        acquire(&lock);
        if(semaforos[sem]==0){
            semaforos[sem]+=1;
            wakeup(&semaforos[sem]);
        } 
        else{
            semaforos[sem]+=1; 
        }
        release(&lock); 
        return 1; 
    }
    else{
        printf("Error al incrementar el semáforo\n"); 
        return 0; 
    }
} 

//Decrementa el semáforo ”sem” bloqueando los procesos cuando su valor es 0.
uint64 
sys_sem_down(void)
{
    int sem;
    argint(0,&sem);
    sem--;

    if((0<=sem && sem<TOTAL_SEM) && semaforos[sem]!=CLOSED){
        acquire(&lock);
        if (semaforos[sem]>0) semaforos[sem]-=1; 
        else {
            sleep(&semaforos[sem], &lock);
        }
        release(&lock);
        return 1;
    }
    else {
        printf("Error al decrementar el semáforo\n"); 
        return 0;
    }
}
