#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 1000

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

static void dump(char a[], unsigned int length) {
    printf("\"");
    for (unsigned int j=0u; j < length; j++) {
        printf("%c", a[j]);
    }
    printf("\"");
    printf("\n\n");
}

unsigned int data_from_file(const char *path,unsigned int indexes[],char letters[],unsigned int max_size){
    unsigned int i=0u; 
    unsigned int size=0u;
    int res = 0;   

    FILE *file=NULL;

    file = fopen(path, "r");
    if (file == NULL) {
        fprintf(stderr, "File does not exist.\n");
        exit(EXIT_FAILURE);
    }    
    
    while(!feof(file) && i<max_size){
        res = fscanf(file,"%u '%c'\n",&indexes[i],&letters[i]); 
        if (res != 2) {
            fprintf(stderr, "Invalid format.\n");
            exit(EXIT_FAILURE);
        }
        
        //Chequear letters[i] sea < max_size para la parte b
        //Evita violaciones de segmento

        i++;    
    }
    size = i;
    fclose(file);
    return size;
}


void sort_word(char letters[],unsigned int indexes[],char sorted[],
        unsigned int length) {

    for (unsigned int i = 0; i < length; i++) {
        sorted[indexes[i]] = letters[i];
    }
}

int main(int argc, char *argv[]) {
    unsigned int indexes[MAX_SIZE];
    char letters[MAX_SIZE];
    char sorted[MAX_SIZE];
    unsigned int length=0; 
    //  .----------^
    //  :
    // Debe guardarse aqui la cantidad de elementos leidos del archivo
    
    char *filepath = NULL;

    /* parse the filepath given in command line arguments */
    filepath = parse_filepath(argc, argv);
       
    length = data_from_file(filepath,indexes,letters,MAX_SIZE);
    /* -- completar -- */
    sort_word(letters, indexes, sorted, length);

    dump(sorted, length);
    
    return EXIT_SUCCESS;
}
