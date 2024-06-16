from math import erf, exp, log, sqrt
from scipy.stats import norm, kstest
import numpy as np
import random
import math

datos = np.array([91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7])
n = len(datos)
media_est = sum(datos)/n
sigma_est = sqrt(sum((datos - media_est)**2) / (n-1))

def norm_acumulada(x, media_est, sigma_est): 
    r = norm.cdf(x, media_est, sigma_est)
    return r

def K_S_Normal(datos, media_est, sigma_est):
    n = len(datos)
    datos.sort()
    d=0
    for j in range(n):
        x = datos[j]
        d = max(d, (j+1)/n-norm_acumulada(x, media_est, sigma_est), norm_acumulada(x, media_est, sigma_est)-j/n )
    return d

d_KS_est = K_S_Normal(datos, media_est, sigma_est)

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

print('p-valor simulado: ', sim())
# print('p-valor: ', kstest(datos, 'norm', args=(media_est, sigma_est)).pvalue)
