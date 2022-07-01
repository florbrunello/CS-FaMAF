#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include "pqueue.h"

struct s_pqueue {
    unsigned int size;
    struct s_node *front;
};

struct s_node {
    pqueue_elem elem;
    unsigned int priority;
    struct s_node *next;
};

static struct s_node * create_node(pqueue_elem e, unsigned int priority) {
    struct s_node *new_node = NULL;
    new_node = malloc(sizeof(struct s_node));
    assert(new_node!=NULL);
    new_node->elem = e;
    new_node->priority = priority;
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
    struct s_node *p = q->front;
    // Si la cola está vacía o tiene un único elemento, se cumple la propiedad fundamental
    bool check = true;
    // Si la cola tiene al menos un elementos, tengo que chequearla con un bucle
    if (p != NULL) {
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
    pqueue q = NULL;
    q = malloc(sizeof(struct s_pqueue));
    q->front = NULL;
    q->size = 0u;
    assert(invrep(q) && pqueue_is_empty(q));
    return q;
}

pqueue pqueue_enqueue(pqueue q, pqueue_elem e, unsigned int priority) {
    assert(invrep(q));
    struct s_node *p = q->front;
    struct s_node *new_node = create_node(e, priority);
    struct s_node *r = NULL;
    // Si la cola está vacía, agrego el nodo a q->front
    if (pqueue_is_empty(q)) {
        q->front = new_node;
    } else {
    // Si tiene al menos un elementos, debo recorrer la cola para ubicar el elemento en el lugar correcto
        if (q->front->priority > priority) {
            r = q->front;
            q->front = new_node;
            new_node->next = r;
        } else {
            while (p->next != NULL && p->next->priority <= priority) {
                p = p->next;
            }
            r = p->next;
            p->next = new_node;
            new_node->next = r;
        }
    }
    q->size = q->size + 1;
    assert(invrep(q) && !pqueue_is_empty(q));
    return q;
}

bool pqueue_is_empty(pqueue q) {
    assert(invrep(q));
    bool empty = (q->size == 0 && q->front == NULL);
    assert(invrep(q));
    return empty;
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
    unsigned int size = q->size;
    assert(invrep(q));
    return size;
}

pqueue pqueue_dequeue(pqueue q) {
    assert(invrep(q) && !pqueue_is_empty(q));
    struct s_node *p = q->front;
    q->front = q->front->next;
    q->size = q->size - 1;
    p = destroy_node(p);
    assert(invrep(q));
    return q;
}

pqueue pqueue_destroy(pqueue q) {
    assert(invrep(q));
    struct s_node *p = q->front;
    while (q->front != NULL) {
        q->front = q->front->next;
        destroy_node(p);
        p = q->front;
    }
    free(q);
    q = NULL;
    assert(q == NULL);
    return q;
}