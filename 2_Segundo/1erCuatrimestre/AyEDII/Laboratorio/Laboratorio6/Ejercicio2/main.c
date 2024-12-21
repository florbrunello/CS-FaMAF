#include <stdio.h>
#include "string.h"

int main (){
    string palabra; 
    string palabra2;
    palabra = string_create ("aba");
    palabra2 = string_create("aaa");
    //bool res; 
    bool res2;
    //res = string_less(palabra, palabra2);
    res2 = string_eq(palabra,palabra2);
    printf("%d\n",res2);

    return 0;
}