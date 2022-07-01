/*
Respuesta: 

El problema de esta implementacion es que el arreglo esta defindo en memoria estática y al 
llamarlo fuera de la funcion no accedo al arreglo creado originalmente. Esto ocurre porque 
unicamente existe dentro de la función donde lo declaré. 

test_bad


==8514== Memcheck, a memory error detector
==8514== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==8514== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==8514== Command: ./bad_graph input/example_graph_1.in
==8514== 
==8514== Invalid write of size 4
==8514==    at 0x109677: graph_add_edge (graph_bad.c:57)
==8514==    by 0x1099F4: graph_from_file (graph_bad.c:122)
==8514==    by 0x109AA3: main (main.c:12)
==8514==  Address 0x1ffefffb70 is on thread 1's stack
==8514==  208 bytes below stack pointer
==8514== 
6
==8514== Invalid read of size 4
==8514==    at 0x109755: graph_get_cost (graph_bad.c:71)
==8514==    by 0x109844: graph_print (graph_bad.c:93)
==8514==    by 0x109AB3: main (main.c:13)
==8514==  Address 0x1ffefffb70 is on thread 1's stack
==8514==  512 bytes below stack pointer
==8514== 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 0 
==8514== 
==8514== HEAP SUMMARY:
==8514==     in use at exit: 0 bytes in 0 blocks
==8514==   total heap usage: 4 allocs, 4 frees, 5,608 bytes allocated
==8514== 
==8514== All heap blocks were freed -- no leaks are possible
==8514== 
==8514== For lists of detected and suppressed errors, rerun with: -s
==8514== 
==8514== HEAP SUMMARY:
==8514==     in use at exit: 0 bytes in 0 blocks
==8514==   total heap usage: 4 allocs, 4 frees, 5,608 bytes allocated
==8514== 
==8514== All heap blocks were freed -- no leaks are possible
==8514== 
==8514== For lists of detected and suppressed errors, rerun with: -s
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "graph.h"

struct graph_data {
    cost_t *costs;
    unsigned int max_vertexs;
};

static unsigned int g_index(vertex_t i, vertex_t j, unsigned int max_vertexs) {
    return i + j * max_vertexs;
}

static bool invrep(graph_t g) {
    /*
     * TODO: Completar
     *
     */
    return g!=NULL;
}

graph_t graph_empty(unsigned int max_vertexs)
{
    graph_t graph = calloc(1, sizeof(struct graph_data));
    assert(graph != NULL);
    graph->max_vertexs = max_vertexs;
    // Create adjacency matrix for graph
    cost_t costs_array[max_vertexs * max_vertexs];

    for (unsigned int i = 0; i < max_vertexs * max_vertexs; ++i) {
      costs_array[i] = cost_inf();
    }
    // Save matrix in the structure
    graph->costs = costs_array;
    assert(invrep(graph) && graph->costs != NULL);
    return graph;
}

unsigned int graph_max_vertexs(graph_t graph)
{
    assert(graph != NULL);
    return graph->max_vertexs;
}

void graph_add_edge(graph_t graph, vertex_t from, vertex_t to, cost_t cost)
{
    assert(graph != NULL);
    assert(from < graph->max_vertexs);
    assert(to < graph->max_vertexs);
    unsigned int index=0u;
    /*
     * TODO: Completar
     *
     */
    graph->costs[index] = cost;
    assert(invrep(graph));
}

cost_t graph_get_cost(graph_t graph, vertex_t from, vertex_t to)
{
    assert(graph != NULL);
    assert(from < graph->max_vertexs);
    assert(to < graph->max_vertexs);
    unsigned int index=0u;
    /*
     * TODO: Completar
     *
     */
    return graph->costs[index];
}

graph_t graph_destroy(graph_t graph)
{
    assert(graph != NULL);
    /*
     * TODO: COMPLETAR
     *
     */
    free(graph);
    graph = NULL;
    assert(graph == NULL);
    return graph;
}

void graph_print(graph_t graph)
{
    assert(graph != NULL);
    printf("%u\n", graph->max_vertexs);
    for (unsigned int i = 0; i < graph->max_vertexs; ++i) {
        for (unsigned int j = 0; j < graph->max_vertexs; ++j) {
            const cost_t cost = graph_get_cost(graph, i, j);
            if (cost_is_inf(cost)) {
                printf("# ");
            } else {
                printf("%d ", cost);
            }
        }
        printf("\n");
    }
}

graph_t graph_from_file(const char *file_path)
{
    FILE *file = fopen(file_path, "r");
    if (file == NULL) {
        fprintf(stderr, "File does not exist.\n");
        exit(EXIT_FAILURE);
    }
    unsigned int tam = 0;
    fscanf(file, "%u", &tam);
    char word[256];
    const graph_t graph = graph_empty(tam);
    for (unsigned int i = 0; i < tam; ++i) {
        for (unsigned int j = 0; j < tam; ++j) {
            cost_t cost = cost_inf();
            fscanf(file, "%s", word);
            if (word[0] != '#') {
                cost = atoi(word);
            }
            graph_add_edge(graph, i, j, cost);
        }
    }
    fclose(file);
    return graph;
}
