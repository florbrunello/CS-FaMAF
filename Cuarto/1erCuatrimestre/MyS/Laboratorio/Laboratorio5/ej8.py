import math
import random
import time

# Ejercicio a
def X_Suma(): 
    U = random.random()
    V = random.random()
    return U+V

# Ejercicio b
def X_Tranformada_Inversa():
    U = random.random()
    if U <= 0.5:
        return math.sqrt(2*U)
    else:
        return 2 - math.sqrt(2-2*U)
    
# Ejercicio c
def f(Y): 
    if 0 <= Y < 1:
        return Y
    elif 1 <= Y <= 2:
        return 2-Y
    else:
        return 0

def X_Aceptacion_Rechazo():
    while True:
        Y = random.uniform(0, 2)
        U = random.random()
        if U <= f(Y):
                return Y
        
# Otra version (yo)
def aceptacion_rechazo_X(): 
    while True: 
        Y = random.uniform(0,2)
        U = random.random()
        if 0 <= Y < 1: 
            if U < Y:
                return Y
        elif 1 <= Y < 2: 
            if U < 2 - Y:
                return Y

# Ejercicio b
def sim(X, Nsim):
    start = time.time()
    for _ in range(Nsim): 
        X()
    end = time.time()
    return end - start

def est_E(X, Nsim):
    e = 0
    for _ in range(Nsim):
        e += X()
    return e / Nsim

# Ejercicio c
# Calcular el x_o tal que P(X > x_o) = 0.125
def est_P(X, Nsim):
    X_Nsim = [X() for _ in range(Nsim)]
    x_o = 2
    while True:
        res = sum(1 for i in X_Nsim if i > x_o)/Nsim
        if res >= 0.125:
            return x_o
        else:
            x_o -= 0.01

# Ejercicio d
# P (X > k)
def est_P_X(X, k, Nsim):
    p = 0
    for _ in range(Nsim):
        r = X()
        if r > k:
            p += 1
    return p/Nsim

def main():
    Nsim = 10000
    print("Tiempo de ejecucion Metodo Ejercicio a: ", sim(X_Suma, Nsim))
    print("Tiempo de ejecucion Metodo Ejercicio b: ", sim(X_Tranformada_Inversa, Nsim))
    print("Tiempo de ejecucion Metodo Ejercicio c: ", sim(X_Aceptacion_Rechazo, Nsim))
    print("Tiempo de ejecucion Metodo Ejercicio d: ", sim(aceptacion_rechazo_X, Nsim))

    print("Estimacion de E(X)")
    print("E(X) ≃ ", est_E(X_Suma, Nsim))
    print("E(X) ≃ ", est_E(X_Tranformada_Inversa, Nsim))
    print("E(X) ≃ ", est_E(X_Aceptacion_Rechazo, Nsim))
    print("E(X) ≃ ", est_E(aceptacion_rechazo_X, Nsim))
    print("E(X) = 1")

    print("Hallar x_o tal que P(X > x_o) = 0.125")
    print("x_o ≃ ", est_P(X_Suma, Nsim))
    print("x_o ≃ ", est_P(X_Tranformada_Inversa, Nsim))
    print("x_o ≃ ", est_P(X_Aceptacion_Rechazo, Nsim))
    print("x_o ≃ ", est_P(aceptacion_rechazo_X, Nsim))

    print("Comparar la proporcion de veces que el algortimo devuelve un valor mayor a 1.5 con probabilidad 0.125")
    print("P(X > 1.5) = 0.125")
    print("P(X > 1.5) dos uniformes ≃ ", est_P_X(X_Suma, 1.5, Nsim))
    print("P(X > 1.5) Transformada Inversa ≃ ", est_P_X(X_Tranformada_Inversa, 1.5, Nsim))
    print("P(X > 1.5) Aceptacion y Rechazo ≃ ", est_P_X(X_Aceptacion_Rechazo, 1.5, Nsim))
    print("P(X > 1.5) Aceptacion y Rechazo (otra version) ≃ ", est_P_X(aceptacion_rechazo_X, 1.5, Nsim))

if __name__ == '__main__':
    main()
