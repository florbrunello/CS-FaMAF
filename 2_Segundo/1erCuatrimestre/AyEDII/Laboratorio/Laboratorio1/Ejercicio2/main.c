/* First, the standard lib includes, alphabetically ordered */
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/* Maximum allowed length of the array */
#define MAX_SIZE 100000


unsigned int array_from_stdin(int array[], unsigned int max_size) {
    printf ("Ingrese el tamano del arreglo\n");
    unsigned int size = 0u;
    fscanf(stdin,"%u\n", &size);
    //Chequear que no sea mayor al max_size

    for(unsigned int i = 0u;i<size && i<max_size;i++){
        printf ("Ingrese el elemento %u del arreglo\n",i);
        fscanf(stdin,"%d",&array[i]);    
    }

    return size;
}

void array_dump(int a[], unsigned int length) {
    printf("[");
    unsigned int i=0;
    for(i=0;i<length;i++){
        printf("%d ",a[i]);
    }
    printf("]\n");
}
/*
unsigned int array_from_stdin(int array[], unsigned int max_size) 
{
    printf ("Ingrese el tamano del arreglo");
    fscanf (stdin,"%u",&max_size);
    
    unsigned int i = 0; 
    while (i<max_size)
    {
        printf ("Ingrese el elemento %u del arreglo",i);
        fscanf (stdin,"%d", &array[i]);
        i = i+1;
    }
    return max_size;
}

void array_dump(int a[], unsigned int length) 
{
    imprimir arreglo 
    unsigned int i = 0;
    printf ("[ ");
    while (i<length)
    {
        printf ("%d ",a[i]);
        i = i + 1;
    }
    printf ("]");
}
*/
int main(void) {

    /* create an array of MAX_SIZE elements */
    int array[MAX_SIZE];
    
    /* parse the file to fill the array and obtain the actual length */
    unsigned int length = array_from_stdin(array, MAX_SIZE);
    
    /*dumping the array*/
    array_dump(array, length);
    
    return EXIT_SUCCESS;
}

// gcc -Wall -Werror -Wextra -pedantic -std=c99 -o reader main.c
// ./reader input/example-easy.in
