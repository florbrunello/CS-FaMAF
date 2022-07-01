/*
  @file array_helpers.h
  @brief defines array helpers methods. These methods operates over multidimensional array of layover
*/
#ifndef _ARRAY_HELPERS_H
#define _ARRAY_HELPERS_H

#include <stdbool.h>
#include "wagon.h"

#define MAX_SIZE 100

typedef Wagon Train [MAX_SIZE];

/**
 * @brief Write the content of the array 'a' into stdout.
 * @param[in] a array to dump in stdout
 */
void array_dump(Train t, unsigned int size);

/**
 * @brief calculates how many wagons should be discarded.
 * @param[in] a array
 */
unsigned int discarded_wagons(Train t, unsigned int trainSize);


/**
 * @brief reads an array of train information from file
 * @details
 *
 *  Each element is read from the file located at 'filepath'.
 *  The file must exist in disk and must have its contents in a sequence of
 *  lines, first line will be:
 *
 *   <train code> <number of wagons> <total kg>
 *
 *   and then each following line will have the following format:
 *
 *   <wagon number> <cargo type> <kg>
 *
 *   Those elements are copied into the array 'a'.
 *   The dimensions of the array are given by the macros noted above.
 *
 * @param a array which will contain read file
 * @param filepath file with train data
 */
void array_from_file(Train t, unsigned int * trainSize, const char *filepath);

#endif
