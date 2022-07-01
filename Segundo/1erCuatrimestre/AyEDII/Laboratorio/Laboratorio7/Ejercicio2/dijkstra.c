#include <assert.h>
#include <stdlib.h>

#include "cost.h"
#include "graph.h"
#include "mini_set.h"

unsigned int minimo(graph_t g, set C, cost_t * D){
    unsigned int res; 
    int min = __INT_MAX__; 
    for (unsigned int j=0u; j < graph_max_vertexs(g); j++){
            if (D[j] <= min && set_member(j,C)){
                min = D[j];
                res = j;
            }
    }
    return res; 
}

cost_t *dijkstra(graph_t graph, vertex_t init) {
    cost_t *D = calloc(graph_max_vertexs(graph),sizeof(cost_t));
    unsigned int c; 
    set C = set_empty();
    
    for (unsigned int i=0u; i < graph_max_vertexs(graph); i++){
        C = set_add(C,i);
    }
    C = set_elim(C,init);

    for (unsigned int j=0u; j < graph_max_vertexs(graph); j++){
        D[j] = graph_get_cost(graph,init,j);
    }
    
    while(!set_is_empty(C)){
        c = minimo(graph,C,D);
        C = set_elim(C,c);

        for (unsigned int i=0u; i < graph_max_vertexs(graph); i++){
            if((D[i] > (cost_sum(D[c],graph_get_cost(graph,c,i)))) && set_member(i,C)){
                D[i] = cost_sum(D[c],graph_get_cost(graph,c,i));
            }
        }        
    }

    C = set_destroy(C);

    return D; 
}
