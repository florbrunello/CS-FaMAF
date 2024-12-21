#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string.h>


#define MAX_LENGTH 20

int main(void) {
    char user_input[MAX_LENGTH];

    printf("Ingrese su nombre y apellido: ");
    //scanf("%s", user_input);   DEJA DE LEER CUANDO ENCUENTRA UN ESPACIO 

    /*La función scanf lee el input del usuario hasta que encuentra un caracter de espacio,
    y luego de eso ignora el input restante. Por eso es que la implementación original da
    problemas a la hora de recopilar el apellido del usuario.


    char *fgets(char *s, int size, FILE *stream);

    fgets()  reads in at most one less than size characters from stream and
    stores them into the buffer pointed to by s.  Reading  stops  after  an
    EOF  or a newline.  If a newline is read, it is stored into the buffer.
    A terminating null byte ('\0') is stored after the  last  character  in
    the buffer.
    */
    fgets(user_input,MAX_LENGTH,stdin);
    /*Ingrese su nombre y apellido: flo r
    Te damos la bienvenida flo r
    a este maravilloso programa!
    */
   //LEE TODO Y AGREGA UN \N AL FINAL
    /*
       #include <string.h>

       size_t strlen(const char *s);

    DESCRIPTION
       The strlen() function calculates the length of the string pointed to by
       s, excluding the terminating null byte ('\0').
       */
    /*
        La función strcspn cuenta la cantidad de caracteres que hay hasta
        el primer '\n'.
        
        En este caso, lo que hacemos es tomar el caracter ubicado en la posición donde
        la función encontró el '\n' y reemplazarlo por el caracter '\0' que indica
        el fin de un string.
    */
   
    user_input[strcspn(user_input,"\n")] = '\0';

    printf("Te damos la bienvenida %s a este maravilloso programa!\n", user_input);

    return EXIT_SUCCESS;
}

