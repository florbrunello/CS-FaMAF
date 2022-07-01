#include <stdio.h>
#include "strfuncs.h"

int main (void){
    char *cadena="h.o.l.a m.u.n.d.o.!";
    char *res = malloc(sizeof(char));
    //NO uso malloc porque string_filter hace eso. 
    //Crea un char* y para ello usa malloc
    size_t length_res = 0;

    printf("'%s' (%ld)\n",cadena,string_length(cadena));
    
    res = string_filter(cadena,'.');
    length_res = string_length(res);
    printf("'%s' (%ld)\n",res,length_res);
    
    free(res);
    // FALTA res = NULL; 
    return 0;
}