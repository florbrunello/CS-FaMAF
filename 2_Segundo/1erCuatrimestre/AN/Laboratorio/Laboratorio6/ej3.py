"""
Ejercicio 3: 
Escribir una función llamada “sollu” que resuelva sistemas lineales Ax = b usando
descomposición LU con pivoteo (para obtener dicha descomposición investigar el sub-
paquete de la libreria scipy: “linalg”) para luego resolver Ly = P^(-1) b (¿cómo se 
puede obtener la inversa de una matriz de pivoteo?) y U x = y usando soltrinf y soltrsup.
La salida debe ser la solución x y debe tener entrada (A,b) con A∈ n*n y b∈n.
"""

from ej1a import soltrsup
from ej1b import soltrinf
from scipy import linalg

def sollu(A,b):
    
    # A = P L U 
    P, L, U = linalg.lu(A)

    #  Ax = b -> PLUx = b
    #         P L U x = b
    #     P^T P L U x = P^T b 
    #           L U x = b_ 
    #             L y = b_ 
    #             U x = y

    #Calculo b_ (producto entre P^T y b)
    b_ = P.T @ b

    #Resuelvo la ecuación Ly=b_ del sistema (encuentro y)
    y = soltrinf(L,b_)

    #Resuelvo la ecuación Ux=Y del sistema (encuentro x)
    x = soltrsup(U,y)

    return x



