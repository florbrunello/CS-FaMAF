"""
Ejercicio 2:
Para las siguientes funciones generar un conjunto de datos (xi,yi), i = 0,...,49
y realizar un ajuste polinomial de grado n con n = 0,...,5:
a) f(x) = arcsen(x), x ∈ [0,1]
b) g(x) = cos(x), x ∈ [0,4π].
Estudiar en cada caso la suma de los residuos.
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

#Inciso A

#Genero 50 puntos entre 0 y 1
x = np.linspace(0,1,50)
y = np.arcsin(x) 

#Coeficientes del polinomio que ajustan los datos x y 
#Polinoio evaluado en x con coefs de la funcion ajuste

for i in range (0,5):
    ajuste = np.polyfit(x, y, i)
    polinomio_ajustado = np.polyval(ajuste, x)
    error = sum(y - polinomio_ajustado)
    print(f"Suma de residuos {error}")    
    plt.plot(x,y,'*')
    plt.plot(x, polinomio_ajustado)
    plt.title("Inciso a")
    plt.show()
    
#Inciso B

x = np.linspace(0,4 * math.pi,50)
y = np.cos(x) 

for i in range (0,5):
    ajuste = np.polyfit(x, y, i)
    polinomio_ajustado = np.polyval(ajuste, x)
    error = sum(y - polinomio_ajustado)
    print(f"Suma de residuos {error}") 
    plt.plot(x,y,'*')
    plt.plot(x, polinomio_ajustado)
    plt.title("Inciso b")
    plt.show()