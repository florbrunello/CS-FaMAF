"""
Ejercicio 4: 
Calcular mediante la regla del trapecio compuesta y la regla de Simpson compuesta, las
siguientes integrales, con una tolerancia de error de 10⁽⁻⁵⁾:
a) I = ∫ 0 - 1 (x * e^(-x)) dx,
b) I = ∫ 0 - 1 (x * sen(x)) dx,
c) I = ∫ 0 - 1 ((1 + x^2)^(3/2)) dx
"""

from ej1a import intenumcomp
import numpy as np 

#Calculo la integral exacta
Ia = -(2/np.exp(1)) + np.exp(0)

def funa(x):
    return (x * np.exp(-x))
    
#Regla de Simpson

#La cantidad de subintervalos debe ser par
i = 2
Isaprox = intenumcomp(funa,0,1,i,"simpson")

#Subdivido el intervalo hasta obtener la cota del error deseada 
while(np.abs(Isaprox-Ia)>1e-5):
    i = i+2
    Isaprox = intenumcomp(funa,0,1,i,"simpson")
    errs = np.abs(Isaprox-Ia)

print(f"El valor exacto y aproximado de la integral es I = {Ia} e I = {Isaprox}, respectivamente. El error exacto de integrar con N = {i} intervalos es e={errs} y la cota del error es c={1e-5}")

#Regla del Trapecio

j = 1
Itaprox = intenumcomp(funa,0,1,j,"trapecio")

#Subdivido el intervalo hasta obtener la cota del error deseada 
while(np.abs(Itaprox-Ia)>1e-5):
    j = j+1
    Itaprox = intenumcomp(funa,0,1,j,"trapecio")
    errt = np.abs(Itaprox-Ia)

print(f"El valor exacto y aproximado de la integral es I = {Ia} e I = {Itaprox}, respectivamente. El error exacto de integrar con N = {j} intervalos es e={errt} y la cota del error es c={1e-5}")