from scipy.stats import binom
import random
import time

# Ejercicio I
x_reordenados = [3, 1, 4, 0, 2]
p_reordenados = [0.35, 0.20, 0.20, 0.15, 0.10]

def discretaX(p=p_reordenados,x=x_reordenados):
    U = random.random()
    i, F = 0, p[0]
    while U >= F:
        i += 1
        F += p[i]
    return x[i]

# Ejercicio II

# Valores y probabilidades de X
x = [0, 1, 2, 3, 4]
p = [0.15, 0.20, 0.10, 0.35, 0.20]

# Probabilidades de Y
q = [0, 0, 0, 0, 0]
for i in range(5):
    q[i] = binom.pmf(i, 4, 0.45)

c = max(p[i]/q[i] for i in range(5))

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

# Genero numeros aleatorios entre 0 y 4 con distribucion binomial
def aceptacion_rechazo(p=p, q=q, c=c):
    while True: 
        Y = Binomial(4, 0.45)
        U = random.random()
        if U < p[Y] / (c * q[Y]):
            return Y

# Ejercicio III     
def sim(X,Nsim):
    start = time.time()
    for _ in range(Nsim):
        X()
    end = time.time()
    return end - start

def main():
    Nsim = 10000
    print("Tiempo de ejecución de X_Transformada: ", sim(discretaX, Nsim))
    print("Tiempo de ejecución de X_Rechazo: ", sim(aceptacion_rechazo, Nsim))

if __name__ == "__main__":
    main()
