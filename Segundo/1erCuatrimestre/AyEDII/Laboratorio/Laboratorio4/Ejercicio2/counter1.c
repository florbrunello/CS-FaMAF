#include <stdbool.h>
#include <stdlib.h>
#include <assert.h>

#include "counter.h"

struct _counter {
    unsigned int count;
};

counter counter_init(void) {
    counter c = NULL; 
    c = malloc(sizeof(struct _counter));
    c->count = 0u;

    assert(counter_is_init(c));
    return c;
}

void counter_inc(counter c) {
    c->count = c->count + 1u; 
}

bool counter_is_init(counter c) {
    bool res=true; 
    res = c->count == 0u; 
    return res; 
}

void counter_dec(counter c) {
    assert(!counter_is_init(c));
    c->count = c->count -1u; 
}

counter counter_copy(counter c) {
    counter d = NULL; 
    d = malloc(sizeof(struct _counter));
    d->count = c->count;    //OJOOO 
    return d; 
}

void counter_destroy(counter c) {
    free(c);
    c = NULL; 
}
