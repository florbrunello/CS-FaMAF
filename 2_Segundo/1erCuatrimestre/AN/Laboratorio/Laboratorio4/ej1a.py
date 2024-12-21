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
sum_xi = sum(x)
sum_yi = sum(y)
sum_xi2 = sum(x**2)
sum_xiyi = sum(x*y)

# Hay que resolver el siguiente sistema lineal
# [m      sum_xi ] [a0] = [ sum_yi ]
# [sum_xi sum_xi2] [a1]   [sum_xiyi]

# Evalúo las fórmulas para cada uno de los coeficientes de la recta.
a0 = (sum_xi2 * sum_yi - sum_xiyi * sum_xi) / (m * sum_xi2 - sum_xi ** 2)
a1 = (m * sum_xiyi - sum_xi * sum_yi) / (m * sum_xi2 - sum_xi ** 2)

# Creamos una función que haga la evaluación de nuestra recta
def eval_pol(x):
    return a1 * x + a0

# Imprimimos en pantalla nuestros coeficientes
print(a0, a1)

#Grafico los puntos
plt.plot(x,y,'*')

#Grafico el ajuste lineal 
plt.plot(x, a1 * x + a0)

plt.title("Inciso a")
plt.show()

"""
Opción: 

# Creamos una función que haga la evaluación de nuestra recta
def eval_pol(x):
    return a1 * x + a0

# Imprimimos en pantalla nuestros coeficientes
print(a0, a1)

# Armamos 100 puntos entre 0 y 5 y les aplicamos la función
z = np.linspace(0, 5, 100)
w = eval_pol(z)

# Ploteamos los puntos iniciales y la recta.
plt.plot(x, y, '*')
plt.plot(z, w)
plt.show()
"""