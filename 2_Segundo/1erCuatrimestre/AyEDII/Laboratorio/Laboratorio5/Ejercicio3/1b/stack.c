#include <stdlib.h>
#include <assert.h>
#include "stack.h"

//VALGRIND ->
/*
==4322== HEAP SUMMARY:
==4322==     in use at exit: 16 bytes in 1 blocks
==4322==   total heap usage: 1 allocs, 0 frees, 16 bytes allocated
==4322== Invalid read of size 8
==4322==    at 0x1087C6: stack_push (stack.c:29)
==4322==    by 0x108A4B: main (test.c:8)
==4322==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
*/

//Hacer funcion inv y chequear con assert

struct _s_node{
    stack_elem elem;
    struct _s_node *next;
};

struct _s_stack{
    struct _s_node *fst; 
    unsigned int size;
};

stack stack_empty(){
    stack s=malloc(sizeof(struct _s_stack));
    s->fst = NULL; 
    s->size = 0u;
    return s; 
}

stack stack_push(stack s, stack_elem e){
    struct _s_node *q = malloc(sizeof(struct _s_node));
    q->elem = e; 
    q->next = s->fst; 
    s->fst = q; 
    s->size = s->size + 1u;     
    return s; 
}

stack stack_pop(stack s){
    assert(!stack_is_empty(s));
    struct _s_node *p=NULL; 
    p = s->fst;
    s->fst = (s->fst)->next; 
    p->next = NULL; 
    free(p);
    p=NULL;
    s->size = s->size - 1u; 
    return s; 
}

unsigned int stack_size(stack s){
    return s->size;    
}

//La cantidad de operaciones que haga no debe depender de la cantidad de elementos de la pila. 
//No crece linealmente la cantidad de operaciones

stack_elem stack_top(stack s){
    assert(!stack_is_empty(s));
    return (s->fst)->elem; 
}

bool stack_is_empty(stack s){
    bool res = (s->size == 0u); 
    return res; 
}

stack_elem *stack_to_array(stack s){

    //OJO USAR CALLOC

    stack_elem *array; 

    if (!stack_is_empty(s)){
    struct _s_node *p = s->fst;    
    unsigned int n = stack_size(s);
    stack_elem *array = calloc(n,sizeof(stack_elem));
        for (unsigned int i = 0u; i < n; i++){
                array[(n-1)-i] = p->elem;
                p = p->next;
            }
    }
    else{
        array = NULL; 
    }
    return array;
}

stack stack_destroy(stack s){
    s->size = 0u;
    struct _s_node *p=NULL; 
    p = s->fst; 
    while(s->fst!=NULL){
        s->fst = (s->fst)->next; 
        p->next = NULL; 
        free(p);
        p = s->fst; 
    }
    free(s);
    s = NULL; 
    return s; 
}