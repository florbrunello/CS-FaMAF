"""
Ejercicio 3:

Obtener el mayor y menor numero positivo en punto flotante (overflow y underflow ). Para
obtener el mayor numero de overflow escribir un ciclo que vaya calculando las sucesivas
potencias de 2 y que finalice cuando se produce overflow. Se recomienda utilizar el comando
isinf (importar la librera math) para detectar cuando se produce el overflow (escribir
help(math.isinf) para obtener informacion sobre este comando). Otra instruccion que
puede resultar util es break para interrumpir el ciclo cuando se produce el overflow, o
utilizar un while. El numero de underflow se puede obtener dividiendo por 2 repetidamente
hasta obtener un numero indistinguible del cero en punto flotante.

Help on built-in function isinf in module math:

isinf(...)
    isinf(x) -> bool
    
    Check if float x is infinite (positive or negative).

import math

a = 1.0

for idx in range(10000):
    a = a / 2.0
    print(a)
    if a == 0.0:
        print(-idx)
        break

a = 1.0

for idx in range(10000):
    a = a * 2.0
    print(a)
    if math.isinf(a):
        print(idx)
        break

a = 1.0
contador = 0
while (math.isinf(a) == False):
    a = a * 2.0
    contador = contador + 1
    print(a)
print(contador)

import math 

mayor = 2.0
while (not math.isinf(mayor*2)):
    mayor = mayor*2

print(f"El overflow es {mayor}")

menor = 2.0
while (menor/2 != 0):
    menor = menor / 2
    
print(f"El underflow es {menor}")

Poner 2.0 ! Sino no puede hacer la conversion de int a float. 
math.isinf(mayor*2), NO math.isinf(mayor), sino alcanzo al overflow 
y yo quiero cortar antes 
"""

import math
x = 2.0
i = 1

while not math.isinf(x*2):
	x = x*2
	i = i+1

print(f"La mayor potencia de 2 en punto flotante es = {x}")
print("Su exponente es:",i)

x = 2.0
i = 1

while x/2 != 0:
	x = x/2
	i = i-1

print("La menor potencia de 2 en punto flotante es:",x)
print("Su exponente es:",i)