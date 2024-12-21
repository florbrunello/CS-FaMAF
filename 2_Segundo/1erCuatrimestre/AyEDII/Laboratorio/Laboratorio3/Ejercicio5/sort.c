/*
  @file sort.c
  @brief sort functions implementation
*/

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include "helpers.h"
#include "sort.h"
#include "player.h"

bool goes_before(player_t x, player_t y){
    // completar aquí
    bool res = true; 
    if (((*x).rank) > ((*y).rank)){
        res = false;
    }
    return res;    
    
    return true;
}

bool array_is_sorted(player_t atp[], unsigned int length) {
    unsigned int i = 1u;
    while (i < length && goes_before(atp[i - 1u], atp[i])) {
        i++;
    }
    return (i == length);
}

void swap(player_t a[], unsigned int i, unsigned int j){
    player_t aux = a[i];
    a[i] = a[j]; 
    a[j] = aux; 
}
/* Exchanges elements of array 'a' in the given positions 'i' and 'j'
   Array remains the same if the two positions are the same
*/

static void insert(player_t a[], unsigned int length) {
    // completar aquí
    unsigned int j = length; 
    while (j>0u && goes_before(a[j],a[j-1u]))
    {
        swap(a,j-1u,j);
        j = j-1u;
    }
}

void sort(player_t a[], unsigned int length) {
    for (unsigned int i = 1u; i < length; ++i) 
    {
        insert(a, i);
        assert(array_is_sorted(a,i));
    }
}