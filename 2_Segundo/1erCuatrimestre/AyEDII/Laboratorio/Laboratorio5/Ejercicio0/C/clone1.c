#include <stdlib.h>
#include <stdio.h>

char *string_clone(const char *str, size_t length) {
    
    //char clone[length + 1];
    //char *output=clone;

    char *clone = calloc(length+1,sizeof(char));
    char *output = clone; 

    for (size_t i=0; i<length; i++) {
        clone[i] = str[i];
    }
    clone[length] = '\0';
    return output;
}


int main(void) {
    char *original="\n"
         "A long time ago in a galaxy far, far away...\n\n\n"
         "         _______..___________.     ___      .______             \n"
         "        /       ||           |    /   \\     |   _  \\          \n"
         "       |   (----``---|  |----`   /  ^  \\    |  |_)  |          \n"
         "        \\   \\        |  |       /  /_\\  \\   |      /        \n"
         "    .----)   |       |  |      /  _____  \\  |  |\\  \\----.    \n"
         "    |_______/        |__|     /__/     \\__\\ | _| `._____|     \n"
         "                                                                \n"
         "____    __    ____      ___      .______           _______.     \n"
         "\\   \\  /  \\  /   /     /   \\     |   _  \\         /       |\n"
         " \\   \\/    \\/   /     /  ^  \\    |  |_)  |       |   (----` \n"
         "  \\            /     /  /_\\  \\   |      /         \\   \\    \n"
         "   \\    /\\    /     /  _____  \\  |  |\\  \\----..----)   |   \n"
         "    \\__/  \\__/     /__/     \\__\\ | _| `._____||_______/     \n"
         "\n\n\n"
         "                     Episode IV \n\n"
         "                     A NEW HOPE \n\n"
         "                     It is a period of civil war. Rebel\n"
         "spaceships, striking from a hidden base, have won their\n"
         "first victory against the evil Galactic Empire. During the\n"
         "battle, Rebel spies managed to steal secret plans to the\n"
         "Empires ultimate weapon, the DEATH STAR, an armored space\n"
         "station with enough power to destroy an entire planet.\n"
         "Pursued by the Empires sinister agents, Princess Leia\n"
         "races home aboard her starship, custodian of the stolen\n"
         "plans that can save her people and restore freedom to the\n"
         "galaxy...\n";
    char *copy=NULL;

    copy = string_clone(original, sizeof(original) - 1);
    printf("Original: %s\n", original);
    printf("Copia   : %s\n", copy);

    free(copy);
    copy = NULL; 

    return EXIT_SUCCESS;
}

/*
Resultado de printf("Copia   : %s\n", copy); al compilar -> 
Copia  :
A long

Esto ocurre porque sizeof(orignial) - 1 no calcula correctamente el largo del 
arreglo apuntado por orginial. 
Notar que al usar size(original) obtenemos el tamaño del puntero que apunta al 
array y no el tamaño del array. PAra saber el tamaño de original, en este caso, 
sería conveniente saber el tipo de dato y el número de elementos. 
Haciendo copy = string_clone(original, sizeof(char) * 1449);  obtenemos lo que queriamos, 
sin embargo no siempre sabemos la cantidad de elementos.
*/
