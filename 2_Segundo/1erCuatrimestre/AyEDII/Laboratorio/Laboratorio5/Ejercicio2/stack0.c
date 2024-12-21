#include <stdlib.h>
#include <assert.h>
#include "stack.h"

//Hacer funcion inv y chequear
//Considero que el ultimo elemento del arreglo es el top del stack

struct _s_stack {
    stack_elem *elems;      // Arreglo de elementos
    unsigned int size;      // Cantidad de elementos en la pila
    unsigned int capacity;  // Capacidad actual del arreglo elems
};

//INVARIANTES DE REPRESENTACION
bool cap_is_cero (stack s){
    bool res; 
    res = s->capacity == 0u;
    return res;
}

bool size_smaller_cap (stack s){
    bool res; 
    res = s->size < s->capacity;
    return res; 
}

bool size_equal_cap (stack s){
    bool res; 
    res = s->size == s->capacity;
    return res; 
}

stack stack_empty(){
    stack s = malloc(sizeof(struct _s_stack));
    s->elems = NULL; 
    s->size = 0u;
    s->capacity = 0u; //?
    return s; 
}

stack stack_push(stack s, stack_elem e){
    if(cap_is_cero(s)){
        s->elems = malloc(2 * sizeof(stack_elem));
        s->capacity = 1u; 
        s->elems[s->size] = e; 
        s->size = s->size + 1u; 
        //ojo usar malloc y s->elems
    }    
    else if (size_smaller_cap(s)){
        s->elems[s->size] = e; 
        s->size = s->size + 1u; 
    }
    else if(size_equal_cap(s)){
        s->elems = realloc(s->elems,2 * s->capacity * sizeof(stack_elem));
        s->elems[s->size] = e;
        s->capacity = (2*s->capacity);
        s->size = s->size + 1u; 
    }
    return s; 
}
// OBS: capacity no se achica nunca. Solo añado memoria. 

stack stack_pop(stack s){
    assert(!stack_is_empty(s));
    s->size = s->size - 1u; 
    return s; 
}

unsigned int stack_size(stack s){
    return s->size; 
}

stack_elem stack_top(stack s){
    assert(!stack_is_empty(s));
    return s->elems[s->size-1u];
}

bool stack_is_empty(stack s){
    bool res; 
    res = s->size == 0u; 
    return res; 
}

stack_elem *stack_to_array(stack s){
    stack_elem *new_array = NULL; 
    if(stack_is_empty(s)){
        new_array = NULL;
    }
    else{
        new_array = calloc (stack_size(s),sizeof(stack_elem));
        for (unsigned int i = 0u; i < stack_size(s); i++){
            new_array[i] = s->elems[i];
        }
    }
    return new_array;
}

stack stack_destroy(stack s){
    s->size = 0u; 
    s->capacity = 0u;     
    
    free(s->elems); 
    s->elems = NULL; 

    free(s); 
    s=NULL; 

    return s; 
}
