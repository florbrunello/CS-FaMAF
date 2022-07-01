/* First, the standard lib includes, alphabetically ordered */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

/* Then, this project's includes, alphabetically ordered */
#include "array_helpers.h"
#include "sort_helpers.h"
#include "sort.h"

/* Maximum allowed length of the array */
static const unsigned int MAX_SIZE = 100000u;

void print_help(char *program_name) {
    /* Print the usage help of this program. */
    printf("Usage: %s <input file path>\n\n"
           "Sort an array given in a file in disk.\n"
           "\n"
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

    if (argc < 2) {
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

    /* create a copy of the array */
    int copy[MAX_SIZE];
    array_copy(copy, array, length);

    /* reset counters and set time */
    reset_comparisons_counter();
    reset_swaps_counter();
    set_current_time();

    /* do the actual sorting */
    selection_sort(copy, length);

    /* show statistics for selection_sort */
    printf("statistics for selection_sort\n");
    printf("time elapsed=%g,    comparisons: %10u,    swaps: %10u\n", calculate_elapsed_time(), comparisons_number(), swaps_number());

    /* all the same for insertion_sort */
    /* Usando la idea de las líneas de códigos anteriores
       muestre las estadísticas (tiempo de ejecución, número de comparaciones e
       intercambios realizados) para insertion_sort. No te olvides que antes debes
       copiar el arreglo original, resetear los contadores y setear el tiempo.
    */    
   /* create a copy of the array */
    int copy2[MAX_SIZE];
    array_copy(copy2, array, length);

    /* reset counters and set time */
    reset_comparisons_counter();
    reset_swaps_counter();
    set_current_time();

    /* do the actual sorting */
    insertion_sort(copy2, length);

    /* show statistics for selection_sort */
    printf("statistics for insertion_sort\n");
    printf("time elapsed=%g,    comparisons: %10u,    swaps: %10u\n", calculate_elapsed_time(), comparisons_number(), swaps_number());


    /* all the same for quick_sort */
    /* Usando la idea de las líneas de códigos anteriores
       muestre las estadísticas (tiempo de ejecución, número de comparaciones e
       intercambios realizados) para quick_sort. No te olvides que antes debes
       copiar el arreglo original, resetear los contadores y setear el tiempo.
    */
    /* create a copy of the array */
    int copy3[MAX_SIZE];
    array_copy(copy3, array, length);

    /* reset counters and set time */
    reset_comparisons_counter();
    reset_swaps_counter();
    set_current_time();

    /* do the actual sorting */
    quick_sort(copy3, length);

    /* show statistics for selection_sort */
    printf("statistics for quick_sort\n");
    printf("time elapsed=%g,    comparisons: %10u,    swaps: %10u\n", calculate_elapsed_time(), comparisons_number(), swaps_number());

    return EXIT_SUCCESS;
}

/*
Compilacion
gcc -Wall -Werror -Wextra -pedantic -std=c99 -c array_helpers.c sort.c main.c
gcc -Wall -Werror -Wextra -pedantic -std=c99 -no-pie array_helpers.o sort.o sort_helpers.o main.o -o sorter
./sorter ../input/example-unsorted.in
*/

/* 
Conclusiones: 
1) Para el acaso de arreglos desordenados, con un tamaño relativamente grande, el mas eficiente sera
quick_sort puesto que hace menor cantidad de comparaciones. Notar que esto ocurre para los arreglos 
all-negative-100, all-positive-100.in y unsorted (arreglos desordenados segun goes_before).

2) Para el caso de arreglos ordenados de forma descendente segun goes_before, los algoritmos
mas eficientes son selecion_sort y quick_sort con una diferencia de tiempo similar considerando 
la longtud de los arreglos. Además, los swaps que realizan siempre difieren en 1. No ocurre lo mismo
con las comparaciones, lo que marca la diferencia de eficiencia segun el caso. 

3) Concluimos de example-sorted.in, sorted-asc-100.in, sorted-asc-1000.in, sorted-asc-10000.in
que para los casos en que el arreglo esté ordenado según goes_before (en modulo), el algoritmo 
de ordenacion que menos demora es insertion_sort puesto que hace menos swaps y comparaciones. 

4) Para el caso de un arreglo desordenado segun goes_before y de pocos elementos (5), el algoritmo mas
eficiente es el insertion_sort debido a la menor cantidad de comparaciones que realiza. 
*/
