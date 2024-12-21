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
    new_node->next = NULL;                                                    //NO OLVIDAR !!!!!!!!!!
    return new_node;
}

static struct s_node * destroy_node(struct s_node *node) {
    assert(node != NULL);
    //node->next=NULL; NO ES NECESARIO
    free(node);
    node=NULL;
    /*
     * COMPLETAR
     *
     */
    assert(node == NULL);
    return node;
}

//REVISARRRRRRRRRRRR
static bool invrep(pstack s) {
    bool res=true;
    struct s_node *p=NULL; 
    p = s->front; 
    while(p!=NULL){                    
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
    assert(invrep(s) && pstack_is_empty(s));
    return s;
}

// SEPARAR CASOS -> S == NULL O S != NULL 
// LUEGO SEPARAR EN MÁS CASOS
// NO USAR UN PUNTERO AL ULTIMO ELEMENTO 
// p->next != NULL PARA EVITAR VIOLACION DE SEGMENTO

pstack pstack_push(pstack s, pstack_elem e, priority_t priority) {
    assert(invrep(s));
    struct s_node *new_node = create_node(e, priority);
    struct s_node *p = s->front, *r = NULL;
    // Si el stack está vacío, asigno el elemento a s->front
    if (pstack_is_empty(s)) {
        s->front = new_node;
    } else {
    // Si tiene al menos un elemento, debo recorrerla para ubicarlo en la posición correcta
        if (s->front->priority <= priority) {
            r = s->front;
            s->front = new_node;
            new_node->next = r;
        } else {
            while (p->next != NULL && p->next->priority > priority) {
                p = p->next;
            }
            r = p->next;
            p->next = new_node;
            new_node->next = r;
        }
    }
    s->size = s->size + 1u;
    assert(invrep(s) && !pstack_is_empty(s));
    return s;
}

//NO OLVIDAR DE CHEQUEAR ASSERTS !!!!!!!!!
bool pstack_is_empty(pstack s) {
    assert(invrep(s));
    bool empty = (s->size == 0 && s->front == NULL);
    assert(invrep(s));
    return empty;
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

//NO OLVIDAR DE CHEQUEAR ASSERTS !!!!!!!!!
unsigned int pstack_size(pstack s) {
    assert(invrep(s));
    unsigned int size = 0u;
    size = s->size;
    assert(invrep(s));
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
    p = NULL;                           //destroy_node(p); MEJOR QUE LAS LINEAS 167 Y 168 
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
    free(s);
    s = NULL;                           
    assert(s == NULL);
    return s;
}