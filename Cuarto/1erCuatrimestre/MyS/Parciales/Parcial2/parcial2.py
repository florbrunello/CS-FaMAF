# Brunello, Florencia - Parcial 2 - 16/04/2024

import random
import math 

# Ejercicio 1
def algo_x(p):
    x = [0, 1, 2, 3]
    q = [0.25, 0.25, 0.25, 0.25]
    c = max([p[i] / q[i] for i in range(len(x))])
    while True: 
        Y = random.randint(0, 3)
        U = random.random()
        if U < p[Y] / (c * q[Y]):
            return Y

def ejercicio1(): 
    p = [0.13, 0.22, 0.35, 0.30]
    return algo_x(p)

# Ejercicio 2
def ejercicio2():
    U = random.random()
    if 0 <= U < 2/3:
        return ((3/2) * U) ** (2/3)
    else: 
        return 3 * (U - (1/3))
    
def est_P(): 
    p = 0 
    for _ in range(10000): 
        res = ejercicio2()
        if res > 1: 
            p += 1
    return p / 10000

print("Estimacion de P ≃ ", est_P())

# Ejercicio 3
def hot_dog(T): 

    def lamda_t(t): 
        if 0 <= t < 3: 
            return 5 + 5*t
        elif 3 <= t <= 5: 
            return 20
        elif 5 < t <= 9: 
            return 30 - 2*t
        else: 
            return 0
    
    intervalos = [1, 2, 6, 8, 9]
    lamda =      [10, 15, 20, 18, 14]       

    j = 0
    t = -math.log(1 - random.random()) / lamda[j]
    NT = 0
    eventos = []
    while t <= T:
        if t <= intervalos[j]:
            V = random.random()
            if V < lamda_t(t) / lamda[j]:
                NT += 1
                eventos.append(t)
            t += -math.log(1 - random.random()) / lamda[j]
        else:  
            t = intervalos[j] + (t - intervalos[j]) * lamda[j] / lamda[j+1]
            j += 1
    return eventos

def est_E(): 
    e = 0 
    for _ in range(10000):
        e += len(hot_dog(9))
    return e / 10000

print("Numero esperado de arribos en [0,9] =", est_E())

# Ejercicio 4
def area(N):
    en_area = 0
    for _ in range(N): 
        U = 3 * random.random() - 1.5
        V = 3 * random.random() - 1.5
        if U**2 + ((V - (abs(U) ** (3/2)))**2) <= 1:
            en_area += 1
    return 9 * en_area / N

print(f"Estimacion del area ≃ {area(100000):.6f}")
