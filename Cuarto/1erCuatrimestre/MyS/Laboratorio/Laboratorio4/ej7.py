from math import exp
import random

def Poisson(lamda): 
    U = random.random()
    i = 0; p = exp(-lamda)
    F = p
    while U >= F:
        i += 1
        p *= lamda/i
        F += p
    return i

def Poisson_Mejorado(lamda):
    p = exp(-lamda)
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
    
def est_P(X, lamda, k, Nsim):
    # P (Y > k)
    suma = 0
    for _ in range(Nsim):
        res = X(lamda)
        if res > k: 
            suma += 1
    return suma/Nsim

def est_P_2(X, lamda, k, Nsim):
    # P (Y <= k)
    suma = 0
    for _ in range(Nsim):
        res = X(lamda)
        if res <= k: 
            suma += 1
    return suma/Nsim

def main():
    Nsim = 10000
    lamda = 0.7
    k = 2
    print(f"Estimacion de P (Y > {k}) con {Nsim} simulaciones")
    
    print(f"Usando Metodo de la Transfomada Inversa: {est_P(Poisson, lamda, k, Nsim)}")
    print(f"Usando Metodo de la Transformada Inversa Mejorado: {est_P(Poisson_Mejorado, lamda, k, Nsim)}")
    # P (Y > 2) = 1 - P (Y <= 2) 
    print(f"Usando Metodo de la Transfomada Inversa: {1 - est_P_2(Poisson, lamda, k, Nsim)}")
    print(f"Usando Metodo de la Transformada Inversa Mejorado: {1 - est_P_2(Poisson_Mejorado, lamda, k, Nsim)}")

if __name__ == "__main__":
    main()
