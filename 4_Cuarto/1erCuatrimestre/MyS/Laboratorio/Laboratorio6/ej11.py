from scipy.stats import chi2, binom, kstest
from math import factorial
import numpy as np
import random

datos = np.array([6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7])
n = len(datos) # n = 18 Tamaño de la muestra
k = 9 # Cantidad de intervalos o numero de agrupamiento de los valores considerados
p_est = (sum(datos)/len(datos)) / 8 # Estimacion de p para una Binomial(8, p)
# print("p: ", p_est)

# Probabilidades teoricas p_i 
p = np.zeros(k)
for i in range(8):
    aux = factorial(8)/(factorial(i)*factorial(8-i))
    p[i] = aux * (p_est**i) * ((1-p_est)**(8-i))
p[8] = 1 - sum(p)

# Frecuencias observadas N_i
f_obs = np.zeros(k, int)
for obs in datos:
    f_obs[obs] += 1
# print("f_obs: ", f_obs)

# Estadistico de prueba
T = 0
for i in range(k):
    T += ((f_obs[i] - n * p[i])**2) / (n*p[i])

# print("T: ", T)
print('p-valor con chi2: ' , '{:.5f}'.format(1-chi2.cdf(T, k-1-1))) # k-2=7

# Haciendo una simulacion
def sim(Nsim=10000):
    datos = np.zeros(n, int) # Muestra simulada
    N = np.zeros(k, int) # Frecuencias observadas en la simulacion N_i
    p_est = 0.6180555555555556
    p_valor = 0
    T = 31.499330934155324

    for _ in range(Nsim):

        # Simular las frecuencias
        datos = np.zeros(n, int)
        for j in range(n):
            datos[j] = binom.rvs(8, p_est)
        N*=0 # Frecuencias observadas en la simulacion
        for obs in datos:
            N[obs] += 1
        if sum(N) != n: # Deben ser n observaciones en total
            break

        # Estimacion de p para una Binomial(8, p)
        p_est_sim = (sum(datos)/len(datos)) / 8

        # Estadistico de prueba simulado
        # Probabilidades teoricas p_i estimadas para el Estadistico de Prueba simulado
        prob_sim = np.zeros(k) #k=9
        for i in range(8):
            aux = factorial(8)/(factorial(i)*factorial(8-i))
            prob_sim[i] = aux * (p_est_sim**i) * ((1-p_est_sim)**(8-i))
        prob_sim[8] = 1 - sum(prob_sim)
        
        T_sim = 0
        for i in range(k):
            T_sim += ((N[i] - n * prob_sim[i])**2) / (n*prob_sim[i])
        
        if T_sim >= T:
            p_valor += 1

    p_valor /= Nsim
    return p_valor

print('p-valor simulado: ', sim())
# print("test de Kolmogorov-Smirnov: ", kstest(datos, 'binom', args=(8, p_est)))
