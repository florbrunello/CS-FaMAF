"""
Ejercicio 6: 

Escribir un programa que pida dos numeros reales e imprima en la pantalla el mayor de
ellos. El programa debe indicar si los numeros son iguales.

def mayor(x,y):
    
    #x = int(input('Ingrese un numero real'))
    #y = int(input('Ingrese un numero real'))

    if x>y: 
        print(f'El mayor número es {x}\n')
        return True

    elif x<y:
        print(f'El mayor numero es {y}\n')
        return True
        
    else:
        print(f'Los numeros {x} y {y} son iguales\n')
        return False

mayor(5,4)

x = int (input('Ingrese un numero\n'))
y = int (input('Ingrese un numero\n'))
print(mayor(x,y))
"""

def comparar ():
    n = int(input("Ingrese un entero:"))
    m = int(input("Ingrese otro entero:"))
    
    if n<m:
        return(m)
    elif n==m: 
        return('Los numeros son iguales')
    else:
        return(n)

res = comparar()
print(res)

#Si pongo print(comparar()) devuelve None
#No usar acentos ni ene
