#include <stdlib.h>
#include <assert.h>
#include "stack.h"

struct _s_stack{
    stack_elem elem;
    struct _s_stack *next;
};

stack stack_empty(){
    stack s=NULL; 
    return s; 
}

stack stack_push(stack s, stack_elem e){
    stack q = malloc(sizeof(struct _s_stack));
    q->elem = e; 
    q->next = s; 
    s = q;
    return s; 
}

stack stack_pop(stack s){
    stack p=s; 
    if(!stack_is_empty(s)){
        s = s->next; 
        p->next = NULL; 
        stack_destroy(p);
    }
    return s; 
}

unsigned int stack_size(stack s){
    stack p = s; 
    unsigned int n = 0u; 
    while (p != NULL){
        p = p->next;
        n++; 
    }
    return n;    
}

stack_elem stack_top(stack s){
    assert(!stack_is_empty(s));
    return s->elem; 
}

bool stack_is_empty(stack s){
    bool res = (s == NULL); 
    return res; 
}

stack_elem *stack_to_array(stack s){

    //OJO USAR CALLOC

    stack_elem *array; 

    if (!stack_is_empty(s)){
    stack p = s;    
    unsigned int n = stack_size(s);
    stack_elem *array = calloc(n,sizeof(stack_elem));        

        for (unsigned int i = 0u; i < n; i++){
                array[(n-1)-i] = stack_top(p);
                p = p->next;
            }
    }
    else{
        array = NULL; 
    }
    return array;
}

stack stack_destroy(stack s){
    stack p; 
    while(s!=NULL){
        p = s; 
        s = s->next; 
        p->next = NULL; 
        free(p);
    }
    free(s);
    s = NULL; 
    return s; 
}

//.h especifica cuando usar assert