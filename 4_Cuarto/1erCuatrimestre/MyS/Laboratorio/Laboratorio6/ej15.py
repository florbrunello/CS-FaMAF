from scipy.stats import kstest
from math import exp, log
import numpy as np
import random

datos = np.array([1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7])
n = len(datos) # n = 15 Tamaño de la muestra
lamda_est = n/sum(datos) # Estimador de lamda

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

d_KS_est = K_S_Exp(datos, lamda_est)

def sim(Nsim=10000, d_KS=d_KS_est): 
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

# print("D = ", d_KS_est)
print("p-valor = ", sim())
print(" Con un IC del 95% tenemos que 0.19 es mayor que 0.05, por lo que no se rechaza la hipotesis nula")
print(" Con un IC del 99% tenemos que 0.19 es mayor que 0.01, por lo que no se rechaza la hipotesis nula")
# print("test de Kolmogorov-Smirnov: ", kstest(datos, 'expon', args=(0, 1/lamda_est)))