#include <stdio.h>
#include <stdlib.h>
#include "strfuncs.h"

size_t string_length(const char *str){
    unsigned int i = 0u;

    if (str == NULL){
        return 0;
    }
    while (str[i]!='\0'){
        i++;
    }
    return i; 
}

//OJO caso str == NULL

char *string_filter(const char *str, char c){
    size_t length = string_length(str);
    unsigned int j = 0u;
    char *new_str = NULL; 
    new_str = malloc(length * sizeof(char));

    for (unsigned int i = 0u; i<length; i++){
        if (str[i] != c){
            new_str[j] = str[i];
            j++;
        }
    }
    return new_str; 
}

//OJO inicializar *new_str = NULL; 