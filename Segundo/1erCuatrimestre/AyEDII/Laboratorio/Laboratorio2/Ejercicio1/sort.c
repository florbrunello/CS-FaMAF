#include <assert.h>
#include <stdbool.h>
#include <stdio.h>

#include "array_helpers.h"
#include "sort_helpers.h"
#include "sort.h"

static void insert(int a[], unsigned int i) {
    /* needs implementation */
    unsigned int j;
    j = i;
    while (j > 0 && goes_before(a[j],a[j-1u])){
        swap(a, j-1u, j);
        j = j-1u;
    }
}

void insertion_sort(int a[], unsigned int length) {
    for (unsigned int i = 1u; i < length; ++i) {
        /* needs implementation */
        insert(a, i);
        assert(array_is_sorted(a,i));
    }
}

/*
Implementar insert del algoritmo insertion sort. 
Invariante: desde 0 a i está ordenado
Reprensentacion de la constante del unsigned int.
j > 0u y no j >= 0 porque sino hago j-1: me voy de rango 

--
Precondicion del invariante: array ordenado hasta i. Array_is_sorted
Asssert: sirve para desarrollo, no para produccion. Al cliente no le puede 
saltar el assert. 
Me da informacion a mi. 
Si no se cumple, el programa esta mal. 
*/