import random
import numpy as np

def suma_dados(): 
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1 + d2

def exp_N(): 
    count = 0
    exitos = [0 for _ in range(11)]
    while np.sum(exitos) != 11:
        W = suma_dados()
        exitos[W-2] = 1
        count += 1
    return count

# Ejercicio a

def est_Esp(Nsim):
    suma = 0
    for _ in range(Nsim):
        suma += exp_N()
    return suma/Nsim

def est_Var(Nsim):
    v = 0
    media = est_Esp(Nsim)
    for _ in range(Nsim):
        v += (exp_N() - media)**2
    return v/Nsim

def est_Std(Nsim):
    return np.sqrt(est_Var(Nsim))

# Ejercicio b

def est_P(i, Nsim): 
    # P(N<=i)
    prob = 0
    for _ in range(Nsim):
        if exp_N() <= i:
            prob += 1
    return prob/Nsim

def main():
    N = [100, 1000, 10000]
    for i in range(len(N)):
        E, Std = est_Esp(N[i]), est_Std(N[i])
        print(f"n = {N[i]}: Esperanza ≃ {E:.5f}, Desv. est. ≃ {Std:.5f}")

    for i in range(len(N)):
        P = est_P(14, N[i])
        print(f"n = {N[i]}: Prob. de que N ≥ 15 ≃ {1 - P}")

    for i in range(len(N)):
        P = est_P(9, N[i])
        print(f"n = {N[i]}: Prob. de que N ≤ 9 ≃ {P}")

if __name__ == "__main__":
    main()