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

#Calculo la matriz completa (incluyendo los ceros)

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

            for j in range(k,n):
                A[i,j] = A[i,j] - m * A[k,j] 

            b[i] = b[i] - m * b[k]

    return A, b