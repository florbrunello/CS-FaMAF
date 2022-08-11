"""
Ejercicio 1: 
Implementar una funcion llamada serie seno que reciba x y calcule los primeros 5 
terminos de la serie de Taylor del seno alrededor de cero.
"""

import math

def serie_seno(x): 
    res = 0
    for n in range (5):
        res = ((-1)**n / math.factorial(2*n+1)) * (x ** (2*n+1)) + res
    return res

"""
Instrucciones de ejecución: 

Para obtener los primeros cinco términos de la serie de taylor del seno alrededor del cero con x
como valor de entrada llamamos a la funcion serie_seno(x) donde x puede tomar cualquier valor,
en este ejemplo toma el 4 y al hacer print obtendremos el resultado buscado. 

print(serie_seno(4))
"""