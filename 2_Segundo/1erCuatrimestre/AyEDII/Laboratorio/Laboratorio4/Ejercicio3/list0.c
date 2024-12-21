#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "list.h"

struct node_t {
    list_elem elem;
    struct node_t * next;
};

list empty(){
    return NULL; 
}

list addl(list_elem e,list l){
    list p = NULL; 
    p = malloc(sizeof(list)); 
    p->elem = e; 
    p->next = l; 
    return p; 
}

list destroy(list l){
  if(l != NULL) {
    list a, b;
    a = l;
    b = a->next;
    while(a != NULL) {
      free(a);
      a = b;
      if(a != NULL) {
        b = a->next;
      }
    }
    l = a;
  }
  return l;
}

bool is_empty(list l){
    return l == NULL; 
}

list_elem head(list l){
    assert(!is_empty(l));
    return l->elem;
}

list tail(list l){
    assert(!(is_empty(l)));
    return l->next;
}

list addr(list l, list_elem e){
    list p; 

    list q = NULL; 
    q = malloc(sizeof(list));
    q->elem = e; 
    q->next = NULL; 

    if (l!=NULL){
        p = l; 
        while (p->next != NULL){
            p = p->next;
        }
        p->next = q; 
    }
    else{
        l = q; 
    }
    return l; 
}

int length(list l){
    list p = l; 
    int n = 0; 
    while (p != NULL){
        p = p->next;
        n = n+1; 
    }
    return n; 
}

list concat(list l, list l1){
    list p = NULL; 
    if (is_empty(l)){
        l = l1; 
    }
    else{
        p = l;
        while (p->next != NULL){
            p = p->next;
        }
        p->next = l1; 
    }
    return l; 
}

list_elem index(list l, int n){
    assert(length(l) > n);
    list p = l; 
    for (int i = 1; i < n; i++){
        p = p->next; 
    }
    return p -> elem; 
}

list take(list l, int n){
    list p = NULL; 
    if (!is_empty(l)){
        p = l; 
        for (int i = 1; i < n; i++){
            p = p->next;
        }
        p = p-> next; 
        destroy(p);
    }
    return l; 
}

list drop(list l, int n){
    list p = NULL; 
    if (!is_empty(l)){
        p = l; 
        for (int i = 1; i < n; i++){
            p = p->next; 
        }
        p = p->next; 
    }
    return l; 
}

list copy_node(list l){
    list q;
    q = malloc(sizeof(list));
    q->next = NULL;
    if (l->next!=NULL){
        q->elem = l->elem; 
        q->next = l->next; 
    }
    return q; 
}

list copy_list(list l){
    list c=NULL; 
    c = copy_node(l);
    list s=NULL; 

    list p,q; 
    p = NULL; 
    q = NULL; 
    p = s; 
    q = c; 
    if (s!=NULL){
        while(p->next != NULL){
            q->next = copy_node(p->next);
            p = p->next;
            q = q->next;
        }
    }
    destroy(p);
    destroy(q);
    return c; 
}