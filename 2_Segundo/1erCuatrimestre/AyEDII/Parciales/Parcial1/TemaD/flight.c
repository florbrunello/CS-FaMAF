/*
  @file layover.c
  @brief Implements flight structure and methods
*/
#include <stdlib.h>
#include "flight.h"

static const int AMOUNT_OF_FLIGHT_VARS = 3;

Flight flight_from_file(FILE* file){
    Flight flight;
    int res = 0u;
    res = fscanf(file,EXPECTED_FLIGHT_FILE_FORMAT,&flight.hour,&flight.delay,&flight.passengers_amount);
    
    /* Chequeo que a ningún vuelo le sobre ni falte información */
    if(res!=AMOUNT_OF_FLIGHT_VARS){
        fprintf(stderr, "Invalid file.\n");
        exit(EXIT_FAILURE);
    }

    /* Chequeo que ningún vuelo tenga una hora no permitida */
    if (flight.hour > 24) {                //NO uso HOURS, tendría que incluir una libreria sino
      fprintf(stderr, "Invalid flight.\n");
      exit(EXIT_FAILURE);
    }

    return flight;
}