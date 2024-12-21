from scipy.stats import chi2, norm
from statistics import stdev
from random import random
import numpy as np

p = np.array([0.25, 0.5, 0.25])
f_obs = np.array([141, 291, 132])
n = sum(f_obs)
k = len(p)

# Ejercicio a
# Estadistico de prueba
T = 0
for i in range(k):
    T += ((f_obs[i] - n * p[i])**2) / (n*p[i])

#print('T: ' , '{:.5f}'.format(T))
print('p-valor con chi2: ' , '{:.5f}'.format(1-chi2.cdf(T, 2)))

# Ejercicio b
def flores():
    U = random()
    if U < 0.5:
        i = 1 # Rosa
    elif U < 0.75:
        i = 0 # Blanca
    else: 
        i = 2 # Roja
    return i

def sim(Nsim=10000):
    p = np.array([0.25, 0.5, 0.25])
    f_obs = np.array([141, 291, 132])
    n = sum(f_obs)
    k = len(p)
    datos = np.zeros(n,int) # Muestras
    N = np.zeros(k,int) # Frecuencias observadas
    t = 0.86170
    p_valor = 0

    for _ in range(Nsim):

        # Simular las frecuencias
        for j in range(n):
            datos[j] = flores()
        N *= 0
        for obs in datos:
            N[obs] += 1
        
        # Calcular t de cada simulacion
        T_sim = 0
        for i in range(k): 
            T_sim += ((N[i] - n*p[i])**2)  / (n*p[i])
        
        # Comparar T con t (estadistico de prueba)
        if T_sim >= 0.86170:
            p_valor += 1
    
    # Calcular el p-valor
    p_valor /= Nsim
    return p_valor

# p-valor = 0.6444
print("p-valor con sim:  ", sim())
