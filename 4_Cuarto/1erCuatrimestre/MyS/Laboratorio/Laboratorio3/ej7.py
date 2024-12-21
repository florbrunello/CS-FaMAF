import random

# La esperanza es e: con tres numeros aleatorios que sumes, 
# lo esperado es que te pases de 1 entre 2 y 3 veces.

def n():
    suma = 0                # Inicializo la suma en 0 (neutro)
    n = 0
    while suma <= 1:        # Mientras NO me pase de 1, sigo sumando
        suma += random.random()
        n += 1
    return n                # Se espera que n sea e 

def est_E_N(NSim):
    suma_e = 0              # Promedio las aproximaciones del valor e
    for _ in range(NSim):
        suma_e += n()
    return suma_e/NSim

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
    print('Aproximacion de e para Nsim =',N[i])
    print(est_E_N(N[i]))
