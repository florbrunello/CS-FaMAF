import random
import math

# X ~ Exp(lamda)
def exponencial_lamda(lamda):
    U = 1 - random.random()
    return -math.log(U) / lamda

# Metodo de Composicion
def X(): 
    U = random.random()
    if U < 0.5: 
        return exponencial_lamda(1/3)
    elif U < 0.8: 
        return exponencial_lamda(1/5)
    else:
        return exponencial_lamda(1/7)

# Sample - Genero valores entre 0 e infinito
def sample():
    return [X() for _ in range(25)]

def est_E(X, Nsim):
    e = 0 
    for _ in range(Nsim):
        e += X()
    return e / Nsim

def main():
    Nsim = 10000
    print("E(X) ≃ ", est_E(X, Nsim))
    print("E(X) = 4.4")

    print(f"Sample: {sample()}")

if __name__ == '__main__':
    main()    