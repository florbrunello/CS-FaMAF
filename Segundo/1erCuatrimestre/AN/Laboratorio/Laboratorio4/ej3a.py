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

datos = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3a.dat")

x = datos[0]
y = datos[1]

"""
y = C * (x**A)
ln (y) = ln (C * (x**A))
ln(y) = ln(C) + A*ln(x)

ln(y) = y_ln
ln(x) = x_ln
ln(C) = b

y_ln = b  + A * x_ln
"""

#Actualizo la tabla de datos y, x -> ln(y), ln(x)
x_ln = np.log(x)
y_ln = np.log(y)

#Obtengo los coeficientes del polinomio que ajusta los datos con un polinomio de grado 1 (modelo lineal)
coefs = np.polyfit(x_ln, y_ln, 1)

#Coeficientes de mayor a menor grado 
A = coefs[0]
lnC = coefs[1]
C = np.exp(lnC)

print(f'Coeficiente A = {A}, Coeficiente C = {C}.')

#Grafico los datos del archivo y el ajuste obtenido
plt.plot(x,y,'o',label="Datos")
plt.plot(x, C * x ** A,label="Ajuste en el sentido de cuadrados mínimos")
plt.title("Inciso a")
plt.legend()
plt.show()