#include <stdio.h>    /* printf(), scanf() */
#include <stdbool.h>  /* tipo bool         */

#include <assert.h>   /* assert() */

#define ARRAY_SIZE 10

struct max_min_result {
    int max_value;
    int min_value;
    unsigned int max_position;
    unsigned int min_position;
};

struct max_min_result compute_max_min(int array[], unsigned int length)
{
    assert(length > 0);
    array = array;
    struct max_min_result result = { 0, 0, 0, 0 };
    result.max_value = array[0];
    result.max_position = 0; 
    result.min_value = array[0];
    result.min_position = 0;
    for (unsigned int i=0; i<length; i++)
    {
        if (result.max_value < array[i])
        {
            result.max_value = array[i];
            result.max_position = i;
        }
        if (result.min_value > array[i])
        {
            result.min_value = array[i];
            result.min_position = i;
        }
    }
    // IMPLEMENTAR

    return result;
}

int main(void)
{
    int i = 0;
    int array[ARRAY_SIZE];
    while (i<ARRAY_SIZE)
    {
        printf ("Ingrese el valor para el elemento %d del arreglo\n", i);
        scanf ("%d",&array[i]);
        i = i + 1;
    }
    // PEDIR AL USUARIO QUE INGRESE LOS ELEMENTOS DEL ARREGLO.

    struct max_min_result result = compute_max_min(array, ARRAY_SIZE);
    printf("Máximo: %d\n", result.max_value);
    printf("Posición del máximo: %u\n", result.max_position);
    printf("Mínimo: %d\n", result.min_value);
    printf("Posición del mínimo: %u\n", result.min_position);
    return 0;
}
