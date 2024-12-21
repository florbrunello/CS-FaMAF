import random
import math
import time

# Metodo de razon entre uniformes
def Cauchy():
    while True: 
        u = random.random()
        v = (random.random() - 0.5) * 2
        if u**2 + v**2 < 1:
            return v / u
        
def cauchy_lamda(lamda):
    return lamda * Cauchy()

# Metodo de la transformada inversa
def cauchy_Transformada_Inversa(lamda):
    U = random.random()
    return lamda * math.tan(math.pi * (U - 0.5))

# Ejercicio d
def est_P(X, lamda, Nsim):
    p = 0
    for _ in range(Nsim):
        x = X(lamda)
        if -lamda < x and x < lamda:
            p += 1
    return p / Nsim

# Ejercicio e
def sim(X,lamda, Nsim):
    start = time.time()
    for _ in range(Nsim): 
        X(lamda)
    end = time.time()
    return end - start

def main():
    Nsim = 10000
    print("Estimacion de la probabilidad que el valor generado caiga en (-lamda,lambda)")
    print("Estimacion de P lamda = 1: ", est_P(cauchy_Transformada_Inversa, 1, Nsim))
    print("Estimacion de P: ", est_P(cauchy_Transformada_Inversa, 2.5, Nsim))
    print("Estimacion de P: ", est_P(cauchy_Transformada_Inversa, 0.3, Nsim))
    print("Probabilidad Teorica: 0.5")

    print("Tiempo de ejecucion Metodo Transformada Inversa: ", sim(cauchy_Transformada_Inversa, 1, Nsim))
    print("Tiempo de ejecucion Metodo Razon entre Uniformes: ", sim(cauchy_lamda, 1, Nsim))

if __name__ == "__main__":
    main()
    