from scipy.stats import kstest
from random import random
import numpy as np

datos = np.array([0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74])
n = len(datos) # Tamaño de la muestra

# Estadistico de Prueba
def K_S_Uniforme(datos):
    datos = np.array([0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74])
    n = len(datos)
    datos.sort()
    d = 0
    for j in range(n):
        x = datos[j]
        d = max(d, (j+1)/n-x, x-j/n)
    return d

d_KS = K_S_Uniforme(datos)

# Simulacion
def sim(Nsim=10000, d_KS=d_KS): 
    p_valor = 0
    for _ in range(Nsim):
        uniformes = np.random.uniform(0,1,n)
        uniformes.sort()
        d_j = 0
        for j in range(n):
            u_j = uniformes[j]
            d_j = max(d_j, (j+1)/n-u_j, u_j-j/n)
        
        if d_j >= d_KS:
            p_valor += 1

    p_valor /= Nsim
    return p_valor

#print("Estimador de Kolmogorov-Smirnov: ", d_KS)
print("p-valor: ", sim())
#print("test de Kolmogorov-Smirnov: ", kstest(datos, 'uniform'))
# Estimador de kolmogorv-Sminrov D = 0.24
# p-valor simulado = 0.5324
