"""
Ejercicio 1: 
Escribir dos funciones en python llamadas soltrsup y soltrinf que resuelvan el sistema
lineal Ax = b, donde A es una matriz triangular (superior e inferior, respectivamente). 
La entrada debe ser (A,b) con A∈ n*n matriz triangular y b∈ n ,y la salida debe ser la
solución x. Se debe imprimir un mensaje de error si la matriz es singular.
"""

import numpy as np 

def soltrsup(A,b):
    
    #Chequeo que la matriz sea no singular
    if np.linalg.det(A) == 0 :
        print('La matriz es singular')
        return None

    #Obtengo n (cantidad de filas de A)
    n = len(b)
    #Copio b (NO creo un arreglo de n ceros)
    x = b.copy()

    #Calculo los elementos de la solución x 
    for i in reversed(range(n)):

        for j in reversed(range(i+1, n)):
            x[i] = x[i] - A[i, j] * x[j]

        x[i] = x[i] / A[i, i]
    
    return x