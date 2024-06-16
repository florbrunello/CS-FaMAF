import numpy as np
import random

def n():
    e3 = np.exp(1)**(-3)
    p = 1                        # Inicializo la productoria en 1 (neutro multiplicativo)
    n = 0
    while p >= e3:               # Mientras la productoria de mayor o igual a e^(-3) sigo
        p = p*random.random()
        n += 1
    return n

def est_E_N(Nsim):
    suma = 0
    for _ in range(Nsim):
        suma += n()
    return suma/Nsim

# Ejercicio a 

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
    print('Aproximacion para Nsim =',N[i])
    print(est_E_N(N[i]))

# Ejercicio b

def est_P (i, Nsim=1000000):
    suma = 0
    for _ in range(Nsim):
        x = n()
        if x == i:
            suma += 1
    return suma/Nsim

I = [0,1,2,3,4,5,6]
for i in range(len(I)):
    print('Aproximacion para Nsim =',I[i])
    print(est_P(I[i]))
    