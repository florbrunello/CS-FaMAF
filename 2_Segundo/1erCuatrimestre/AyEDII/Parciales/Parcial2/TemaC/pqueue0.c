#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include "pqueue.h"

struct s_pqueue {
    unsigned int size; 
    struct s_node **elems;
    unsigned int min_priority;                                                //Es de tipo priority_y
};

struct s_node {
    pqueue_elem elem; 
    struct s_node *next;
};

static struct s_node * create_node(pqueue_elem e) {
    struct s_node* new_node=NULL;
    new_node = malloc(sizeof(struct s_node));
    assert(new_node!=NULL);
    new_node->elem = e;
    new_node->next = NULL;
    return new_node;
}

static struct s_node * destroy_node(struct s_node *node) {
    assert(node != NULL);
    node->next = NULL;
    free(node);
    node = NULL;
    assert(node == NULL);
    return node;
}


static bool invrep(pqueue q) {
    struct s_node *p = NULL;
    unsigned int res = 0u; 
    bool respuesta = true; 
    for(unsigned int i = 0u; i<= q->min_priority; i++){
        if (q->elems[i]==NULL){
            res = res + 0u; 
        }
        else{
            p = q->elems[i];
            while(p!=NULL){
                p=p->next;
                res = res + 1u;
            }
        }
    }
    respuesta = q->size == res;
    return respuesta;
}

pqueue pqueue_empty(priority_t min_priority) {
    pqueue q=NULL;
    q = malloc(sizeof(struct s_pqueue));
    q->size = 0u;
    q->min_priority = min_priority;
    q->elems = calloc(min_priority+1u,sizeof(struct s_node));                             //Falto +1u
    for (unsigned int i = 0u; i<=min_priority; i++){
        q->elems[i] = NULL; 
    }
    assert(invrep(q) && pqueue_is_empty(q));
    return q;
}

pqueue pqueue_enqueue(pqueue q, pqueue_elem e, priority_t priority){
    assert(invrep(q) && priority <= q-> min_priority);
    struct s_node *new_node = create_node(e);

    struct s_node *p = NULL;
    p = q->elems[0];

    if(q->elems[priority]==NULL){
        q->elems[priority] = new_node;
    }
    else{ //q->elems[priority] != NULL
        p = q->elems[priority];
        while (p->next != NULL){
            p = p->next;
        }
        p->next = new_node;
    }
    q->size = q->size + 1u;
    assert(invrep(q) && !pqueue_is_empty(q));
    return q;
}

bool pqueue_is_empty(pqueue q) {
    assert(invrep(q));
    bool res = true; 
    for (unsigned int i=0u; i<=q->min_priority;i++){                           //FALTO CHEQUEAR ESTO?
        res = res && q->elems[i] == NULL; 
    }
    bool empty = (q->size == 0) && res;
    assert(invrep(q));
    return empty;
}

pqueue_elem pqueue_peek(pqueue q) {
    assert(invrep(q) && !pqueue_is_empty(q));
    unsigned int i = 0u;
    while (q->elems[i]==NULL){
        i++;
    }
    pqueue_elem first = (q->elems[i])->elem;
    assert(invrep(q));
    return first; 
}

priority_t pqueue_peek_priority(pqueue q) {
    assert(invrep(q) && !pqueue_is_empty(q));
    unsigned int i = 0u; 
    bool check = true;

    while(i<=q->min_priority && check){
        if(q->elems[i] == NULL){
            i++;
        }
        else{
            check = false; 
        }
    }
    unsigned int prio = i;
    assert(invrep(q));
    return prio;
}

size_t pqueue_size(pqueue q) {
    assert(invrep(q));
    unsigned int size = q->size;
    assert(invrep(q));
    return size;
}

pqueue pqueue_dequeue(pqueue q) {
    assert(invrep(q) && !pqueue_is_empty(q));
    unsigned int prio=0u; 
    prio = pqueue_peek_priority(q);
    
    struct s_node * killme = q->elems[prio];
    q->elems[prio] = q->elems[prio]->next;
    killme = destroy_node(killme);
    (q->size)--;
    assert(invrep(q));
    return q;
}

pqueue pqueue_destroy(pqueue q) {
    assert(invrep(q));
    for (unsigned int i = 0u; i <=q->min_priority; i++){
        struct s_node *p = q->elems[i];
        while (q->elems[i] != NULL) {         
            q->elems[i] = q->elems[i]->next; 
            destroy_node(p);
            p = q->elems[i];
        }
    }
    free(q->elems);                                                          //FALTA LIBERAR Q->ELEMS
    q->elems = NULL; 
    free(q);
    q = NULL;
    assert(q == NULL);
    return q;
}