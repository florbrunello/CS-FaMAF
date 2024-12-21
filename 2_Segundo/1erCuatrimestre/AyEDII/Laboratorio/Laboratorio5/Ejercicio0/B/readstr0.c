#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 20

int main(void) {
    char user_input[MAX_LENGTH];
    char aux[MAX_LENGTH];

    printf("Ingrese su nombre y apellido: ");
    //scanf("%s", user_input);

    fgets(aux, MAX_LENGTH, stdin);
    strncpy(user_input, aux, strlen(aux)-1);

    printf("Te damos la bienvenida %s a este maravilloso programa!\n", user_input);

    return EXIT_SUCCESS;
}

/*
scanf no lee una cadena que contiene espacios, sino que se detiene una vez halló un espacio. 
Para escanear una cadena con espacios en C usamos fgets. 
Observacion: 
    la máxima longitud de cadena, al leer, debería contemplar el carácter de terminación
    de cadena (el \0) y también el salto de línea. En otras palabras, si la máxima 
    longitud es 4, colocamos en 6 para tomar estos dos caracteres.
*/
