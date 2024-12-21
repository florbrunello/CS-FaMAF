"""
Ejercicio 4: 
El polinomio interpolante se puede ver afectado por el conjunto de puntos elegidos. 
Considerar la funcion f tal que f(x) = 1/(1+25x^2).
Graficar f, pn y qn en una misma figura usando 200 puntos igualmente espaciados en el
intervalo [-1, 1], donde:
    (a) pn es el polinomio que interpola los pares {(xi , f(xi))} con i = 1,...,n+1 con
        xi = (2(i -1) / n) - 1, para i = 1,...,n+1.

    (b) qn es el polinomio que interpola los pares {(xi, f(xi))} con i = 0,...,n con 
        xi = cos((2i+1)π / (2n+2)), para i = 0,...,n. Estos puntos son conocidos como 
        nodos de Tchebychev.

Varie n entre 1 y 15. Implementar la resolucin de este ejercicio en el script “lab3ej4”.
Al ejecutarlo debe mostrar 15 graficos.
"""

import numpy as np 
import matplotlib.pyplot as plt
from ej1 import ilagrange

#Gráfico
def funej4 (x):
    return 1/(1+25*x**2)

#Genero 200 puntos gualmente espaciados entre -1 y 1
x = np.linspace (-1,1,201)
#Genero la lista y con la evaluación de esos puntos en f
y = funej4(x)

#Inciso A y B

#Genero dos listas con el restultado de las interpolaciones
fun_a = []
fun_b = []

for i in range (1,16):
    puntos_a = np.arange(1,i+2)
    puntos_a = ((2*(puntos_a -1)) / i) - 1
    f_puntos_a = funej4(puntos_a)
    interpol_a = ilagrange(puntos_a, f_puntos_a,x)
    #Guardo el resultado de haber interpolado 
    fun_a.append(interpol_a)

    puntos_b = np.arange(0,i+1)
    puntos_b = np.cos((2*puntos_b+1)/(2*i+2) * np.pi)
    f_puntos_b = funej4(puntos_b)
    interpol_b = ilagrange(puntos_b, f_puntos_b, x)
    #Guardo el resultado de haber interpolado 
    fun_b.append(interpol_b)

#Genero 15 gráficos en ventanas simultáneas
i=0
fig,ax=plt.subplots(3,5)

for idx in range(3):
    for idy in range(5):
            #Grafico la interpolación a y b
            ax[idx][idy].plot(x, fun_a[idy+i],label="Interpolación a")
            ax[idx][idy].plot(x, fun_b[idy+i],label="Interpolación b")
            #Grafico la función f 
            ax[idx][idy].plot(x,y,label="f(x)")
    i = i + 5

fig.show()
plt.show()