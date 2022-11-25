#ifndef SEM_H
#define SEM_H

//Defino cantidad total de semáforos disponibles 
#define TOTAL_SEM 100
#define CLOSED -1

uint64 sys_sem_open(void);
uint64 sys_sem_close(void);
uint64 sys_sem_up(void);
uint64 sys_sem_down(void);

#endif