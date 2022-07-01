#include <assert.h>
#include <stdbool.h>
#include <stdio.h>

#include "array_helpers.h"
#include "sort_helpers.h"
#include "sort.h"


static void quick_sort_rec(int a[], unsigned int izq, unsigned int der) {
    unsigned int ppiv = 0u;
    if (der > izq){
        ppiv = partition(a,izq,der); 
        quick_sort_rec(a,izq,ppiv-1u);
        quick_sort_rec(a,ppiv+1u,der);
    }
}
    /*precondicion: leugo de llamar a partition, piv queda en la 
    posicion en que va en el arreglo
    if piv>0 , al restarle 1 al unsi
    Arreglo ordenado al reves: 
    ppiv + 1: no existe la posicion

    Indentancion
    Unsigned int
    Inicializar 
    
    needs implementation

    no implementes partition, ya está implementado en sort_helpers.o
    (no se puede leer, pero en sort_helpers.h vas a encontrar información
    para saber cómo usarlo)

    unsigned int ppiv=0u;
    if (der > izq) {
        ppiv = partition(a, izq, der);
        quick_sort_rec(a, izq, (ppiv == 0) ? 0 : ppiv-1);
        quick_sort_rec(a, (ppiv == der) ? der : ppiv+1, der);
    }
    */

void quick_sort(int a[], unsigned int length) {
    quick_sort_rec(a, 0u, (length == 0u) ? 0u : length - 1u);
}
