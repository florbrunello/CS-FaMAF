from scipy.stats import kstest
from math import exp
import numpy as np
import random

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

#Muestra de n exponenciales con lamda = 1
lamda = 1 # Parametro lamda
n = 30
datos = [-np.log(1-random.random()) for _ in range(n)]
datos.sort()

# Estadistico de prueba
d = K_S_Exp(datos, lamda)
# print("Estadistico de prueba: ", d)

def sim(Nsim=1000, n=30, d_KS=d):
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

"""
Estadistico de prueba:  0.14419415002324565
No se rechaza la hipotesis nula
Estadistico de prueba:  0.1456435311091323
No se rechaza la hipotesis nula
p-valor simulado:  0.5
"""
print("p-valor simulado: ", sim(10000, 30))
# print("Test de Kolmogorov-Smirnov: ", kstest(datos, 'expon', args=(0, 1/lamda)))
