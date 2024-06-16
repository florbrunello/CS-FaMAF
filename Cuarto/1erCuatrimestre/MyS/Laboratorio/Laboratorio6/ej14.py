from random import gammavariate, gauss
from scipy.stats import kstest
from math import erf, sqrt
import numpy as np

# Estadistico de Prueba
def norm_acumulada(x): 
    if x >= 0:
        F_i = erf(x/sqrt(2.))/2. + 0.5
    else:
        F_i = 0.5 - erf(-x/sqrt(2.))/2.
    return F_i

def K_S_Normal(datos):
    n = len(datos)
    datos.sort()
    d=0
    for j in range(n):
        x = datos[j]
        d = max(d, (j+1)/n-norm_acumulada(x), norm_acumulada(x)-j/n )
    return d

# Generar valores de una t-student
def rt(df): # df grados de libertad
    x = gauss(0.0, 1.0)
    y = 2.0*gammavariate(0.5*df, 2.0)
    return x / (sqrt(y/df))

# Ejercicio a
def sim(Nsim=10000):
    df = 11
    print("n\t  ", "D\t  ", "p-valor")
    muestras_n = [10, 20, 100, 1000]
    for n in muestras_n:
        datos = np.empty(n)
        for i in range(n):
            datos[i] = rt(df)
        D = K_S_Normal(datos)
    
        p_valor = 0
        for _ in range(Nsim):
            uniformes = np.random.uniform(0,1,n)
            uniformes.sort()
            d_j = 0
            for j in range(n):
                u_j = uniformes[j]
                d_j = max(d_j, (j+1)/n-u_j, u_j-j/n)
            
            if d_j >= D:
                p_valor += 1

        p_valor /= Nsim
        print(n, "\t", D, "\t", p_valor)
        #print("Test de Kolmogorov-Smirnov: ", kstest(datos, 'norm'))

sim()

# Ejercicio b
def sim2():
    df = 11
    print("n\t  ", "D\t  ", "p-valor", "Nsim")
    muestras_n = [10, 20, 100, 1000]
    for n in muestras_n:
        datos = np.empty(n)
        for i in range(n):
            datos[i] = rt(df)
        D = K_S_Normal(datos)    
    
        L = 0.01 # Amplitud del intervalo
        z_alpha_2 = 1.96 # 95% de confianza
        d = L/(2*z_alpha_2)
        Nsim = 0
        p_valor = 0
        while Nsim <= 100 or sqrt(1/Nsim) >= d:
            Nsim += 1
            uniformes = np.random.uniform(0,1,n)
            uniformes.sort()
            d_j = 0
            for j in range(n):
                u_j = uniformes[j]
                d_j = max(d_j, (j+1)/n-u_j, u_j-j/n)
            
            if d_j >= D:
                p_valor += 1

        p_valor /= Nsim
        print(n, "\t", D, "\t", p_valor, "\t", Nsim)

sim2()