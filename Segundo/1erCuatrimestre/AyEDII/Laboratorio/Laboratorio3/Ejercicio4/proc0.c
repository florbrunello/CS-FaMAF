#include <stdlib.h>
#include <stdio.h>

void absolute(int x, int y) {
    // Completar aqui

    if (x >= 0){
        y = x;
    }
    else{
        y = (-x);
    }
    printf("%d\n",y);
}

int main(void) {

    int a = -98; 
    int res = 0; 
    absolute(a,res);

    return EXIT_SUCCESS;
}

/*
Compilacion
gcc -Wall -Werror -pedantic -std=c99 proc1.c -o abs1
./abs1
*/
