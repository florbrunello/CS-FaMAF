#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

/*
VALGRIND -> Sin memory leaks
==4598== Memcheck, a memory error detector
==4598== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==4598== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==4598== Command: ./K
==4598== 
11==4598== 
==4598== HEAP SUMMARY:
==4598==     in use at exit: 0 bytes in 0 blocks
==4598==   total heap usage: 7 allocs, 7 frees, 1,116 bytes allocated
==4598== 
==4598== All heap blocks were freed -- no leaks are possible
==4598== 
==4598== For counts of detected and suppressed errors, rerun with: -v
==4598== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
*/

int main (){
    // ANDA 
    stack s=NULL;
    s = stack_push(s,3);
    s = stack_pop(s);
    s = stack_push(s,4); 
    s = stack_destroy(s);

    // ANDA
    bool res; 
    stack p;
    stack_elem *q; 
    p = stack_empty();
    q = stack_to_array(p);
    res = q == NULL;
    printf("%u",res);
    p = stack_destroy (p);
    free(q); 
    q=NULL;
    
    //
    stack f = NULL; 
    stack_elem *g;
    f = stack_push(f,1);
    f = stack_push(f,2);
    f = stack_push(f,3);
    g = stack_to_array(f);
    printf("%d",g[0]);
    f = stack_destroy(f);
    free(g);
    g = NULL;
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
