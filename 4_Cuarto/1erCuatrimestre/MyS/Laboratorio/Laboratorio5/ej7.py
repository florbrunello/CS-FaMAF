import random
import math
import time 

# Metodo Transformada inversa
def X_Transformada_Inversa(): 
    U = random.random()
    return (math.e)**U

# Metodo Aceptacion y Rechazo
def X_Acep_Rechazo(): 
    while True:
        Y = random.uniform(1, math.e)
        U = random.random()
        if U < 1/Y:
            return Y

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

def est_P(X, Nsim):
    p = 0
    for _ in range(Nsim):
        r = X()
        if r <= 2: 
            p += 1
    return p / Nsim

def main():
    Nsim = 10000
    print("Tiempo de ejecucion Metodo Transformada inversa: ", sim(X_Transformada_Inversa, Nsim))
    print("Tiempo de ejecucion Metodo Aceptacion y Rechazo: ", sim(X_Acep_Rechazo, Nsim))

    print("Estimacion de E[X]")
    print("E[X] ≃ ", est_E(X_Transformada_Inversa, Nsim))
    print("E[X] ≃ ", est_E(X_Acep_Rechazo, Nsim))
    print("E[X] = 1.718281828459045")

    print("Estimacion de P(X < 2)")
    print("P(X < 2) ≃ ", est_P(X_Transformada_Inversa, 10000))
    print("P(X < 2) ≃ ", est_P(X_Acep_Rechazo, 10000))
    print("P(X < 2) = 0.6931471805599453")

if __name__ == "__main__":
    main()
