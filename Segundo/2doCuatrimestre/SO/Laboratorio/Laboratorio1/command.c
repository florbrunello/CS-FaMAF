#include <assert.h>
#include <glib-2.0/glib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "command.h"
#include "strextra.h" /* Para strmerge() */

/* Estructura de un comando simple: ([char*],char*,char*) */

struct scommand_s {
    GSList* commands; 
    char* rdir_in;
    char* rdir_out;
}; 

/* Estructura de un comando pipeline: ([scommand],bool) */ 

struct pipeline_s{
    GSList* list_scommand;
    bool wait;  
};

scommand scommand_new(void){  
    scommand result = malloc(sizeof(struct scommand_s));
    if(result==NULL){ //Caso en que malloc falle
        printf("Error: malloc");
        exit(EXIT_FAILURE);
    }
    result->commands = NULL;
    result->rdir_in = NULL; 
    result->rdir_out = NULL; 

    assert(result != NULL && scommand_is_empty(result) 
    && scommand_get_redir_in(result) == NULL
    && scommand_get_redir_out(result) == NULL);
    
    return result; 
}

scommand scommand_destroy(scommand self){
    assert(self!=NULL);

    g_slist_free_full(self->commands,free);
    self->commands = NULL;
    free(self->rdir_in);
    self->rdir_in = NULL;
    free(self->rdir_out);
    self->rdir_out = NULL;

    free(self);
    self = NULL;

    assert(self == NULL);
    
    return self;
}

void scommand_push_back(scommand self, char * argument) {
    assert(self!=NULL && argument!=NULL);
    
    self->commands = g_slist_append(self->commands, argument);
    
    assert(!scommand_is_empty(self));
}

void scommand_pop_front(scommand self){
    assert(self!=NULL && !scommand_is_empty(self));

    gpointer * tmp;
    tmp = g_slist_nth_data(self->commands,0);
    self->commands = g_slist_remove(self->commands, tmp);
    free(tmp);
}

void scommand_set_redir_in(scommand self, char * filename){
    assert(self!=NULL);
    
    if(self->rdir_in != NULL) free(self->rdir_in);
    self->rdir_in = filename;
}

void scommand_set_redir_out(scommand self, char * filename){
    assert(self != NULL);
    
    if(self->rdir_out != NULL) free(self->rdir_out);
    self->rdir_out = filename;
}

bool scommand_is_empty(const scommand self) {
    assert(self!=NULL);
    
    return (self->commands == NULL);
}

unsigned int scommand_length(const scommand self){
    assert(self!=NULL);

    unsigned int length;
    length = (unsigned int) g_slist_length(self->commands);

    assert((length==0) == scommand_is_empty(self));
    
    return length;
}

char * scommand_front(const scommand self){
    assert(self!=NULL && !scommand_is_empty(self)); 
    
    char * cmd = g_slist_nth_data(self->commands,0u);

    assert(cmd!=NULL); 
    
    return cmd; 
}

char* scommand_get_redir_in(const scommand self){
    assert(self!=NULL);
    
    return (self->rdir_in);
}

char* scommand_get_redir_out(const scommand self) {
    assert(self!=NULL);
    
    return self->rdir_out;
}

//Libera el espacio del primer argumento de strmerge
static char * strmerge2(char * str1, char * str2){
    char * result = strmerge(str1,str2);
    free(str1);
    return result;
}

char * scommand_to_string(const scommand self){
    assert(self!=NULL);

    char *result = NULL;
    if (self->commands != NULL){
        result = strdup((char *)g_slist_nth_data(self->commands,0));
    } else {
        result = strdup("");
    }
    char *data = NULL;
    for (unsigned int i = 1; i < (unsigned int) g_slist_length(self->commands); i++)
    {
        data = g_slist_nth_data(self->commands,i);
        result = strmerge2(result, " ");
        result = strmerge2(result, data);
    }
    if (self->commands != NULL && self->rdir_out != NULL){
        data = self->rdir_out;
        result = strmerge2(result, " > ");
        result = strmerge2(result, data);
    }
     if (self->commands != NULL && self->rdir_in != NULL){
        data = self->rdir_in;
        result = strmerge2(result, " < ");
        result = strmerge2(result, data);
    }
    
    data = NULL;
    assert(scommand_is_empty(self) ||
    scommand_get_redir_in(self)==NULL || scommand_get_redir_out(self)==NULL ||
    strlen(result)>0);
    return result;
}

pipeline pipeline_new(void){
    pipeline result = malloc(sizeof(struct pipeline_s));
    if(result == NULL){ //Caso en que malloc falle
        printf("Error: malloc");
        exit(EXIT_FAILURE);
    }
    result->list_scommand = NULL; 
    result->wait = true; 

    assert(result != NULL && pipeline_is_empty(result) && pipeline_get_wait(result)); 
    
    return result; 
}

//Libera cada scommand
static void ret_void_scommand_destroy(void* self) {
    scommand self_aux = self;
    scommand_destroy(self_aux);
}

pipeline pipeline_destroy(pipeline self){
    assert(self!=NULL);

    g_slist_free_full(self->list_scommand,ret_void_scommand_destroy);
    self->list_scommand = NULL;
    free(self);
    self = NULL;

    assert(self == NULL);
    return self;
}

void pipeline_push_back(pipeline self, scommand sc) {
    assert(self!=NULL && sc!=NULL);
    
    self->list_scommand = g_slist_append(self->list_scommand, sc);
    
    assert(!pipeline_is_empty(self));
} 

void pipeline_pop_front(pipeline self){
    assert(self!=NULL && !pipeline_is_empty(self));
    
    gpointer * tmp;
    tmp = g_slist_nth_data(self->list_scommand, 0u);
    self->list_scommand = g_slist_remove(self->list_scommand, tmp);
    free(tmp);
}

void pipeline_set_wait(pipeline self, const bool w){
    assert(self!=NULL); 
    
    self->wait = w; 
}

bool pipeline_is_empty(const pipeline self){
    assert(self!=NULL);
    
    return self->list_scommand == NULL;   
}

unsigned int pipeline_length(const pipeline self) {
    assert(self!=NULL);
    
    return g_slist_length(self->list_scommand);
} 

scommand pipeline_front(const pipeline self){
    assert(self!=NULL && !pipeline_is_empty(self)); 
    
    scommand result = g_slist_nth_data(self->list_scommand,0u);

    assert(result!=NULL);

    return result;
}

bool pipeline_get_wait(const pipeline self){
    assert(self!=NULL);

    return self->wait; 
}

char* pipeline_to_string(const pipeline self){
    assert(self != NULL);

    char* res = NULL;
    if (self->list_scommand!=NULL){
        res = scommand_to_string(g_slist_nth_data(self->list_scommand,0));

        char *str = NULL;
        for (unsigned int i = 1u; i < g_slist_length(self->list_scommand); i++) {
            str = scommand_to_string(g_slist_nth_data(self->list_scommand,i));
            res = strmerge2(res," | ");
            res = strmerge2(res, str);
            free(str);
        }

        if(!pipeline_get_wait(self)){
            res = strmerge2(res," &");
        }
        
        str = NULL;
    } 
    else {
        res = strdup("");
    }

    assert(pipeline_is_empty(self) || pipeline_get_wait(self) || strlen(res)>0);
    
    return res;
}
