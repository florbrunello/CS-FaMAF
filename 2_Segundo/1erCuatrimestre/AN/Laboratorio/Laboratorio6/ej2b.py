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

from ej1a import soltrsup
from ej2ab import egauss

def soleg(A,b):
    U, y = egauss(A,b)
    x = soltrsup(U,y)
    return x