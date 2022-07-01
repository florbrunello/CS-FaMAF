#include "array_helpers.h"
#include "mybool.h"
#include <stdio.h>
#include <stdlib.h>

unsigned int array_from_file(int array[], unsigned int max_size, const char *filepath) {
    
    /* usar fopen fscanf buscar*/

    FILE *programa; 
    programa = fopen (filepath,"r");
    fscanf (programa,"%u",&max_size);
    
    unsigned int i = 0;
    while (i<max_size)
    {
        fscanf (programa,"%d",&array[i]);
        i = i+1;       
    }
    /*  (programa,"%u",&i);*/
    
    fclose(programa);
    return max_size;
}

void array_dump(int a[], unsigned int length) {
    /* imprimir arreglo */
    unsigned int i = 0;
    printf ("[ ");
    while (i<length)
    {
        printf ("%d ",a[i]);
        i = i + 1;
    }
    printf ("]\n");
}

mybool array_is_sorted(int a[], unsigned int length)
{
    unsigned int i = 0;
    mybool res = true;
    while (i < (length-1))
    {
        if (a[i] > a[i+1])
        {
        res = false;
        break;            
        }
        else 
        {
            i = i+1;
        }
    }
    return res;
}