#include "mybool.h"
#ifndef ARRAY_HELPERS_H
#define ARRAY_HELPERS_H

unsigned int array_from_file(int array[], unsigned int max_size, const char *filepath);
void array_dump(int a[], unsigned int length);
mybool array_is_sorted(int a[], unsigned int length);

#endif

/* 
Puede ser que pese a no haber agregado nada al mybool.h
(lo del ifndef y endif), me haya compilado y corrido correctamente 
de igual modo aunque usé todas las flags (como dice el ej3)? 
Consulto porque uno de los puntos es responder porqué no compila pero sí lo hace
fijate que te falta incluir a mybool.h en array_helpers.h.
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("spoiler!!\n");
   return EXIT_SUCCESS;
}
en el .h van los prototipos de las funciones de la librería, pero 
si en los prototipos hay tipos que no son nativos del lenguajte 
(caso de mybool) tenes que incluir ahí tambien la librería que tiene 
su definición (que en este caso sería hacer #include "mybool.h").
*/