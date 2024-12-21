/*
  @file layover.c
  @brief Implements flight structure and methods
*/
#include <stdlib.h>
#include "flight.h"

static const int AMOUNT_OF_FLIGHT_VARS = 2;

Flight flight_from_file(FILE* file, char code, item_t type)
{
    Flight flight;
    flight.code = code;
    flight.type = type;

    int res = 0u; 
    res = fscanf(file,EXPECTED_FLIGHT_FILE_FORMAT,&flight.hour,&flight.items_amount);

    /* Chequeo que a ninguna entrega le sobre ni falte información */
    if(res!=AMOUNT_OF_FLIGHT_VARS){
        fprintf(stderr, "Invalid file.\n");
        exit(EXIT_FAILURE);
    }

    /* Chequeo que ninguna entrega tenga una hora no permitida */
    if (flight.hour > 24) {                 //HOURS
      fprintf(stderr, "Invalid flight.\n");
      exit(EXIT_FAILURE);
    }
    /* COMPLETAR */

    return flight;
}



