"""
Ejercicio 5: 
Escribir dos funciones llamadas “jacobi” y “gseidel” que resuelvan sistemas lineales
Ax = b usando los metodos de Jacobi y Gauss-Seidel, respectivamente. La salida debe ser
[x,k] donde x es la solucion aproximada y k la cantidad de iteraciones realizadas. Debe
tener entrada (A,b,err,mit) con A∈Rn*n, b∈Rn, err tolerancia de error y mit cantidad
maxima de iteraciones. El algoritmo debe parar si ‖x(k) - x(k-1)‖∞ ≤err o k ≥mit.
"""

import numpy as np

#Implementación basada en el teórico 

def jacobi(A,b,err,mit):
    
    #Calculo la dimensión de la matriz A (conservo una dimensión)
    n = A.shape[0]
    #Creo dos arreglos de n ceros [0,...,0] 
    x = np.zeros(n)
    x_n = np.zeros(n)

    #Chequeo la tolerancia de iteraciones
    for k in range(mit):

        #Realizo la iteración del método de Jacobi 
        for i in range(n):

            sum = 0
            for j in range(n):
                if (j!=i):
                    sum = sum + A[i,j] * x[j]
            
            x_n[i] = (b[i] - sum) / A[i,i]

        #Chequeo la tolerancia del error 
        if (np.linalg.norm(x_n - x, np.inf) <= err):
            print('La norma infinito es pequeña')
            return x_n, k+1 
        
        x = x_n.copy() 
        #x_n = np.zeros(n)

    return x, k+1

#A = np.array( [ [10, -1, 2, 0],  [ -1, 11, -1 , 3 ], [ 2, -1, 10, -1], [ 0, 3, -1, 8 ] ] )
#b = np.array([ 6, 25, -11, 15 ])
#print(jacobi( A,b, 1e-6, 100 ))