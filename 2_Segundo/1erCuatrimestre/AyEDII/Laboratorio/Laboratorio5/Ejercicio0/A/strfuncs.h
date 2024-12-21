#ifndef _STRFUNCS_H
#define _STRFUNCS_H
#include <stdlib.h>

size_t string_length(const char *str);

char *string_filter(const char *str, char c);

#endif

//OJO: incluir #include <stdlib.h> para size_t