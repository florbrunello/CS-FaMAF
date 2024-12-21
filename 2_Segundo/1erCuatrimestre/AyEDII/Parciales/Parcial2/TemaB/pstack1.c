#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include "pstack.h"

struct s_pstack {
    /*
     * COMPLETAR
     *
     */
    struct s_node * front;
    struct s_node * last;
    unsigned int size;

};

struct s_node {
    pstack_elem elem; 
    priority_t priority;
    struct s_node *next; 

};

static struct s_node * create_node(pstack_elem e, priority_t priority) {
    struct s_node *new_node = NULL;
    // Completar
    new_node = malloc(sizeof(struct s_node));
    assert(new_node!=NULL);
    /*
     * COMPLETAR
     */
    new_node->elem = e; 
    new_node->priority = priority; 
    new_node->next = NULL;     //revisar
    return new_node;
}

static struct s_node * destroy_node(struct s_node *node) {
    assert(node != NULL);
    node->next=NULL; 
    free(node);
    node=NULL;
    /*
     * COMPLETAR
     *
     */
    assert(node == NULL);
    return node;
}


static bool invrep(pstack s) {
    bool res=true;
    struct s_node *p=NULL; 
    p = s->front; 
    while(p!=NULL){                    //OJO NO USAR FUNCIONES !!! //OJOO NO HACER VIOLACION DE SEGMENTO -- SI PONGO P!=Null Y DESPUES QUIERO ACCEDER A P->NEXT ESTA MAL
        if(p->next!=NULL){
            res = res && ((p->priority)>((p->next)->priority) || (p->priority)==((p->next)->priority));
            p=p->next;
        }
        else{
            return res;
        }
    }
    return res;
}

pstack pstack_empty(void) {
    pstack s=NULL;
    /*
     */
    s = malloc(sizeof(struct s_pstack));
    s->size = 0u; 
    s->front = NULL; 
    s->last = NULL; 
    assert(invrep(s) && pstack_is_empty(s));
    return s;
}

pstack pstack_push(pstack s, pstack_elem e, priority_t priority) {
    assert(invrep(s));
    struct s_node *new_node = create_node(e, priority);
    if (s->front==NULL){
        s->front=new_node;
        s->last=new_node;
        return s; 
    }
    else if(priority>(s->front)->priority || priority==(s->front)->priority){
        new_node->next=s->front;
        s->last = s->front;
        s->front=new_node;
        s->size=s->size+1u;
    }
    else if(priority<(s->front)->priority){
        struct s_node *p=NULL; 
        p = s->front;                         //Ojo VIOLACIONES DE SEGMENTO AL HACE Q->NEXT
        struct s_node *q=NULL; 
        q = s->last; 

        while(p->priority!=q->priority){
            if(p->priority>priority && q->priority<priority){
                //p = p->next; 
                q = q->next;
            }
            else if(p->priority>priority && q->priority>priority){
                p = p->next;
                s->last=new_node;
            }
            else if(p->priority>priority && q->priority==priority){
                q = q->next;
            }
        }
        if(p->priority>priority){
            new_node->next=q->next;
            p->next=new_node;
            s->size=s->size+1u;
        }
        else{
            new_node->next=p;
            q->next=new_node;
            s->size=s->size+1u;
        }
    }
        /*
                        s->last = new_node;
 
                
                if(q->next==NULL){
            new_node->next=NULL; 
            q->next=new_node;
            s->size=s->size+1u; 
        }           
        else if (q->next!=NULL){
            while(((q->next)->priority)>priority && q->next!=NULL){
                q=q->next;
            }
            new_node->next=q->next;
            q->next=new_node;
            s->size=s->size+1u;
        }
        */
    assert(invrep(s) && !pstack_is_empty(s));
    return s;
}

bool pstack_is_empty(pstack s) {
    /*
     * COMPLETAR
     *
     */
    return s->size==0u && s->front == NULL && s->last == NULL;
}

pstack_elem pstack_top(pstack s) {
    assert(invrep(s) && !pstack_is_empty(s));
    pstack_elem e; 
    e = s->front->elem;
    assert(invrep(s));
    return e;
}

priority_t pstack_top_priority(pstack s) {
    assert(invrep(s) && !pstack_is_empty(s));
    priority_t p; 
    p = s->front->priority;
    assert(invrep(s));
    return p;
}

unsigned int pstack_size(pstack s) {
    assert(invrep(s));
    unsigned int size=s->size;
    return size;
}

pstack pstack_pop(pstack s) {
    /*
     * COMPLETAR
     */
    assert(invrep(s) && !pstack_is_empty(s));
    struct s_node *p = NULL;
    p = (s->front);
    s->front = (s->front)->next;
    free(p);
    p = NULL;
    s->size = s->size - 1u;
    assert(invrep(s));
    return s;
}

pstack pstack_destroy(pstack s) {
    assert(invrep(s));
    /*
     * COMPLETAR
     *
     */
    struct s_node *p=NULL; 
    p = s->front;
    while (p!=NULL){
        struct s_node *killme=p;
        p = p->next;
        killme = destroy_node(killme);
    }
    free(s->last);
    s->last=NULL;           //No olvidar !!!!!
    free(s);
    s = NULL;                           
    assert(s == NULL);
    return s;
}