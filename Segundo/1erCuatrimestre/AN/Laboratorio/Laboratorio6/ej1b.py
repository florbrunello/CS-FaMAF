"""
Ejercicio 1: 
Escribir dos funciones en python llamadas soltrsup y soltrinf que resuelvan el sistema
lineal Ax = b, donde A es una matriz triangular (superior e inferior, respectivamente). 
La entrada debe ser (A,b) con A∈ n*n matriz triangular y b∈ n ,y la salida debe ser la
solución x. Se debe imprimir un mensaje de error si la matriz es singular.
"""

import numpy as np

def soltrinf(A,b):

    #Chequeo que la matriz sea no singular
    if np.linalg.det(A) == 0 :
        print('La matriz es singular')
        return None

    #Obtengo n (cantidad de filas de A)
    n = A.shape[0]
    #Creo un arreglo de n ceros [0,...,0] 
    x = np.zeros(n)

    #Calculo los elementos de la solución x 
    for i in range(n):
        
        suma = 0
        for j in range(i):
            suma  = suma + A[i,j] * x[j]

        x[i] = b[i] - suma
        x[i] = x[i] / A[i,i]

    return x 
