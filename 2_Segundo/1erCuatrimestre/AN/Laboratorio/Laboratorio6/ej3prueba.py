"""
Ejercicio 3: 
Escribir una función llamada “sollu” que resuelva sistemas lineales Ax = b usando
descomposición LU con pivoteo (para obtener dicha descomposición investigar el sub-
paquete de la libreria scipy: “linalg”) para luego resolver Ly = P^(-1) b (¿cómo se 
puede obtener la inversa de una matriz de pivoteo?) y U x = y usando soltrinf y soltrsup.
La salida debe ser la solución x y debe tener entrada (A,b) con A∈ n*n y b∈n.
"""

from ej3 import sollu
import numpy as np 

def test_sollu():
    A = np.array([
        [3, 1, 1],
        [2, 6, 1],
        [1, 1, 4],
    ], dtype="float"
    )
    b = np.array([5, 9, 6], dtype="float")
    print(sollu(A, b)) 
    #Nos deberia dar [1, 1, 1]

test_sollu()