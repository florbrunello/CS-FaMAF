/*
  @file wagon.h
  @brief Defines a train wagon cargo
*/

#ifndef _WAGON_H
#define _WAGON_H
#define EXPECTED_WAGON_LINE_FORMAT " %u %c %u "

typedef enum { rice, mushrooms, oatmeal, pepper } cargo_t;

#include <stdio.h>

/** @brief Type used to represent wagon cargo data.*/
typedef struct _wagon
{
  unsigned int number;
  cargo_t cargo;
  unsigned int weight;
} Wagon;

/**
 * @brief reads cargo data from file line
 * @details
 * Cargo file line must contain:
 * <unsigned int> <char*> <unsigned int>
 *
 * @param[in] file Opened file stream
 * @return Wagon structure which contain read information from file
 */
Wagon wagon_from_file(FILE* file);

#endif //_WAGON_H
