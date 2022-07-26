"""
Ejercicio 6: 
Usar los metodos de Jacobi y Gauss-Seidel para resolver a y b con una tolerancia de 
10^(-11) para (1) y 10^(-4) para (2). ¿Cuantas iteraciones son necesarias en cada 
caso para alcanzar la precision deseada?
"""

from ej5ab import jacobi
from ej5b import gseidel
import numpy as np

#Inciso A 

#Defino la matriz A y el arreglo b
A = np.array(
[ 
  [3, 1, 1],
  [2, 6, 1],
  [1, 1, 4],
], dtype="float")

b = np.array([5, 9, 6], dtype="float")

#Resolución mediante el método de Jacobi 
x,k = jacobi(A,b,1e-11,100)

#Resolución mediante el método de Gauss-Seidel 
x_,k_ = gseidel(A,b,1e-11,100)

print("Matriz (1):")
print(f"Usando el método de Jacobi, se necesitan {k} iteraciones para alcanzar la presición deseada")
print(f"Usando el método de Gauss-Seidel, se necesitan {k_} iteraciones para alcanzar la presición deseada")

#Inciso B

#Defino la matriz B y el arreglo c
B = np.array(
[ 
  [5, 7, 6, 5],
  [7, 10, 8, 7],
  [6, 8, 10, 9],
  [5, 7, 9, 10],
], dtype="float")

c = np.array([23, 32, 33, 31], dtype="float")

#Resolución mediante el método de Jacobi 
y,j = jacobi(A,b,1e-4,100)

#Resolución mediante el método de Gauss-Seidel 
y_,j_ = gseidel(A,b,1e-4,100)

print("Matriz (2):")
print(f"Usando el método de Jacobi, se necesitan {j} iteraciones para alcanzar la presición deseada")
print(f"Usando el método de Gauss-Seidel, se necesitan {j_} iteraciones para alcanzar la presición deseada")