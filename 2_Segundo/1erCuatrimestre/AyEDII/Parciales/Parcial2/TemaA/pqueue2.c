#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include "pqueue.h"

struct s_pqueue {
    struct s_node *front; 
    unsigned int size; 
};

struct s_node {
    pqueue_elem elem; 
    unsigned int priority; 
    struct s_node *next; 
};

static struct s_node * create_node(pqueue_elem e, unsigned int priority) {
    struct s_node *new_node = NULL;
    // Completar
    new_node = malloc(sizeof(struct s_node));
    assert(new_node!=NULL);
    new_node->elem = e; 
    new_node->priority = priority; 
    new_node->next = NULL;     
    /*
     * COMPLETAR
     */
    return new_node;
}    

static struct s_node * destroy_node(struct s_node *node) {
    assert(node != NULL);
    node->next = NULL;         //OJO
    free(node);
    node=NULL;
    /*
     * COMPLETAR
     *
     */
    assert(node == NULL);
    return node;
}

//NO ANDA
/*
static bool invrep(pqueue s) {
    bool res=true;
    struct s_node *p=NULL; 
    p = s->front; 
    while(p!=NULL && res){                    
        if(p->next!=NULL){
            res = res && ((p->priority)<((p->next)->priority) || (p->priority)==((p->next)->priority));
            p=p->next;
        }
    }
    return res;
}
*/
static bool invrep(pqueue q) {
    struct s_node *p = q->front;
    // Si la cola está vacía o tiene un único elemento, se cumple la propiedad fundamental
    bool check = true;
    // Si la cola tiene al menos un elementos, tengo que chequearla con un bucle
    if (p != NULL){
        while((p->next != NULL) && check) {
            if (p->priority > p->next->priority) {
                check = false;
            }
            p = p->next;
        }
    }
    return check;
}

pqueue pqueue_empty(void) {
    pqueue q=NULL;
    q = malloc(sizeof(struct s_pqueue));
    q->size = 0u; 
    q->front=NULL; 
    assert(invrep(q) && pqueue_is_empty(q));
    return q;
}

pqueue pqueue_enqueue(pqueue q, pqueue_elem e, unsigned int priority) {
    assert(invrep(q));
    struct s_node *new_node = create_node(e, priority);
    struct s_node *r=NULL;
    if (pqueue_is_empty(q)){
        q->front = new_node;
        q->size = q->size +1u; 
    }
/*
        if(q->front==NULL && q->size == 0u){
            q->front = new_node;             //OJOO podria haber tenido elemenos y sacarlos y por eso queda en null. NO significa que el q sea null TODOOOOO
            q->size = q->size +1u; 
        }
*/
    else{        
        if(q->front->priority>priority){
            /*new_node->next = q->front;
            q->front = new_node;
            q->size = q->size +1u; 
            */
            r = q->front;
            q->front = new_node;
            new_node->next = r;
            q->size = q->size +1u; 
        }
        else{
            struct s_node *p=NULL;
            p = q->front;

            while(p->next!=NULL && (p->next->priority)<=priority){
                p = p->next;
            }
            r = p->next;
            p->next = new_node;
            new_node->next = r;
            q->size = q->size +1u; 
        }
    }
    assert(invrep(q) && !pqueue_is_empty(q));
    return q;
}

bool pqueue_is_empty(pqueue q) {
    assert(invrep(q));
    bool res = true; 
    res = q->front == NULL && q->size == 0u; 
    assert(invrep(q));
    return res;
}

pqueue_elem pqueue_peek(pqueue q) {
    assert(invrep(q) && !pqueue_is_empty(q));
    pqueue_elem first = q->front->elem;
    assert(invrep(q));
    return first;
}

unsigned int pqueue_peek_priority(pqueue q) {
    assert(invrep(q) && !pqueue_is_empty(q));
    unsigned int prio = q->front->priority;
    assert(invrep(q));
    return prio;
}

unsigned int pqueue_size(pqueue q) {
    assert(invrep(q));
    return q->size;
}

pqueue pqueue_dequeue(pqueue q) {
    assert(invrep(q) && !pqueue_is_empty(q));
    struct s_node *p=NULL; 
    p = q->front; 
    /*
    if(p->next!=NULL){
        p = p->next;
        q->front = q->front->next;
    }
    */
    q->front = q->front->next;
    q->size = q->size - 1;
    free(p);
    p=NULL; 
    assert(invrep(q));
    return q;
}

pqueue pqueue_destroy(pqueue q) {
    assert(invrep(q));
    /*
     * COMPLETAR
     *
     */
    struct s_node *p=NULL; 
    p = q->front;
    while (p!=NULL){
        struct s_node *killme=p;
        p = p->next;
        killme = destroy_node(killme);
    }
    free(q);
    q = NULL;                           
    assert(q == NULL);
    return q;
}
