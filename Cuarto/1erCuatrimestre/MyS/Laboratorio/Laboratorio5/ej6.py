import random
import time

# Metodo Ejercicio 5
def M(n):
    U = [0] * n
    for i in range(n):
        U[i] = random.random()
    return max(U)

# Metodo Transformada inversa
def transformada_inversa(n):
    U = random.random()
    return (U ** (1/n))

# Metodo Aceptacion y Rechazo 
def acep_rechazo(n): 
    while True:
        #Variable Soporte
        Y = random.random()
        U = random.random()
        if U < Y**(n-1):
            return Y
        
def sim(X, n, Nsim):
    start = time.time()
    for _ in range(Nsim): 
        X(n)
    end = time.time()
    return end - start

def main():
    Nsim = 10000
    n = 10
    print("Tiempo de ejecucion Metodo Ejercicio 5: ", sim(M, n, Nsim))
    print("Tiempo de ejecucion Metodo Transformada inversa: ", sim(transformada_inversa, n, Nsim))
    print("Tiempo de ejecucion Metodo Aceptacion y Rechazo: ", sim(acep_rechazo, n, Nsim))

if __name__ == "__main__":
    main()