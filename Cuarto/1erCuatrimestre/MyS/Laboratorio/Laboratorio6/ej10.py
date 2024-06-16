from scipy.stats import kstest
from math import exp, log
import numpy as np
import random

datos = np.array([86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99])
n = len(datos) # Tamaño de la muestra
lamda = 1/50 # Parametro lamda

# Estadistico de Prueba
def F_exponencial(x, lamda):
    return 1-exp(-x*lamda)

def K_S_Exp(datos, lamda):
    n = len(datos)
    datos.sort()
    d=0
    for j in range(n):
        x = datos[j]
        # Usar acumulada de una exponencial
        d = max(d, (j+1)/n-F_exponencial(x, lamda), F_exponencial(x, lamda)-j/n )
    return d

d_KS = K_S_Exp(datos, lamda)

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

# D = 0.392254455
# print("D = ", d_KS) 
# p-valor = 0.0249
print("p-valor = ", sim())
# print("test de Kolmogorov-Smirnov: ", kstest(datos, 'expon', args=(0, 1/lamda)))
