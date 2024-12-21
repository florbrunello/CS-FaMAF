"""
Ejercicio 2: 
a) Escribir una función llamada “egauss” que implemente el método de eliminación
Gaussiana. Debe tener entrada (A,b) con A∈ n*n y b∈ n , con salida [U,y] con
U ∈ n*n triangular superior e y ∈ n.
b) Escribir una función llamada “soleg” que resuelva sistemas lineales Ax = b usando
eliminación Gaussiana y resolviendo el sistema triangular superior U x = y (usando
soltrsup). Debe tener entrada (A,b) con A∈ n*n y b∈ n y, la salida debe ser la
solución x.
"""

from ej2b import soleg
import numpy as np 

#Creo una matriz de tamaño 4*4
A = np.random.rand(4,4)
#Creo un arreglo de 4 elementos
x = np.random.rand(4)
#b es la sulución de calcular A * x 
b = A @ x
#Calculo el arrelglo x a partir de b, este debe coincidir con el generado anteriormente
x_sol = soleg(A,b)
print(x_sol, x)