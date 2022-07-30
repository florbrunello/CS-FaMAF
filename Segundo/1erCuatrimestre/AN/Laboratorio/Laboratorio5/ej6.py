"""
Ejercicio 6: 
El periodo de un pendulo de longitud l con amplitud alpha puede aproximarse con la 
formula: T = 4 √l g ∫ π/2 0 dθ (1 -sen2 alpha 2 sen2θ) 1 2, donde g = 9.8m/s2.
Programar una funcion pendulo que reciba una longitud l en metros y alpha en forma de
un numero entero entre 0 y 90, transforme el valor a radianes y devuelva el periodo del
pendulo de longitud l. ¿Que ocurre en el caso de alpha = 0?
"""

import numpy as np
from ej1a import simpson

def periodo(alpha_rad, theta):
    denominador = np.sqrt(1 - np.sin(alpha_rad / 2)**2 * np.sin(theta)**2)
    return 1 / denominador


def pendulo(longitud, alpha):
    alpha_rad = alpha * np.pi / 180
    fun_periodo = lambda theta: periodo(alpha_rad, theta)

    integral = simpson(fun_periodo, 0, np.pi / 2, 2**10)

    periodo_final = 4 * np.sqrt(longitud / 9.8) * integral

    print(f"Tenemos un periodo de {periodo_final:.2f}")
    return periodo_final