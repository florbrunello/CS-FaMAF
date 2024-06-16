from scipy.stats import geom
import numpy as np
import random
import time

def geometrica_transformada(p):
    u = random.random()
    return int(np.log(1 - u) / np.log(1-p)) + 1

def geometrica_recursiva(p):
    u = random.random()
    i = 1
    prob = p 
    F = prob
    while u >= F:
        i += 1
        prob *= (1-p)
        F += prob
    return i

def ensayo(p):
    u = random.random()
    if u <= p:
        return 1 # exito
    else:
        return 0 # fracaso

def geometrica_ensayos(p):
    failures = 0
    res = ensayo(p)
    while res == 0:
        failures += 1
        res = ensayo(p)
    return failures + 1

def geometrica_ensayos_2(p):
    failures = 0 
    while True: 
        U = random.random()
        if U <= p: 
            return failures +1
        else: 
            failures += 1

def sim(X, p, Nsim): 
    start = time.time()
    for _ in range(Nsim):
        X(p)
    end = time.time()
    return end - start

def est_E(X, p, Nsim):
    suma = 0
    for _ in range(Nsim):
        suma += X(p)
    return suma / Nsim

def main(): 
    print("Comparacion de los algoritmos")
    print("p = 0.8 - X ~ Geom(0.8)")
    print("Metodo de la Transformada Inversa - Tiempo = ", sim(geometrica_transformada, 0.8, 10000))
    print("Aplicando la Formula Recursiva: ", sim(geometrica_recursiva, 0.8, 10000))
    print("Metodo de Simular Ensayos: ", sim(geometrica_ensayos, 0.8, 10000))
    print("Metodo de Simular Ensayos 2: ", sim(geometrica_ensayos_2, 0.8, 10000))

    print("p = 0.2 - X ~ Geom(0.2)")
    print("Metodo de la Transformada Inversa - Tiempo = ", sim(geometrica_transformada, 0.2, 10000))
    print("Aplicando la Formula Recursiva: ", sim(geometrica_recursiva, 0.2, 10000))
    print("Metodo de Simular Ensayos: ", sim(geometrica_ensayos, 0.2, 10000))
    print("Metodo de Simular Ensayos 2: ", sim(geometrica_ensayos_2, 0.2, 10000))

    print("Estimacion de E[X] con 10000 simulaciones")
    print("p = 0.8 - X ~ Geom(0.8)")
    print("Metodo de la Transformada Inversa: ", est_E(geometrica_transformada, 0.8, 10000))
    print("Aplicando la Formula Recursiva: ", est_E(geometrica_recursiva, 0.8, 10000))
    print("Metodo de Simular Ensayos: ", est_E(geometrica_ensayos, 0.8, 10000))
    print("Metodo de Simular Ensayos 2: ", est_E(geometrica_ensayos_2, 0.8, 10000))
    print("Valor teorico: ", geom.mean(0.8))

    print("p = 0.2 - X ~ Geom(0.2)")
    print("Metodo de la Transformada Inversa: ", est_E(geometrica_transformada, 0.2, 10000))
    print("Aplicando la Formula Recursiva: ", est_E(geometrica_recursiva, 0.2, 10000))
    print("Metodo de Simular Ensayos: ", est_E(geometrica_ensayos, 0.2, 10000))
    print("Metodo de Simular Ensayos 2: ", est_E(geometrica_ensayos_2, 0.2, 10000))

if __name__ == "__main__":
    main()
    