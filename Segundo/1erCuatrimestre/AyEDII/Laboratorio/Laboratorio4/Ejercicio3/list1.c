#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "list.h"

struct node_t{
    list_elem elem; 
    struct node_t *next;
};

list empty(void){
    list l = NULL;
    return l; 
}

list addl (list_elem e, list l){
    list p = NULL; 
    p = malloc(sizeof(struct node_t));
    p->elem = e; 
    p->next = l; 
    l = p;
    return l; 
}

list destroy(list l){
    list p = NULL; 
    p = l; 
    while (l!=NULL){
        p = l; 
        l = l->next; 
        free(p);
        p = NULL;  //EN LA ultima iteracion no queda colgando
    }
    return l; 
}

bool is_empty (list l){
    bool res = true; 
    res = l == NULL; 
    return res; 
}

list_elem head(list l){
    assert(l!=NULL);
    list_elem e = l->elem; 
    return e; 
}

list tail (list l){
    assert(l!=NULL);
    list p = NULL; 
    p = l;
    l = l->next; 
    free(p);
    p = NULL; 
    return l; 
}

list addr(list l, list_elem e){
    // OJO caso l == NULL 
    list p = NULL; 
    p = malloc(sizeof(struct node_t));
    p->elem = e; 
    p->next = NULL; 

    if (l == NULL){
        l = p; 
    }
    else{
        list q = NULL; 
        q = l; 
        while (q->next != NULL){
            q = q->next;        // q = q->next; 
        }    
        q->next = p;
    }
    return l; 
}

unsigned int length (list l){
    unsigned int length = 0u; 
    if (l == NULL){
        length = 0u;
    }
    else{
        list p = NULL; 
        p = l;
        while(p!=NULL){
            p = p->next; 
            length++;
        } 
        /*
        length = 1u; 
        while(p->next!=NULL){
            p = p->next; 
            length++;
        }
        */
    }
    return length; 
}

list concat(list l0, list l1){
    if (l0==NULL){
        l0 = l1;
    }
    else{
        list p = NULL; 
        p = l0; 
        while (p->next!=NULL){  //USAR p->next y no p porque sino termino con p = NULL
            p = p->next;        // y pierdo la referencia del ultimo elem de l0
        }
        p->next=l1; 
    }
    return l0;
}
/*
USAR UNA COPIA DE L2 Y NO L2 SINO MODIFICO L2 ??
list concat(list l1, list l2) {
    list l2c = copy_list(l2);
    list p = l1;
    while (p->next != NULL) {
        p = p->next;
    }
    p->next = l2c;
    return l1;
}
*/

list_elem index(list l, unsigned int n){
    assert(length(l)>n);
    unsigned int i = 0u;
    list_elem e; 
    list p = NULL; 
    p = l; 
    while(i<n){
        p = p->next;
        i++;
    }
    e = p->elem; 
    return e; 
}

list take(list l, unsigned int n){
    if(l==NULL){
        return l; 
    }
    else if(length(l) == n){
        return l;
    }
    else if(length(l) < n){
        return l; 
    }
    else if(n==0){
        l = destroy(l);
        return l;
    }    
    else if(length(l) > n){
        list p=NULL; 
        list q=NULL; 

        unsigned int i = 0u;
        p = l; 
        while(i<n){ //&& p->next!=NULL SI NO PUSIERA TODAS LAS GUARDAS ANTERIORES
            p = p->next;
            i++;
        }
        //se puede USAR DESTROY
        while (p!=NULL){
            q = p; 
            p = p->next; 
            free(q);
            q=NULL; 
        }
    }
    return l;
}
/*
list take(list l, unsigned int n) {
    list p = l, q;
    unsigned int i = 0u;
    if (n == 0) {
        l = NULL;
        p = list_destroy(p);
    } else if (!is_empty(l)) {
        while (i < n-1 && p->next != NULL) {
            p = p->next;
            i++;
        }
        q = p->next;
        p->next = NULL;
        q = list_destroy(q);
    }
    return l;
}
*/ 

list drop(list l, unsigned int n){
    list p = NULL; 
    unsigned int i = 0u;
    p = l; 
    while (l!=NULL && i<n){
        p = l; 
        l = l->next; 
        free(p);
        p = NULL;  //EN LA ultima iteracion no queda colgando
        i++;
    }
    return l; 
}

list copy_list(list l){
   list p = NULL;
   p = l; 

   list copy = NULL; 
   copy = malloc(sizeof(struct node_t) * length(l));

   while(p!=NULL){
       copy = addr(copy,p->elem);
       p = p->next;
   } 
   return copy;
}
