/*
  @file layover.c
  @brief Implements flight structure and methods
*/
#include <stdlib.h>
#include "flight.h"

static const int AMOUNT_OF_FLIGHT_VARS = 2;

Flight flight_from_file(FILE* file, char code, unsigned int arrival_hour)
{
    Flight flight;
    flight.code = code;
    flight.hour = arrival_hour;

    /*Leo y guardo los datos del tipo de entrega y la cantidad de items*/
    int res = 0u; 
    res = fscanf(file,EXPECTED_FLIGHT_FILE_FORMAT, &flight.type, &flight.items_amount);
    
    /* Chequeo la cantidad de datos recibida (no debe sobre ni faltar información)*/
    if(res!=AMOUNT_OF_FLIGHT_VARS){
        fprintf(stderr, "Invalid file.\n");
        exit(EXIT_FAILURE);
    }
    /* COMPLETAR */

    return flight;
}
