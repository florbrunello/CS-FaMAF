/*
@file array_helpers.c
@brief Array Helpers method implementation
*/
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "array_helpers.h"

/**
* @brief returns true when reach last line in flight file
* @return True when is the last line of the file, False otherwise
*/
static bool is_last_line(unsigned int hour, unsigned int type) {
  return  hour == HOURS - 1u && type == TYPE - 1u;
}

void array_dump(DelayTable a) {
  for (unsigned int type = 0u; type < TYPE; ++type) {
    for (unsigned int hour = 0u; hour < HOURS; ++hour) {
      Flight f = a[type][hour];
      fprintf(stdout, "%c: %s flight with %u passengers arrived at %u:00, with %u delay",
        f.code,
        f.type == 0 ? "last_mile" : "layover",
        f.passengers_amount,
        f.hour - 1,
        f.delay
      );
      if (!is_last_line(hour, type))
      {
        fprintf(stdout, "\n");
      }
    }
  }
}

unsigned int compensation_cost (DelayTable a, unsigned int hour) {

  unsigned int compensation = 0u; 
  unsigned int total_cost_lm = 0u; 
  unsigned int total_cost_ly = 0u; 

  for(unsigned int j = 0u; j < hour; j++){
  
    /* Calculo la demora a pagar para los vuelos de tipo Last Mile */
    if (a[last_mile][j].delay > MAX_LM_DELAY_ALLOWED){
      total_cost_lm += (a[last_mile][j].delay - MAX_LM_DELAY_ALLOWED) * a[last_mile][j].passengers_amount * COMPENSATION_PER_MINUTE;
    }

    /* Calculo la demora a pagar para los vuelos del tipo Layover */
    if (a[layover][j].delay > MAX_LAYOVER_DELAY_ALLOWED){
      total_cost_ly += (a[layover][j].delay - MAX_LAYOVER_DELAY_ALLOWED) * a[layover][j].passengers_amount * COMPENSATION_PER_MINUTE;
    }
  }
  
  compensation = total_cost_lm + total_cost_ly;
  
  return compensation;
}


void array_from_file(DelayTable array, const char *filepath) {
  FILE *file = NULL;

  file = fopen(filepath, "r");
  if (file == NULL) {
    fprintf(stderr, "File does not exist.\n");
    exit(EXIT_FAILURE);
  }

    char code;
    int i = 0;
    while (!feof(file) && i<HOURS){
      /* COMPLETAR: lectura de cada vuelo*/
      Flight last_mile_info = flight_from_file(file);
      Flight layover_info =  flight_from_file(file);

      //OJO orden fscanf
      //OJO # y \n
      int res = fscanf(file," #%c#\n",&code);
      if (res != 1) {
        fprintf(stderr, "Invalid file.\n");
        exit(EXIT_FAILURE);
      }

      //OJO usar variables definidas 

      last_mile_info.code = code;
      last_mile_info.type = last_mile;    //0u OJO
      layover_info.code = code;
      layover_info.type = layover;        //0u OJO
      
      //OJO las horas no estan en orden
      //OJO cada linea puede tener dos horas distintas

      array[last_mile_info.type][last_mile_info.hour-1u] = last_mile_info;
      array[layover_info.type][layover_info.hour-1u] = layover_info;

      i++;
    }
    fclose(file);
}