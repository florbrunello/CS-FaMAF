/* First, the standard lib includes, alphabetically ordered */
/* header files*/
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "array_helpers.h"
#include "mybool.h"

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
    /* solo dos argumentos*/
    /* cantidad de argumentos que se le pasa al arreglo argv - filepath = ruta del archivo - parse_filepath: ruta de análisis */
    char *result = NULL;
    // Program takes exactly two arguments
    // (the program's name itself and the input-filepath)
    mybool valid_args_count = (argc == 2);
    /*  si no tiene dos argumetnos*/
    if (!valid_args_count) {
        print_help(argv[0]);
        exit(EXIT_FAILURE);
    }

    result = argv[1];

    return result;
}

int main(int argc, char *argv[]) {
    char *filepath = NULL;

    /* parse the filepath given in command line arguments */
    filepath = parse_filepath(argc, argv);
    
    /* create an array of MAX_SIZE elements */
    int array[MAX_SIZE];
    
    /* parse the file to fill the array and obtain the actual length */
    unsigned int length = array_from_file(array, MAX_SIZE, filepath);
    
    /*dumping the array*/
    array_dump(array, length);
    
    if (array_is_sorted(array,length) == true)
    {
        printf ("El arreglo está ordenado");
    }
    else 
    {
        printf ("El arreglo no está ordenado");
    }    
    return EXIT_SUCCESS;
}

/* ¿Por qué falla la compilación?
In file included from ej5.c:7:0:
mybool.h:4:13: error: redefinition of typedef ‘mybool’ [-Werror=pedantic]
 typedef int mybool;
             ^~~~~~
In file included from array_helpers.h:1:0,
                 from ej5.c:6:
mybool.h:4:13: note: previous declaration of ‘mybool’ was here
 typedef int mybool;

El problema surge porque redefinimos el tipo mybool pues cuando no utilizamos #ifndef 
incluimos el tipo mybool de forma repetida.
Al incluirlo la primera vez, no está definido my_bool_h, se copia todo al archivo y luego termina.
*/

//gcc -Wall -Werror -Wextra -pedantic -std=c99 -c array_helpers.c
//gcc -Wall -Werror -Wextra -pedantic -std=c99 -c main.c
//gcc -Wall -Werror -Wextra -pedantic -std=c99 array_helpers.o main.o -o reader
// ./reader input/example-easy.in
