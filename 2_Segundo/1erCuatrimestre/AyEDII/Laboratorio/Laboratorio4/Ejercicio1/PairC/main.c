/*
Respuesta:

-- No esta mas la estructura definidia en el .h, por lo tanto la defino 
en el .c. 

-- main.c 
ERROR: printf("(%d, %d)\n", p->fst, p->snd); tengo que usar la especificacion dada. 
Como trate de acceder a la estructura p, esto esta mal en cuanto
a encapsulamiento porque accedo en la estructura. 
Antes tenia la estructura definida publicamente en el h, pero como la defini en 
el c, el main incluye .h y este no trae una definicion de la estructura. 
Luego el main no puede entrar en la estructura porque no tiene el struct definido. 
Puede usar las funciones porque incluyó pair.h. 

-- pair.c 
Puede entrar dentro de la estructura porque la tiene definida. 

-- pair.h 
No conoce la forma de la estructura. 

Hay encapsulamiento. La estructura no es conocida y no puedo acceder a los campos. 
Debo usar lo que esta especificado en la libreria. 
*/

#include <stdlib.h>  /* EXIT_SUCCESS... */
#include <stdio.h>   /* printf()...     */
#include "pair.h"    /* TAD Par         */

static
void show_pair(pair_t p) {
    printf("(%d, %d)\n", pair_first(p), pair_second(p));
}

int main(void) {
    pair_t p, q;
    // Nuevo par p
    p = pair_new(3, 4);
    // Se muestra el par por pantalla
    printf("p = ");
    show_pair(p);
    // Nuevo para q con elementos de p intercambiados
    q = pair_swapped(p);
    // Se muestra q
    printf("q = ");
    show_pair(q);
    // Se destruyen p y q
    p = pair_destroy(p);
    q = pair_destroy(q);
    return EXIT_SUCCESS;
}
