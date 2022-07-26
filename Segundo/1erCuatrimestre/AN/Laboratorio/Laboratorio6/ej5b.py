"""
Ejercicio 5: 
Escribir dos funciones llamadas “jacobi” y “gseidel” que resuelvan sistemas lineales
Ax = b usando los metodos de Jacobi y Gauss-Seidel, respectivamente. La salida debe ser
[x,k] donde x es la solucion aproximada y k la cantidad de iteraciones realizadas. Debe
tener entrada (A,b,err,mit) con A∈Rn*n, b∈Rn, err tolerancia de error y mit cantidad
maxima de iteraciones. El algoritmo debe parar si ‖x(k) - x(k-1)‖∞ ≤err o k ≥mit.
"""

from ej1b import soltrinf
import numpy as np 

#Implementación matricial

def gseidel(A,b,err,mit):

    #Defino las matrices M y N 
    M = np.tril(A)
    N = M - A

    #Calculo la dimensión de la matriz A
    n = b.shape
    #Creo un arreglo de n ceros [0,...,0] 
    x0 = np.zeros(n)

    #Chequeo la tolerancia de iteraciones
    for k in range(mit):
		
        #Calculo x_i mediante la fórmula de iteración
        #x1 = Minv @ ( N @ x0 + b) (debería calcular Minv)

		# x1 = (M^-1 N) x0 + M^-1 * b
		# M @ x1 = N @ x0 + b
        x1 = soltrinf(M, N @ x0 + b)

        #Chequeo la tolerancia del error 
        if (np.linalg.norm(x1-x0, ord=np.inf) < err):
            break
        else:
            x0 = x1.copy()  

    return [x1,k]