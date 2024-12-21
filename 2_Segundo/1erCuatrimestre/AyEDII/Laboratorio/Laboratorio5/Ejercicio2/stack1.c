#include <stdlib.h>
#include <assert.h>
#include "stack.h"

struct _s_stack {
    stack_elem *elems;      // Arreglo de elementos
    unsigned int size;      // Cantidad de elementos en la pila
    unsigned int capacity;  // Capacidad actual del arreglo elems
};


stack stack_empty(){
    stack s=NULL; 
    s = malloc(sizeof(struct _s_stack));
    s->elems = NULL; 
    s->size = 0u; 
    s->capacity = 0u; 
    return s; 
}

stack stack_push(stack s, stack_elem e){
    if(s->size==s->capacity){
        s->elems = realloc(s->elems,2*s->capacity*sizeof(stack_elem) );    /////OOOOOOJOOOOOOOOO
        s->elems[s->size] = e; 
        s->capacity = 2 * s->capacity;
    }
    else if(s->size<s->capacity){
        s->elems[s->size] = e;
    }
    else if(s->capacity == 0u){
        s->elems = malloc(sizeof(stack_elem));
        s->capacity = 1u;
        s->elems[s->size] = e;
        s->size = s->size + 1u;
    }
    s->size = s->size + 1u; 
    return s; 
}

stack stack_pop(stack s){
    assert(!stack_is_empty(s));
    s->size = s->size - 1u; 
    return s;
}

unsigned int stack_size(stack s){
    unsigned int size; 
    size = s->size;
    return size;
}

stack_elem stack_top(stack s){
    assert(!stack_is_empty(s));
    stack_elem e;
    e = s->elems[s->size-1u];
    return e; 
}

bool stack_is_empty(stack s){
    bool res = true; 
    res = s->size == 0u && s->capacity == 0u && s->elems == NULL;
    return res; 
}

stack_elem *stack_to_array(stack s){
    stack_elem *copy=NULL;     
    if(s!=NULL && s->elems!=NULL){
        copy = calloc(stack_size(s)+1u,sizeof(stack_elem));

        for (unsigned int i=0u;i<s->size;i++){
            copy[i] = s->elems[i];
        }
    }
    else{
        return copy;
    }
    return copy; 
}

stack stack_destroy(stack s){
    free(s->elems);
    s->elems = NULL; 
    free(s);
    s = NULL; 
    return s; 
}
