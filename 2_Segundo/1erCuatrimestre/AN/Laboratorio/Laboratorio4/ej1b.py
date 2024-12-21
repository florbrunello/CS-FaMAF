"""
Ejercicio 1: 
1. (a) Usando el comando loadtxt de python (np.loadtxt), leer los datos almacenados en
el archivo datos1a.dat Usar las formulas para un ajuste lineal por cuadrados minimos
para obtener la recta que mejor aproxima estos datos. Graficar los datos y el ajuste
obtenido.
(b) Realizar los mismos calculos con la ayuda de las funciones dot y ones (numPy).
(c) Dada la recta y = 3 / 4 x - 1/2, generar un conjunto de pares (xi, yi), 
i = 0, . . . , 19, en el intervalo [0, 10], con dispersion normal en el eje y. 
Realizar un ajuste lineal a los datos, obtener los coeficientes y dibujar el ajuste. 
Investigar los comandos: linspace, randm, polyval y polyfit (numPy).
"""

import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat")

#  Guardamos la primer columna en "x" y la segunda en "y"
x = datos[:, 0]
y = datos[:, 1]

# Calculo los 5 coeficientes (reconocer las cosas que se repiten dentro de las formulas a0 y a1)
m = len(x)
unos = np.ones(m)

a = np.dot(x, x)
b = np.dot(y, unos)
c = np.dot(x, y)
d = np.dot(x, unos)

a_0 = (a * b - c * d) / (m * a - d ** 2)
a_1 = (m * c - b * d) / (m * a - d ** 2)

plt.plot(x, y, '*')
plt.plot(x, a_1 * x + a_0)
plt.title("Inciso b")
plt.show()