"""
Ejercicio 1: 
Una persona debe comprar fertilizantes (abono) para sus campos. Le informaron que cada
kilogramo de fertilizante le alcanza para 10m2 de su campo, y debido a las caracteristicas
propias de esas tierras, el fertilizante debe contener (al menos): 3g de fosforo (P), 
1.5g de nitrogeno (N) y 4g de potasio (K) por cada 10m2. En el mercado existen 2 tipos
de fertilizantes: T1 y T2. El fertilizante T1 contiene 3g de P, 1g de N y 8g de K y 
cuesta $10 por kilogramo. En cambio, el fertilizante T2 contiene 2g de P, 3g de N y 2g
de K y cuesta $8 por kilogramo. ¿cuantos kilogramos de cada fertilizante se debe comprar,
por cada 10m2de campo, de modo de minimizar el costo total, cubriendo los requerimientos
de su suelo?. Graficar la region factible para el problema.
"""

# c = (10,8)
# A_ub = - [3, 2], b_ub = - [ 3 ]
#          [1, 3]           [1.5]
#          [8, 2]           [ 4 ]

import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np
# from scipy.optimize import linprog

#Creo el arreglo costo = [10,8], la matriz A_ub y el vector b_ub
costo = np.array([10, 8], dtype="float")
mat_des = - np.array([
    [3, 2],
    [1, 3],
    [8, 2],
], dtype="float")
vec_des = - np.array([3, 1.5, 4], dtype="float")

#Resuelvo el problema de minimixación 
res = optimize.linprog(c=costo, A_ub=mat_des, b_ub=vec_des)
#res.x contiene el par (x_1, x_2): cantidad de T1 y T2 a comprar
solucion = res.x
#res.fun contiene la evaluacion de f(x,y) = 10 * x_1 + 8 * x_2
evaluacion = res.fun

print(f"Solucion: {solucion}")
print(f"Dinero por 10 m2: {evaluacion}")
print(f"Encontro solucion? {res.success}")

#Creo las rectas que delimitan la región factible
x = np.linspace(0, 3, 100)
y1 = 1.5 - 1.5 * x
y2 = 0.5 - 1/3 * x
y3 = 2 - 4 * x

#Comparo los 100 puntos de las rectas y1, y2 e y3 y grafico los maximos
curva_region = np.maximum(np.maximum(y1, y2), y3)

#Grafico las tres rectas
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

#Pinto el área entre dos lineas: el máximo entre las rectas y1, y2, y3 y 3 (alpha suaviza el color).
plt.fill_between(x, curva_region, 3, alpha=0.2)
#Hago un punto en la solucion: mínimo (x1,x2)
plt.plot(solucion[0], solucion[1], '*')
#Limito la región en la cual quiero realizar el gráfico 
plt.xlim([0, 3])
plt.ylim([0, 3])
#Muestro el gráfico 
plt.show()