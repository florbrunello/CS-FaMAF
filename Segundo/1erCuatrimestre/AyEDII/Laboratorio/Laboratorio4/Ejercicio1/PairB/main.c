/*
Respuesta:
Hay buen acoplamiento porque con respecto al ejercicio a, nada cambio. 
Cambie la manera de implementar el par pero el main no se modifico. 
Tiene bajo acomplamiento: modifique la implementacion por dentro y no cambie 
el resto del programa. La implementacion no logra encapsulamiento 
porque en el .h sigo teniendo la estructura. 
*/

#include <stdlib.h>  /* EXIT_SUCCESS... */
#include <stdio.h>   /* printf()...     */
#include "pair.h"    /* TAD Par         */

static
void show_pair(pair_t p) {
    printf("(%d, %d)\n", p->fst, p->snd);
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
