"""
Ejercicio 4: 
Comparar las soluciones dadas por soleg y sollu al resolver Ax = b.
"""

from ej2b import soleg
from ej3 import sollu
import numpy as np

#Inciso A 

#Defino la matriz A y el arreglo b
A = np.array(
[ 
  [4, -1, 0, -1, 0, 0],
  [-1, 4, -1, 0, -1, 0],
  [0, -1, 4, 0, 0, -1],
  [-1, 0, 0, 4, -1, 0],
  [0, -1, 0, -1, 4, -1], 
  [0, 0, -1, 0, -1, 4],
], dtype="float")

b = np.array([1, 1, 1, 0, 0, 0], dtype="float")

#Resolución mediante Eliminación Gaussiana 
x = soleg(A,b)

#Resolución mediante factorización LU 
x_ = sollu(A,b)

print(f"Solución mediante EG {x}")
print(f"Solución mediante LU {x_}")

#Inciso B

b_ = np.array([1, 1, 1, 1, 1, 1], dtype="float")

#Resolución mediante Eliminación Gaussiana 
z = soleg(A,b_)

#Resolución mediante factorización LU 
z_ = sollu(A,b_)

print(f"Solución mediante EG {z}")
print(f"Solución mediante LU {z_}")

"""
Respuesta: la solución es la misma para ambos casos. 
"""