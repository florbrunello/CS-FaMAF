"""
Ejercicio 3: 
Obtener los datos almacenados en los archivos datos3a.dat y datos3b.dat para realizar
el ajuste de los siguientes modelos, es decir, determinar los coeficientes de cada modelo:
a) y(x) = C * (x**A)
b) y(x) = x / (Ax + B)
Ayuda: Transformar en cada caso la expresion dada a un modelo lineal, y obtener una recta que
mejor ajusta los datos (transformados) en el sentido de minimos cuadrados.
"""

import matplotlib.pyplot as plt 
import numpy as np

"""
filepath = "./datos3b.dat"
data = np.loadtxt(filepath)
"""

datos = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3b.dat")

x = datos[0]
y = datos[1]

"""
     y = x / (Ax + B)
  y^-1 = (x / (Ax + B))^-1 
   1/y = (Ax + B) / x 
   1/y = A + 1/x * B
"""

#Actualizo la tabla de datos x,y -> 1/x, 1/y

#x = 1/x
#y = 1/y
x_inv = [1/i for i in x]
y_inv = [1/i for i in y]

#Obtengo los coeficientes del polinomio que ajusta los datos con un polinomio de grado 1 (modelo lineal)
coefs = np.polyfit(x_inv, y_inv, 1)
#Evalúo el polinomio con los coeficientes que corresponden a la función original
ajuste=np.polyval(coefs,x)

#Coeficientes de mayor a menor grado 
B = coefs[0]
A = coefs[1]

print(f'Coeficiente A = {A}, Coeficiente B = {B}.')

#Grafico los datos del archivo y el ajuste obtenido
plt.plot(x,y,'o',label="Datos")
plt.plot(x, x / (A*x + B),label="Ajuste en el sentido de cuadrados mínimos")
plt.title("Inciso b")
plt.legend()
plt.show()