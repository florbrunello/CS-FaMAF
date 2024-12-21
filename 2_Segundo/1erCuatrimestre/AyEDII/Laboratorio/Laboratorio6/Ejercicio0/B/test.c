#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/* Then, this project's includes, alphabetically ordered */
#include "queue.h"
#include "queue_helpers.h"

int main() {
    queue q; 
    unsigned int size =0u; 
    q = queue_empty(); 
    size = queue_size(q);
    printf("%u\n",size);
    q = queue_enqueue(q,3);
    size = queue_size(q);
    printf("%u\n",size);
    q = queue_enqueue(q,4);
    //q = queue_enqueue(q,5);
    size = queue_size(q);
    printf("%u\n",size);
    return 0;
}