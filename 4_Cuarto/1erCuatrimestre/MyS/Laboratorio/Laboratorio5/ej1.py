import random
import math

# Utilizando el metodo de la Transformada Inversa para Variables Aleatorias Continuas

# Ejercicio a
def inversaXa():
    U = random.random()
    if U <= 0.25:
        return 2 + 2*(math.sqrt(U))
    else:
        return 6 - 2*(math.sqrt(3-3*U))

# Ejercicio b
def inversaXb():
    U = random.random()
    if U <= 0.6:
        return (math.sqrt((35*U)/3 + 9) - 3)
    else: 
        return (-(-1/2)**3) * (35*U-19)**3

# Ejercicio c
def inversaXc():
    U = random.random()
    if U <= 0.0625:
        return (1/4*math.log(16*U))
    else: 
        return (4*U-2/3)
