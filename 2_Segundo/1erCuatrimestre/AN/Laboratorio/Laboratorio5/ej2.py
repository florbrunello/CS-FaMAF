"""
Ejercicio 2: 
Ejecutar los comandos necesarios para mostrar en pantalla los errores absolutos de 
integrar numericamente ∫ 0 1 e^(-x) dx, usando 4, 10 y 20 subintervalos con las 3 
reglas compuestas del ejercicio 1.
"""

from ej1a import intenumcomp
import numpy as np 

#Valor exacto de la integral
integral = - np.exp(-1) + np.exp(0)

print(f"El valor exacto de la integral es I = {integral}")

def fun(x): 
    return (np.exp(-x))

subint = [4,10,20]

for i in subint:
    s = intenumcomp(fun,0,1,i,"simpson")
    t = intenumcomp(fun,0,1,i,"trapecio")
    pm = intenumcomp(fun,0,1,i,"puntomedio")
    errs = np.abs(s - integral)
    errt = np.abs(t - integral)
    errpm = np.abs(pm - integral)
    print(f"Usando {i} subintervalos, los errores absolutos de calcular la integral son: R. Simpson = {errs}, R. Trapecio = {errt} y R. Punto Medio = {errpm}")