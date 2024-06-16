from scipy.stats import chi2, binom
from random import random
import numpy as np

# Ejercicio a
def est_de_prueba():
    p = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    f_obs = np.array([158, 172, 164, 181, 160, 165])
    n = sum(f_obs) # n = 1000
    k = len(p)

    T = 0
    for i in range(k):
        T += (f_obs[i] - n * p[i])**2 / (n*p[i])

    return T

# Distribución chi-cuadrado con 5 grados de libertad y T valor observado
# Valor critico
T = est_de_prueba()
# print('T: ' , T)
# p_valor con chi2: 0.82372
print('p-valor con chi2; ', '{:.5f}'.format(1-chi2.cdf(T,5)))

# Ejercicio b
def sim(Nsim=10000):
    p = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    f_obs = np.array([158, 172, 164, 181, 160, 165])
    n = sum(f_obs)
    k = len(p)
    N = np.zeros(k,int) # Frecuencias observadas
    T = 2.18
    p_valor = 0
    tasas_riesgo = np.array([1/6, 1/5, 1/4, 1/3, 1/2])
    
    for _ in range(Nsim):

        # Simular las frecuencias
        N = N * 0             # = [0 0 0 0 0 0]
        tiradas = n           # 1000
        for i in range(k-1):  # 5
            dados_k = binom.rvs(tiradas, tasas_riesgo[i])
            N[i] = dados_k
            tiradas -= dados_k
        N[5] = tiradas

        # Calcular t de cada simulacion
        T_sim = 0
        for i in range(k): 
            T_sim += ((N[i] - n*p[i])**2)  / (n*p[i])
        
        # Comparar T con t (estadistico de prueba)
        if T_sim >= 2.18:
            p_valor += 1
        
    # Calcular el p-valor
    p_valor /= Nsim
    return p_valor

# p valor simulando frecuencias: 0.8263
print("p-valor simulando frecuencias: ", sim())
