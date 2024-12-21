import numpy as np
from scipy.stats import poisson
import random

# Ejercicio a

"""------------------------------------------------------------------------"""
# Calcular P (X = i) para i = 0, 1, ..., k
def Poisson_Num(lamda, i):
    p = np.exp(-lamda)
    if i == 0:
        return p
    else:
        for j in range(1, i+1):
            p *= lamda / j
        return p
    
def Sumatoria_Den(lamda, k): 
    p = np.exp(-lamda)
    S = p
    for j in range(1, k+1):
        p *= lamda / j
        S += p
    return S

# P (X = i), i = 0, 1, ..., k
def Poisson_Truncada(lamda, k, i):
    return Poisson_Num(lamda, i) / Sumatoria_Den(lamda, k)
"""------------------------------------------------------------------------"""
def Poisson_Mejorado(lamda):
    p = np.exp(-lamda)
    F = p
    for j in range(1, int(lamda) + 1):
        p *= lamda / j
        F += p
    U = random.random()
    if U >= F: 
        j = int(lamda) + 1
        while U >= F:
            p *= lamda / j
            F += p
            j += 1
        return j-1
    else:
        j = int(lamda)
        while U < F:
            F -= p
            p *= j / lamda
            j -= 1
        return j+1
    
# Metodo de la Transformada Inversa
def discretaX(lamda, k):
    U = random.random()
    S = Sumatoria_Den(lamda, k)
    p = np.exp(-lamda)/S
    i = 0; F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F += p
    return i

# Metodo de Rechazo
def rechazo(lamda, k):
    # Simular Y
    # Genero una variable aleatoria Poisson y calculo su probabilidad
    y = Poisson_Mejorado(lamda)
    qy = Poisson_Num(lamda, y)
    
    S = Sumatoria_Den(lamda, k)
    c = 1 / S
    
    u = random.random()
    
    while u >= Poisson_Truncada(lamda, k, y) / (c * qy):
        y = Poisson_Mejorado(lamda)
        u = random.random()
    return y

# Mi Version 
def aceptacion_rechazo_1(lamda, k): 
    S = Sumatoria_Den(lamda, k)
    c = 1 / S
    while True:
        Y = Poisson_Mejorado(lamda)
        qy = Poisson_Num(lamda, Y)
        U = random.random()
        if 0 <= Y <= k: 
            # Este if es siempre verdadero
            if U < Poisson_Truncada(lamda, k, Y) / (c * qy):
                return Y

# Mi version
def aceptacion_rechazo_2(lamda, k): 
    while True:
        Y = Poisson_Mejorado(lamda)
        if 0 <= Y <= k: 
            return Y
            
# Ejercicio b
# P (X > i)
def est_P(X, lamda, k, i, Nsim):
    est = 0 
    for _ in range(Nsim):
        res = X(lamda, k)
        if res > i:
            est += 1
    return est / Nsim

# Ejercicio c
# En este caso tiene distribucion Poisson
def generalizar_rechazo(lamda, a, b):  
    while True: 
        y = Poisson_Mejorado(lamda)
        if a <= y <= b:
            return y

def main(): 
    
    # Ejercicio b
    # P (X > 2) = 1 - P (X <= 2) = 1 - (P (X = 0) + P (X = 1) + P (X = 2))
    Nsim = 10000
    lamda = 0.7
    k = 10
    
    print("El valor exacto de P(X > 2) es: ", 1 - (Poisson_Truncada(lamda, k, i=0) + Poisson_Truncada(lamda, k, i=1) + Poisson_Truncada(lamda, k, i=2)))
    print("El valor estimado de P(X > 2) - Metodo TI: ", est_P(discretaX, lamda, k, 2, Nsim))
    print("El valor estimado de P(X > 2) - Metodo AR: ", est_P(rechazo, lamda, k, 2, Nsim))
    print("El valor estimado de P(X > 2) - Metodo AR1: ", est_P(aceptacion_rechazo_1, lamda, k, 2, Nsim))
    print("El valor estimado de P(X > 2) - Metodo AR2: ", est_P(aceptacion_rechazo_2, lamda, k, 2, Nsim))

if __name__ == "__main__":
    main()
