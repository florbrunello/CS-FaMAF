"""
Ejercicio 4: 

Escribir la siguiente secuencia de comandos en un archivo con extension .py y ejecutarlo.
x = 0
while x != 10:
x = x + 0.1
Para interrumpir la ejecucion, pulsar <CTRL>+<c>. ¿Que ocurre si en lugar de incrementarse
la variable en 0.1 lo hace en 0.5? ¿Por que?
"""

x = 0
while abs (x-10) >= 0.0000000001: 
    x = x + 0.1
print (x)

#profes

x = 0
while abs (x-10) >= 0.0000000001: 
    x = x + 0.5
print (x)

"""
Imprime 10.0
Caso 0,1 -> nunca es igual a 10, lo saltea
Al pasar a binario se acumulan errores
"""

