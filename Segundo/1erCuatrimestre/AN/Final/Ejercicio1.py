"""
Análisis Numérico 
Examen Final - 10 de agosto 2022
Laboratorio - Brunello, Florencia Luciana

Resolución:
Lo primero que haré es obtener f(w) = a2 w**2 + a1w + a0
Debo aproximar f dado cuatro puntos (xi, yi), i = 0,...,3 en el sentido de 
cuadrados mínimos. Para ello utilizo polyfit y polyval, ambas importadas de numpy. 
Polyfit me devolverá los coeficientes a2, a1 y a0 tal que minimicen el error de 
cuadrados mínimos. 
"""

import numpy as np

#Genero las listas x e y con los puntos a ser ajustados
x = [-2,0,2,4]
y = [0,-2,1,2]

#Hacemos un ajuste cuadrático sobre estos puntos
[a2,a1,a0] = np.polyfit(x,y,2)
polinomio_ajustado = np.polyval([a2,a1,a0], x)

"""
Una vez obtenidos los coeficientes de f, creamos una función que luego nos 
servirá para obtener el valor de f(5).
"""

# Creamos una función que haga la evaluación de nuestro polinomio 
def eval_pol(x):
    y = a2 * (x**2) + a1*x + a0
    return y

fun_cinco = eval_pol(5)

"""
Debemos resolver el sistema lineal utilizando el método de eliminación gaussiana.
Para ello, definimos soltrsup, egauss y soleg, donde: 
    - soltrsup: resuelve el sistema lineal Ax = b, donde A es una matriz 
    triangular superior.
    - egauss: implementa el método de eliminación Gaussiana.
    - soleg: resuelve sistemas lineales Ax = b usando eliminación Gaussiana.
"""

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

def egauss(A_, b_):

    #Copio la matriz y la lista b para no modificarlas
    A = A_.copy()
    b = b_.copy()
    n = A.shape[0]

    #Recorro las columnas de 0 a n-2
    for k in range(n-1):

        for i in range(k+1,n):

            if (A[k,k] == 0):
                print("El elemento a_kk es igual a cero")
                return None

            #Calculo el multiplicador 
            m = A[i,k] / A[k,k]

            for j in range(k+1,n):
                A[i,j] = A[i,j] - m * A[k,j]

            b[i] = b[i] - m * b[k]

    #No es necesario anular los elementos debajo de la diagonal, utilizo la parte triangular superior. 
    U = np.triu(A)

    return U, b

def soleg(A,b):
    U, y = egauss(A,b)
    x = soltrsup(U,y)
    return x

"""
Una vez definidas nuestras funciones, creamos la matriz A y el vector b, 
reemplazando f(5) por el resultado obtenido anteriormente. 
"""

#Definimos la matriz A y b: 

A = np.array([
        [fun_cinco, 1, 1],
        [1, fun_cinco, 1],
        [1, 1, fun_cinco],
], dtype="float")
b = np.array([1, 1, 1], dtype="float")

#Obtenemos la solución del sistema lineal
res = soleg(A,b)
print(f"La solución del sistema de ecuaciones es {res}")