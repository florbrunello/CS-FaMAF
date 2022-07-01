#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include "pair.h"

struct s_pair_t {
    int fst;
    int snd;
};

static bool invrep(pair_t p){
    return (p!=NULL); 
}

pair_t pair_new(int x, int y){
    pair_t new_pair; 
    new_pair = malloc(sizeof(struct s_pair_t));
    new_pair->fst = x; 
    new_pair->snd = y; 
    assert(new_pair!=NULL);
    //assert(invrep(new_pair));
    return new_pair; 
}

int pair_first(pair_t p){
    // assert(invrep(p));;
    assert(p != NULL);
    return p->fst; 
}

int pair_second(pair_t p){
    assert(p != NULL);
    return p->snd;
}

pair_t pair_swapped(pair_t p){
    
    // pair_t res; 
    // assert(invrep(p));
    // ... 
    // assert(invrep(res));

    assert(p != NULL);
    return pair_new(p->snd,p->fst);
}

pair_t pair_destroy(pair_t p){
    //se chequea antes (no al final)
    free(p);
    p = NULL; 
    return p;
}