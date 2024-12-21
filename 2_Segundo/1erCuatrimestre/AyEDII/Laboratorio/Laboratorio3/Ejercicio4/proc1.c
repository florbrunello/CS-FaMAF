#include <stdlib.h>
#include <stdio.h>

void absolute(int x, int *y) {
    // Completar aqui

    if (x >= 0){
        y = &x;
    }
    else{
        y = &x;
        *y = -(*y);  
    }
    printf("%d\n",*y);
}

int main(void) {
    // Completar aqui
    int a = -98; 
    int res = 0;
    int *p = &res; 
    absolute(a,p);    
    
    return EXIT_SUCCESS;
}

/*
Compilacion
gcc -Wall -Werror -Wextra -pedantic -std=c99 proc2.c -o abs2
./abs2
98
*/
