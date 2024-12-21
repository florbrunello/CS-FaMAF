#include <stdio.h>
#include "stack.h"

/*
VALGRIND 
==5258== Memcheck, a memory error detector
==5258== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==5258== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==5258== Command: ./K
==5258== 
==5258== 
==5258== HEAP SUMMARY:
==5258==     in use at exit: 0 bytes in 0 blocks
==5258==   total heap usage: 3 allocs, 3 frees, 32 bytes allocated
==5258== 
==5258== All heap blocks were freed -- no leaks are possible
==5258== 
==5258== For counts of detected and suppressed errors, rerun with: -v
==5258== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
*/

int main (){
    stack s = stack_empty();
    s = stack_push(s, 3);
    s = stack_push(s,4); 
    stack_destroy(s);
    return 0; 
}