#include <stdio.h>
#include <stdlib.h>
#include "hanoi.h"

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: ./solve-hanoi <disk-count>\n");
        exit(EXIT_FAILURE);
    }
    int count = atoi(argv[1]);
    if (count < 0) {
        printf("Negative disk-count is not allowed\n");
        exit(EXIT_FAILURE);
    }
    if (count > 20) {
        printf("> 20 is too slow!\n");
        exit(EXIT_FAILURE);
    }
    hanoi_t hanoi = hanoi_init(count);
    hanoi_print(hanoi);
    hanoi_solve(hanoi);
    hanoi = hanoi_destroy(hanoi);
    return 0;
}

/*
==22129== Invalid read of size 4
==22129==    at 0x108C0B: stack_is_empty (stack.c:80)
==22129==    by 0x108C3B: stack_to_array (stack.c:86)
==22129==    by 0x109348: print (hanoi.c:147)
==22129==    by 0x108E27: hanoi_print (hanoi.c:45)
==22129==    by 0x109488: main (main.c:20)
==22129==  Address 0x8 is not stack'd, malloc'd or (recently) free'd
==22129== 
==22129== 
==22129== Process terminating with default action of signal 11 (SIGSEGV)
==22129==  Access not within mapped region at address 0x8
==22129==    at 0x108C0B: stack_is_empty (stack.c:80)
==22129==    by 0x108C3B: stack_to_array (stack.c:86)
==22129==    by 0x109348: print (hanoi.c:147)
==22129==    by 0x108E27: hanoi_print (hanoi.c:45)
==22129==    by 0x109488: main (main.c:20)
==22129==  If you believe this happened as a result of a stack
==22129==  overflow in your program's main thread (unlikely but
==22129==  possible), you can try to increase the size of the
==22129==  main thread stack using the --main-stacksize= flag.
==22129==  The main thread stack size used in this run was 8388608.
==22129== 
==22129== HEAP SUMMARY:
==22129==     in use at exit: 168 bytes in 5 blocks
==22129==   total heap usage: 9 allocs, 4 frees, 232 bytes allocated
==22129== 
==22129== LEAK SUMMARY:
==22129==    definitely lost: 0 bytes in 0 blocks
==22129==    indirectly lost: 0 bytes in 0 blocks
==22129==      possibly lost: 0 bytes in 0 blocks
==22129==    still reachable: 168 bytes in 5 blocks
==22129==         suppressed: 0 bytes in 0 blocks
==22129== Reachable blocks (those to which a pointer was found) are not shown.
==22129== To see them, rerun with: --leak-check=full --show-leak-kinds=all
==22129== 
==22129== For counts of detected and suppressed errors, rerun with: -v
==22129== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Violación de segmento (`core' generado)
*/
