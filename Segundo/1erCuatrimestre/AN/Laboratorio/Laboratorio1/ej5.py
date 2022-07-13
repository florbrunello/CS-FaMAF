"""
Ejercicio 5: 

a) Escribir un programa que calcule el factorial de 6.
b) Importar la librera math, ¿que funcion puede utilizar para calcular el punto anterior?
c) Escribir una funcion que calcule el factorial de un numero n dado
"""

#Ejercicio a

"""
print (1*2*3*4*5*6)

i = 6
fact = 1

while i>1:
    fact = fact * (i)
    i = i-1    

print(fact)
"""

import math 

res = 1
for i in range (1,7):
    res = res * i

print(f"El factorial de 6 con un for es {res}")

#Ejercicio b

import math 

print(math.factorial(6))

#from math import factorial
#print(f"El factorial de 6 con la librería math es {factorial(6)}")

#Ejercicio c

def factorial (n):
    res  =  1
    for  i in range (1,n+1):
        res = res*i

    return res

resultado = factorial(6)
print(resultado)

n = int(input("Ingrese un entero:"))
fact = (math.factorial(n))
print(fact)