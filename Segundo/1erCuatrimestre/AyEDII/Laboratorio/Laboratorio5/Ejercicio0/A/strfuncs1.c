#include "strfuncs.h"
#include <stdlib.h>

size_t string_length(const char *str){
    size_t length = 0u; 
    unsigned int i = 0u;
    const char *p = NULL; 
    p = str; 
    while (p[i]!='\0'){
        length++;
        i++;
    }
    return length; 
}
/*
size_t string_length(const char *str) {
    size_t size = 0;
    unsigned int i = 0;

    while (str[i] != '\0') {
        size++;
        i++;
    }

    return size;
}
*/

char *string_filter(const char *str, char c){
    char *res = NULL; 
    size_t length = string_length(str);
    res = calloc(length,sizeof(char));    //RESERVO MEMORIA DE MAS
    unsigned int j=0u;
    for(unsigned int i=0u; i<length; i++){
        if(str[i] != c){
            res[j] = str[i];
            j++;        
        }
    }
    return res; 
}

/*
char *string_filter(const char *str, char c) {
    unsigned int c_count = 0u, i = 0u;
    while (str[i] != '\0') {
        if (str[i] == c) {
            c_count++;
        }
        i++;
    }

    unsigned int new_len = string_length(str) - c_count;
    char *new_str = NULL;
    new_str = malloc(sizeof(char) * (new_len + 1));

    unsigned int j = 0u, k = 0u;
    while (str[j] != '\0') {
        if (str[j] != c) {
            new_str[k] = str[j];
            k++;
        }
        j++;
        new_str[new_len] = '\0';
    }

    return new_str;
}
*/