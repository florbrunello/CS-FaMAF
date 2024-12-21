#include <stdlib.h>
#include <assert.h>
#include "stack.h"


struct _s_stack{
    stack_elem elem;
    struct _s_stack * next;
};

stack stack_empty(){
    stack s; 
    s=NULL; 
    return s; 
}

stack stack_push(stack s, stack_elem e){
    stack p=NULL; 
    p = malloc(sizeof(struct _s_stack));
    p->elem = e; 
    p->next = s; 
    s = p;              //NO OLVIDAR
    return s; 
}
stack stack_pop(stack s) {
    assert(!stack_is_empty(s));
    stack p = s;
    s = s->next;
    p->next = NULL;
    stack_destroy(p);
    return s;
}
/*
stack stack_pop(stack s){
    assert(s!=NULL);
    stack p=NULL; 
    p = s;
    if (s->next!=NULL){
        s = s->next;         //OJO VIOLACION DE SEGMENTO SI S TIENE UN SOLO ELEMENTO
        free(p);    
    }  
    else{
        free(p);
        s=NULL; 
    }        
    return s; 
}
*/
unsigned int stack_size(stack s){
    stack p = s; 
    unsigned int n = 0; 
    while (p != NULL){
        p = p->next;
        n = n+1; 
    }
    return n; 
}

stack_elem stack_top(stack s){
    assert(s!=NULL);
    stack_elem e = s->elem;
    return e;
}

bool stack_is_empty(stack s){
    bool res = true; 
    res = s == NULL; 
    return res; 
}

stack_elem *stack_to_array(stack s){
    stack_elem *array=NULL; 
    array = calloc(stack_size(s),sizeof(stack_elem));

    stack p=NULL; 
    p = s; 

    for(unsigned int i = 0u; i<stack_size(s);i++){
        array[(stack_size(s)-i)-1u] = p->elem;
        p = p->next;
    }
    return array;
}
/*
stack_elem *stack_to_array(stack s) { 
    stack_elem *array = NULL;
    stack p = s;
    if (stack_is_empty(s)) {
        array = NULL;
    } else {
        unsigned int size = stack_size(s);
        array = calloc(size, sizeof(stack_elem));
        for (unsigned int i = 0; i < size; i++) {
            array[size-1-i] = p->elem;
            p = p->next;
        }
    }

    return array;
}
*/
stack stack_destroy(stack s){
    stack p = NULL; 
    p = s;
    while (s!=NULL){
        p = s; 
        s = s->next; 
        free(p);
        p = NULL;  //EN LA ultima iteracion no queda colgando
    }
    return s; 
}
/*

stack stack_destroy(stack s) {
    stack p = s;
    while (!stack_is_empty(s)) {
        s = s->next;
        p->next = NULL;
        free(p);
        p = s;
    }

    return s;
}
*/