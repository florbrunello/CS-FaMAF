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

#Genero 20 puntos en el intervalo [0,10]
x = np.linspace(0,10,20)
y = 0.75 * x - 0.5

#Aplicamos una desviación a cada punto en y por una distribución normal
y_disp = y + np.random.randn(20)

#Hacemos un ajuste lineal sobre estos puntos
[a1,a0] = np.polyfit(x,y_disp,1)
#Evaluamos en x este ajuste para graficar
recta_ajustada = np.polyval([a1,a0],x)

plt.plot(x,y,'*',label="Puntos Originales")
plt.plot(x,y,label="Recta Original")
plt.plot(x, y_disp,'o',label="Puntos Desviados")
plt.plot(x,recta_ajustada,label="Nueva Aproximación")
plt.legend()
plt.title("Inciso c")
plt.grid()
plt.show()
