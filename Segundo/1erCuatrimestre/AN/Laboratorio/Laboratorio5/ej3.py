"""
Ejercicio 3: 
Escribir una funcion en python llamada senint que para cada x ∈ Rn retorne y ∈ Rn tal
que yi es la aproximacion numerica de ∫ 0 a xi de cos(t) dt, usando la regla compuesta
del trapecio con Ni subintervalos. La cantidad Ni de subintervalos debe ser escogida
de forma que la longitud de los subintervalos sea menor o igual a 0.1 (ver comandos
floor, ceil, round). Para x = 0,...,2π, con pasos de 0.5, grafique simultaneamente 
sin(x) y senint(x).
"""

from ej1a import intenumcomp
import matplotlib.pyplot as plt
import numpy as np
import math 

def senint(x): 

    #np.ceil nos puede devolver un flotante (Ojo)
    N = math.ceil(x / 0.1) 

    #Para PM o Simpson necesito N par
        # if N % 2 == 1: 
        #     N = N + 1

    #Ojo, no es math.cos(x)
    y = intenumcomp(math.cos,0,x,N,"trapecio")
    return y 

#Genero un arreglo con nodos entre 0 y 2pi con pasos de 0,5
x = np.arange(0,2*np.pi,0.5)
#Evaluo los puntos anteriores en sen
y = np.sin(x)

#Genero una lista que contendrá las integrales de cos evaluadas en la lista anterior
yaprox = []

for xi in x:
    yaprox.append(senint(xi))

#Grafico ambas funciones 
plt.plot(x,y,color="yellow",label='Seno')
plt.plot(x,yaprox,color="red",label='Senint',linestyle="dotted")
plt.legend()
plt.show()