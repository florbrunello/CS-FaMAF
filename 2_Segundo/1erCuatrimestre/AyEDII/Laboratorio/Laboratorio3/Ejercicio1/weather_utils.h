#ifndef _WEATHER_UTILS_H
#define _WEATHER_UTILS_H

/* First, the standard lib includes, alphabetically ordered */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "array_helpers.h"

int min_temp_hist(WeatherTable array);
void max_temp_year(WeatherTable arr, int output[YEARS]);
void max_temp_month_year(WeatherTable arr, month_t output[YEARS]);

#endif
