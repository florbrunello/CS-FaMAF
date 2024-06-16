from scipy.stats import chi2
from random import random
import numpy as np

p = np.array([0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01])
f_obs = np.array([188, 138, 87, 65, 48, 32, 30, 34, 13, 2])
n = sum(f_obs)
k = 10

# Estadistico de prueba
T = 0
for i in range(k):
    T += ((f_obs[i] - n*p[i])**2) / (n*p[i])

# Estadistico de prueba:  9.810370888711903
# p-valor con chi2:  0.36605
# print('Estadistico de prueba: ', T)
print('p-valor con chi2: ' , '{:.5f}'.format(1-chi2.cdf(T, k-1)))

# Usando una simulación
def premios(): 
    U = random()
    if U < 0.31:
        return 0
    elif U < 0.53:
        return 1
    elif U < 0.65:
        return 2
    elif U < 0.75:
        return 3
    elif U < 0.83:
        return 4
    elif U < 0.89:
        return 5
    elif U < 0.93:
        return 6
    elif U < 0.97:
        return 7
    elif U < 0.99:
        return 8
    else:
        return 9

def sim_Bin(Nsim=10000):
    datos_sim = np.zeros(n, int) # Muestras
    N = np.zeros(k, int) # Frecuencias observadas en la simulacion
    p_valor = 0

    for _ in range(Nsim):

        # Simular las frecuencias
        # Chequeado profe
        for j in range(n):
            datos_sim[j] = premios()
        N *= 0
        for obs in datos_sim:
            N[obs] += 1
        if sum(N) != n: # Deben ser n observaciones en total
            break
        
        # Calcular t de cada simulacion
        T_sim = 0
        for i in range(k): 
            T_sim += ((N[i] - n*p[i])**2)  / (n*p[i])
        
        # Comparar T con t (estadistico de prueba)
        if T_sim >= 9.810370888711903:
            p_valor += 1
    
    # Calcular el p-valor
    p_valor /= Nsim
    return p_valor

# p-valor con simulacion:  0.354
print('p-valor con simulacion: ', '{:.5f}'.format(sim_Bin()))