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
* @brief returns true when reach last entry in flight table
* @return True when is the last entry of the flight table, False otherwise
*/
static bool is_last_line(unsigned int hour, unsigned int type) {
  return  hour == HOURS - 1u && type == TYPE - 1u;
}

void array_dump(LayoverTable a) {
  for (unsigned int hour = 0u; hour < HOURS; ++hour) {
    for (unsigned int type = 0u; type < TYPE; ++type) {
      Flight f = a[hour][type];
      fprintf(stdout, "%c: %s at %u:00 with %u passengers", f.code, f.type == 0 ? "arrives" : "departs", f.hour - 1, f.passengers_amount);
      if (!is_last_line(hour, type))
      {
        fprintf(stdout, "\n");
      }
    }
  }
}


unsigned int passengers_amount_in_airport (LayoverTable a, unsigned int h) {
  unsigned int arrivals_amount=0u;
  unsigned int departures_amount=0u;
  unsigned int passengers_waiting=0u;

  //Sumo el total de pasajeros que llegaron y partieron a lo largo de día hasta las h-1 hs
  for(unsigned int i=0u; i<h;i++){       //h-1
    arrivals_amount += a[i][arrival].passengers_amount;
    departures_amount += a[i][departure].passengers_amount;
  }

  //Calculo la diferencia entre todos los que llegaron y se fueron para obtener los que aún esperan
  if (arrivals_amount > departures_amount){
    passengers_waiting = arrivals_amount - departures_amount;
  }

  //Sumo los que esperan en la ultima hora
  passengers_waiting += a[h][arrival].passengers_amount;    //h-1
  
  return passengers_waiting;
}

/*
unsigned int passengers_amount_in_airport (LayoverTable a, unsigned int h) {
  unsigned int passengers_waiting = 0;
  
  //Sumo los pasajeros que arrivaron y quito los que se fueron
  for(unsigned int i = 0u; i < h; i++){
    passengers_waiting += a[i][arrival].passengers_amount;
    passengers_waiting -= a[i][departure].passengers_amount;
  }
  
  //Sumo los que esperan en la ultima hora
  passengers_waiting += a[h][arrival].passengers_amount;

  return passengers_waiting;
}
*/
void array_from_file(LayoverTable array, const char *filepath) {
  FILE *file = NULL;

  file = fopen(filepath, "r");
  if (file == NULL) {
    fprintf(stderr, "File does not exist.\n");
    exit(EXIT_FAILURE);
  }

  char code;
  int i=0;
  while (!feof(file) && i<HOURS){/*lectura completa de todos los datos */
    int res = fscanf(file,"\n_%c_ ",&code);/*lectura de codigo de vuelo */
    if (res != 1) {
      fprintf(stderr, "Invalid file.\n");
      exit(EXIT_FAILURE);
    }

    /* COMPLETAR: Generar y guardar ambos Flight en el array multidimensional */
    Flight flight_arrival = flight_from_file(file,code);
    Flight flight_departure = flight_from_file(file,code);

    array[flight_arrival.hour-1u][flight_arrival.type] = flight_arrival;
    array[flight_departure.hour-1u][flight_departure.type] = flight_departure;

    i++;
  }
  fclose(file);
}