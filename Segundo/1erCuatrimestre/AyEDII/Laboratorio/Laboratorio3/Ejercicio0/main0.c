#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 1000 /* se usa de manera global */

static void dump(char a[], unsigned int length) {
    printf("\"");
    for (unsigned int j=0u; j < length; j++) {
        printf("%c", a[j]);
    }
    printf("\"");
    printf("\n\n");
}

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
    bool valid_args_count = (argc == 2);
    /*  si no tiene dos argumetnos*/
    if (!valid_args_count) {
        print_help(argv[0]);
        exit(EXIT_FAILURE);
    }

    result = argv[1];

    return result;
}

unsigned int data_from_file (const char *path, 
                            unsigned int indexes[],
                            char letters[],
                            unsigned int max_size){
    FILE *fp; 
    fp = fopen(path,"r");
    unsigned int length = 0u; 
    while ((!feof(fp)) && (length < max_size)){
        fscanf (fp,"%u '%c'\n", &indexes[length], &letters[length]);
        length = length + 1;
    }

    fclose(fp);
    return length;    
}

int main(int argc, char *argv[]) {
    //FILE *file;
    unsigned int indexes[MAX_SIZE];
    char letters[MAX_SIZE];
    char sorted[MAX_SIZE];
    unsigned int length=0; 
    //  .----------^
    //  :
    // Debe guardarse aqui la cantidad de elementos leidos del archivo
    
    /* -- completar -- */

    /* parse the filepath given in command line arguments */
    char* path = NULL; 
    path = parse_filepath(argc, argv);
        
    /* parse the file to fill the array and obtain the actual length */
    length = data_from_file(path, indexes, letters, MAX_SIZE);

    unsigned int j = 0; 
   
    for (unsigned int i = 0u; i < length; i++){
        j = indexes[i];
        sorted[j] = letters[i]; 
    }

    dump(sorted, length);

    return EXIT_SUCCESS;
}

/* FILE : tipo de vairable. FP es un punetro a file descriptor (tipo de variable)
arse_filepath(argc, argv) devuelve el nombre del archiv 
printf("%u %u",length, indexes[length]);

gcc -Wall -Werror -Wextra -pedantic -std=c99 main.c
gcc -Wall -Werror -Wextra -pedantic -std=c99 main.c -o ej0
usuario@usuario-CX215XX-CX212XX:~/Escritorio/AyEDII/Laboratorios/Laboratorio3/lab03/ej0$ ./main phrase1.in
"Hola gente! Como les va?"
*/
