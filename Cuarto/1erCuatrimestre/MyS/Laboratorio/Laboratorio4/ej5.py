from scipy.stats import binom
import random
import time

# Ejercicio I
def Binomial(n,p):
    c = p / (1-p)
    prob = (1-p)**n
    F = prob; i = 0
    U = random.random()
    while U >= F:
        prob *= (c * (n-i)) / (i+1)
        F += prob
        i += 1
    return i

# Ejercicio II
def ensayos(n, p):
    exitos = 0
    for _ in range(n):
        U = random.random()
        if U <= p:
            exitos += 1
    return exitos

# Ejercicio a
def sim(X, n, p, Nsim):
    start = time.time()
    for _ in range(Nsim):
        X(n, p)
    end = time.time()
    return end - start

# Ejercicio b
def est_E(X, n, p, Nsim):
    e = 0
    for i in range(Nsim):
        e += X(n, p)
    return e / Nsim

def est_P(X, n, p, k, Nsim):
    # P(X = k)
    c = 0
    for _ in range(Nsim):
        r = X(n, p)
        if r == k:
            c += 1
    return c / Nsim

def main():
    Nsim = 10000
    n, p = 10, 0.3
    print("Tiempo de ejecución de Binomial: ", sim(Binomial, n, p, Nsim))
    print("Tiempo de ejecución con ensayos: ", sim(ensayos, n, p, Nsim))

    print("Estimación de E:" 
          f"    Usando Binomial = {est_E(Binomial, n, p, Nsim)}"
          f"    Usando ensayos = {est_E(ensayos, n, p, Nsim)}")
    print("Estimación de P(X = 0):"
            f"    Usando Binomial = {est_P(Binomial, n, p, 0, Nsim)}"
            f"    Usando ensayos = {est_P(ensayos, n, p, 0, Nsim)}")
    print("Estimación de P(X = 10):"
            f"    Usando Binomial = {est_P(Binomial, n, p, 10, Nsim)}"
            f"    Usando ensayos = {est_P(ensayos, n, p, 10, Nsim)}")
    
    # Ejercicio c
    # Generar todos los valores de la Binamial con n = 10 y p = 0.3 para chequear que este ok
    print("Valor Esperado de la Binomial con n = 10 y p = 0.3 es", binom.mean(10, 0.3))
    print("Probabilidad de X = 0: ", binom.pmf(0, 10, 0.3))
    print("Probabilidad de X = 10: ", binom.pmf(10, 10, 0.3))
    
    """
    print("Usando la funcion Binomial recursiva:")
    n = 10;  p = 0.3
    c = p / (1-p)
    prob = (1-p)**n
    F = prob
    print("j  |         P(X = j)       |        P(X <= j)   ")  
    print("--------------------------------------------------")
    print(f"0  | {prob} | {F}")
    for i in range(10):
        prob *= (c * (n-i)) / (i+1)
        F += prob
        print(f"{i+1}  | {prob} | {F}")
    """

if __name__ == "__main__":
    main()
    