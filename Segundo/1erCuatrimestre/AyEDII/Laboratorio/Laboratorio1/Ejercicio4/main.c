/* First, the standard lib includes, alphabetically ordered */
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "array_helpers.h"

/* Maximum allowed length of the array */
#define MAX_SIZE 100000

void print_help(char *program_name) {
    /* Print the usage help of this program. */
    printf("Usage: %s <input file path>\n\n"
           "Loads an array given in a file in disk and prints it on the screen."
           "\n\n"
           "The input file must have the following format:\n"
           " * The first line must contain only a positive integer,"
           " which is the length of the array.\n"
           " * The second line must contain the members of the array"
           " separated by one or more spaces. Each member must be an integer."
           "\n\n"
           "In other words, the file format is:\n"
           "<amount of array elements>\n"
           "<array elem 1> <array elem 2> ... <array elem N>\n\n",
           program_name);
}

char *parse_filepath(int argc, char *argv[]) {
    /* Parse the filepath given by command line argument. */
    char *result = NULL;
    // Program takes exactly two arguments
    // (the program's name itself and the input-filepath)
    bool valid_args_count = (argc == 2);

    if (!valid_args_count) {
        print_help(argv[0]);
        exit(EXIT_FAILURE);
    }

    result = argv[1];

    return result;
}

int main(int argc, char *argv[]) {
    char *filepath = NULL;
    bool sorted=true; 
    /* parse the filepath given in command line arguments */
    filepath = parse_filepath(argc, argv);
    
    /* create an array of MAX_SIZE elements */
    int array[MAX_SIZE];
    
    /* parse the file to fill the array and obtain the actual length */
    unsigned int length = array_from_file(array, MAX_SIZE, filepath);
    
    /*dumping the array*/
    array_dump(array, length);

    sorted = array_is_sorted(array,length);
    if (sorted==true){
        printf("El arreglo esta ordenado");
    }
    else{
        printf("El arreglo no esta ordenado\n");
    }

/*
    if (array_is_sorted(array,length) == true)
    {
        printf ("El arreglo está ordenado");
    }
    else 
    {
        printf ("El arreglo no está ordenado");
    }    
    */
    
    return EXIT_SUCCESS;
}

//gcc -Wall -Werror -Wextra -pedantic -std=c99 -c array_helpers.c
//gcc -Wall -Werror -Wextra -pedantic -std=c99 -c main.c
//gcc -Wall -Werror -Wextra -pedantic -std=c99 array_helpers.o main.o -o reader
// ./reader input/example-easy.in


/*
En el ejercicio 4, nos piden incluir los booleanos en array_helpers.h 
pero vi que al quitarlo funciona igual y ni siquiera devuelve algun flag 
cuando compilamos. El codigo es el siguiente:
array_helpers.h del ej4

unsigned int array_from_file(int array[],
unsigned int max_size,
const char *filepath);

void array_dump(int a[], unsigned int length);

bool array_is_sorted(int a[], unsigned int length);
Eso sucede debido a que en el módulo main.c y (seguramente) en array_helpers.c 
haces un #include <stdbool.h> antes que #include "array_helpers.h" . Entonces, 
cuando el preprocesador copia el contenido de array_helpers.h ya antes había 
copiado la definición del tipo bool que está en stdbool.h, pero de repente si 
cambias el orden de las inclusiones, la compilación va a fallar. Sin embargo, 
si haces en array_helpers.h la inclusión de la librería stdbool.h (o sea, si 
agregas el #include <stdbool.h> allí) el éxito de la compilación ya no va a 
depender que por casualidad se haya hecho la inclusión de stdbool.h antes.
*/
