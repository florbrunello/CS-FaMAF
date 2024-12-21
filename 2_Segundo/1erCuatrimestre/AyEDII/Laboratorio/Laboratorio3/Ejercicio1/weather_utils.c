/* First, the standard lib includes, alphabetically ordered */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

/* Then, this project's includes, alphabetically ordered */
#include "array_helpers.h"

int min_temp_hist(WeatherTable array){
    int min = array[0][0][0]._min_temp;
    for(unsigned int year = 0u; year < YEARS; year++){
        for(month_t month = january; month < MONTHS; month++){
            for(unsigned int day = 0u; day < DAYS; day++){
                if(array[year][month][day]._min_temp < min){         //OJO COMO USO ARRAY
                    min = array[year][month][day]._min_temp;
                }
            }
        }
    }
    return min; 
}

void max_temp_year(WeatherTable a, int output[YEARS]) {

    for(unsigned int year = 0u; year<YEARS;year++){
        int max_temp_year = a[year][january][0]._max_temp;      //ojo inicializacion desde 0
        for(month_t month = january; month < MONTHS; month++){
            for(unsigned int day = 0u; day < DAYS; day++){
                if(a[year][month][day]._max_temp > max_temp_year){
                    max_temp_year = a[year][month][day]._max_temp;
                }
            }
        }
        output[year] = max_temp_year;
    }
}

void max_temp_month_year(WeatherTable a, month_t output[YEARS]) {
    for (unsigned int year = 0; year < YEARS; a++) {
        month_t month_max = january;
        unsigned int prec_max = 0;
        for (month_t m = january; m <= december; m++) {
            unsigned int prec_month = 0;
            for (unsigned int d = 0; d < DAYS; d++) {
                prec_month += a[year][m][d]._rainfall;
            }
            if (prec_month > prec_max) {
                prec_max = prec_month;
                month_max = m;
            }
        }
        output[year] = month_max;
    }
}