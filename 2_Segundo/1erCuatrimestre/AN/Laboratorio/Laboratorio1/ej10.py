"""
Ejercicio 10:

Escribir una funcion llamada SonReciprocos(x,y) que tenga dos numeros como input y
devuelva True si son recprocos, es decir, si xy = 1.
Luego ejecutar las siguientes instrucciones:
        import random
        for _ in range(100):
        x = 1 + random.random()
        y = 1/x
        if not SonReciprocos(x,y):
        print(x)
Explicar lo que sucedio.
"""

def son_reciprocos(x,y):
    #if x*y == 1: 
    tol = 1e-1
    if abs(x*y-1) < tol:
        return True

    else:
        return False

import random 
for _ in range (100): 
    x = 1 + random.random()
    y = 1/x
    if not son_reciprocos(x,y):
        print(x)

#Hecho así andan todos bien
#De las 100 corridas , 10 no son si usamos x*y == 1