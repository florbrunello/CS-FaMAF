#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

/*
VALGRIND -> sin memory leaks
==5214== Memcheck, a memory error detector
==5214== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==5214== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==5214== Command: ./K
==5214== 
==5214== 
==5214== HEAP SUMMARY:
==5214==     in use at exit: 0 bytes in 0 blocks
==5214==   total heap usage: 3 allocs, 3 frees, 48 bytes allocated
==5214== 
==5214== All heap blocks were freed -- no leaks are possible
==5214== 
==5214== For counts of detected and suppressed errors, rerun with: -v
==5214== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
*/

int main (){
    
    stack s = stack_empty();
    s = stack_push(s,3);
    s = stack_pop(s);
    s = stack_push(s,4); 
    s = stack_destroy(s);

    return 0; 
}

/*
Al usar gdb, p (s->next)->elem para acceder al segundo elemento.

    stack s=NULL;
    s = stack_push(s,3);


    bool res; 
    unsigned int length=0u;
    length = stack_size(s); //debe tener tamaño 1
    res = length == 1;

Error
     //unsigned int length=0u;
   
    //length = stack_size(s); //debe tener tamaño 1
    stack_elem e;
    e = stack_top(s);
    bool res; 
    res = length == 1;

    printf("%u",res);
    stack_pop(s);
    //printf("%p\n",s);

*/
