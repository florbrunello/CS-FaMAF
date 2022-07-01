/*
@file array_helpers.c
@brief Array Helpers method implementation
*/
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "array_helpers.h"
#include "wagon.h"

char * cargo_type_to_str(cargo_t cargo) {
  if (cargo == rice)
    return "rice";
  if (cargo == mushrooms)
    return "mushrooms";
  if (cargo == oatmeal)
    return "oatmeal";
  if (cargo == pepper)
    return "pepper";
  return "error";
}

void array_dump(Train t, unsigned int size) {
  for (unsigned int i = 0u; i < size; ++i) {
    Wagon w = t[i];
    fprintf(stdout, "wagon %u: %u kg of %s", w.number, w.weight, cargo_type_to_str(w.cargo));
    if (i != size-1) {
      fprintf(stdout, "\n");
    }
  }
}

unsigned int discarded_wagons (Train t, unsigned int size){

  unsigned int discart_wagons = 0u; 
  unsigned int i = 0u; 
  unsigned int j = 0u; 

  while(i<size-1u){
    /*Chequeo si tengo dos vagones seguidos de oatmeal*/
    if(t[i].cargo == oatmeal && t[i+1].cargo == oatmeal){
      j = i+2u; 
      
      /*Sumo los vagones de oatmeal que existen luego de los dos hallados anteriormente*/
      while(j<size && t[j].cargo == oatmeal){
        discart_wagons += 1u; 
        j++;
      }
      i = j; 
    }

    /*Caso contrario itero en el arreglo*/
    else{
      i++;
    }
  }

  return discart_wagons;
}

// the wagon data should be saved on array
// the number of wagons should be stored on trainSize
void array_from_file(Train array, unsigned int * trainSize, const char *filepath) {
  FILE *file = NULL;

  file = fopen(filepath, "r");
  if (file == NULL) {
    fprintf(stderr, "File does not exist.\n");
    exit(EXIT_FAILURE);
  }

  char code;
  unsigned int size = 0;
  unsigned int totalKg = 0;

  int res = fscanf(file," <%c> %u %u ",&code, &size, &totalKg);
  if (res != 3) {
    fprintf(stderr, "Invalid file.\n");
    exit(EXIT_FAILURE);
  }

  /*Chequeo que el número de vagones esté permitido*/ 
  if (size>MAX_SIZE) {
    fprintf(stderr, "Invalid file.\n");
    exit(EXIT_FAILURE);
  }

  *trainSize = size;

  unsigned int i = 0u;
  while (i<size && !feof(file)) {
    Wagon wagon = wagon_from_file(file);
    
    /* Chequeo que ningún vagon tenga un numero no permitido*/ 
    if(wagon.number>size){
      fprintf(stderr, "Invalid file.\n");
      exit(EXIT_FAILURE);
    }       

    array[wagon.number-1u] = wagon;

    i++;
  }
  
  /*Chequeo que no hayan datos de menos*/
  if(i!=size){
    fprintf(stderr, "Invalid file.\n");
    exit(EXIT_FAILURE); 
  }

  fclose(file);
}
