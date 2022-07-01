#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include "pstack.h"

struct s_pstack {
    unsigned int size;
    struct s_node *front;
};

struct s_node {
    pstack_elem elem;
    priority_t priority;
    struct s_node *next;
};

static struct s_node *create_node(pstack_elem e, priority_t priority) {
    struct s_node *new_node = NULL;
    new_node = malloc(sizeof(struct s_node));
    assert(new_node!=NULL);
    new_node->elem = e;
    new_node->priority = priority;
    new_node->next = NULL;
    return new_node;
}

static struct s_node *destroy_node(struct s_node *node) {
    assert(node != NULL);
    free(node);
    node = NULL;
    assert(node == NULL);
    return node;
}


static bool invrep(pstack s) {
    struct s_node *p = s->front;
    // Si la pila está vacía, se cumple la propiedad fundamental
    bool check = true;
    // Si la pila tiene al menos un elemento, debemos chequearla con un bucle
    if (p != NULL) {
        while (p->next != NULL && check) {
            if (p->priority < p->next->priority) {
                check = false;
            }
            p = p->next;
        }
    }
    return check;
}

pstack pstack_empty(void) {
    pstack s = NULL;
    s = malloc(sizeof(struct s_pstack));
    s->size = 0;
    s->front = NULL;
    assert(invrep(s) && pstack_is_empty(s));
    return s;
}

pstack pstack_push(pstack s, pstack_elem e, priority_t priority) {
    assert(invrep(s));
    struct s_node *new_node = create_node(e, priority);
    struct s_node *p = s->front;
    struct s_node *r = NULL;

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
    s->size = s->size + 1;
    assert(invrep(s) && !pstack_is_empty(s));
    return s;
}

bool pstack_is_empty(pstack s) {
    assert(invrep(s));
    bool empty = (s->size == 0 && s->front == NULL);
    assert(invrep(s));
    return empty;
}

pstack_elem pstack_top(pstack s) {
    assert(invrep(s) && !pstack_is_empty(s));
    pstack_elem top = s->front->elem;
    assert(invrep(s));
    return top;
}

priority_t pstack_top_priority(pstack s) {
    assert(invrep(s) && !pstack_is_empty(s));
    priority_t prio = s->front->priority;
    assert(invrep(s));
    return prio;
}

unsigned int pstack_size(pstack s) {
    assert(invrep(s));
    unsigned int size = 0;
    size = s->size;
    assert(invrep(s));
    return size;
}

pstack pstack_pop(pstack s) {
    assert(invrep(s) && !pstack_is_empty(s));
    struct s_node *p = s->front;
    s->front = s->front->next;
    destroy_node(p);
    s->size = s->size - 1;
    assert(invrep(s));
    return s;
}

pstack pstack_destroy(pstack s) {
    assert(invrep(s));
    struct s_node *p = s->front;
    while (s->front != NULL) {
        s->front = s->front->next;
        destroy_node(p);
        p = s->front;
    }
    free(s);
    s = NULL;
    assert(s == NULL);
    return s;
}