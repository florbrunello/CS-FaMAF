"""
Ejercicio 7: 

Escribir una funcion que calcule la potencia enesima de un numero, es decir que devuelva
x n para x real y n entero. Realice un programa que utilice la funcion e imprima en pantalla
las primeras 5 potencias naturales de un numero ingresado.
"""

#Ejercicio 7a
def potencia(x,n):
    res = 1
    for i in range (1,n+1):
        res = res * x
        print (f'El resultado de la operacion {x}**{i} es {res}\n')
    print (f'El resultado final es {res}\n')
    return (res)

#Ejemplo
potencia (2,3)

#Ejercicio 7b

z = int(input('Ingrese un numero real\n'))
potencia(z,5)

"""
n = int(input('Ingrese la potencia a la cual quiere elevar x\n'))
print(potencia(x,n))
(potencia (2,5))
print("Ingrese valor de base")
x = int(input())
potencia(x,5)
"""

"""
Diferencia entre:
    print(potencia (2,5))
    El resultado final es 32
    32

    potencia (2,5)
    El resultado final es 32

def potenciacion (x,n):
    res = x
    for i in range (1,n):
        res = x * res
    return res

z = int(input('Ingrese un numero real\n'))
for i in range(1,6):
    print(potenciacion(z,i))
"""
