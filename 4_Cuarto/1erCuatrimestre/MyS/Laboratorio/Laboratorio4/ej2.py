import random
import math
import time

# Ejercicio a
def suma_estimada(Nsim): 
    suma = 0
    for _ in range(Nsim):
        U = int(random.random()*10000) + 1
        suma += math.exp(U/10000)
    result = suma / Nsim * 10000
    return result

# Ejercicio b
def suma_estimada_100(): 
    return suma_estimada(100)

# Ejercicio c
def suma_n_terminos(N):
    suma = 0
    for i in range(1, N+1):
        suma += math.exp(i/10000)
    return suma

def sim(X, N):
    start = time.time()
    X(N)
    end = time.time()
    return end - start

def main():
    print("Valor exacto: ", suma_n_terminos(10000), "Tiempo: ", sim(suma_n_terminos, 10000))
    print("Estimacion Monte Carlo 100 simulaciones: ", suma_estimada_100(), "Tiempo: ", sim(suma_estimada, 100))
    print("Estimacion usando los primeros 100 terminos: ", suma_n_terminos(100), "Tiempo: ", sim(suma_n_terminos, 100))

if __name__ == "__main__":
    main()
