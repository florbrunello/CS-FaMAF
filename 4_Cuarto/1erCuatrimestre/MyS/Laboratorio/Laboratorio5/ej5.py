import random
import math

# Ejercicio a
def exponencial_lamda(lamda):
    U = 1 - random.random()
    return -math.log(U) / lamda

def M():
    X = exponencial_lamda(1)
    Y = exponencial_lamda(2)
    Z = exponencial_lamda(3)
    return max(X, Y, Z)

def m(): 
    X = exponencial_lamda(1)
    Y = exponencial_lamda(2)
    Z = exponencial_lamda(3)
    return min(X, Y, Z)

def m1(): 
    return exponencial_lamda(6)

# Ejercicio b
def muestraM(): 
    return [M() for _ in range(10)]

def muestram(): 
    return [m() for _ in range(10)]

def est_E(X, Nsim):
    e = 0
    for _ in range(Nsim):
        e += X()
    return e / Nsim

def main():
    print("Muestras de M")
    print(muestraM())

    print("Muestras de m")
    print(muestram())
    
    print("Estimacion del Minimo")
    print("E(m) ≃ ", est_E(m, 10000))
    print("E(m) = 0.16666666666666666")

if __name__ == '__main__':
    main()