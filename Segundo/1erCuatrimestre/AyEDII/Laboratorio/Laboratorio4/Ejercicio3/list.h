#ifndef _LIST_H
#define _LIST_H
#include <stdbool.h>

typedef int list_elem;

typedef struct node_t * list;

//OJO DEFINICION DEL TIPO -> list_t si defino todo junto ? Separar las definiciones

list empty();

list addl(list_elem e,list l);

list destroy(list l);

//operations

bool is_empty(list l); 

list_elem head(list l);

list tail(list l);

list addr(list l, list_elem e);

int length(list l);

list concat(list l, list l1);

list_elem index(list l, int n);

list take(list l, int n);

list drop(list l, int n);

list copy_list(list l);

#endif