# Brunello, Florencia - Parcial 3 - 13/06/2024 #

from scipy.stats import chi2, binom, norm, kstest
from math import factorial, exp, sqrt
from random import random
import numpy as np

# Ejercicio 2

def ejercicio2():
    datos = np.array([1.628, 1.352, 1.800, 1.420, 1.594, 2.132, 1.614, 1.924, 1.692])
    datos.sort()
    n = 9 
    media_est = sum(datos)/n
    sigma_est = sqrt(sum((datos - media_est)**2)/(n-1))
    print("Media y Sigma estimados", media_est, sigma_est)

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
    print("D = ", d_KS_est)

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

    p_valor = sim()
    if p_valor < 0.04:
        print("Rechazo la hipótesis nula")
    else:
        print("No hay evidencia para rechazar la hipótesis nula")

    def muestra(d_KS=d_KS_est, n=9):
        uniformes = np.array([0.23, 0.12, 0.45, 0.67, 0.01, 0.51, 0.38, 0.92, 0.84])
        uniformes.sort()
        d_j = 0
        for j in range(n):
            u_j = uniformes[j]
            d_j = max(d_j, (j+1)/n-u_j, u_j-j/n)
            
        return d_j
    
    D_u = muestra()
    print("D de la muestra: ", D_u)
    if D_u >= d_KS_est:
        print("El estadistico de la muestra resulta mayor")
    else:
        print("El estadistico de la muestra resulta menor")

# Ejercicio 3

def ejercicio3():
    f_obs = np.array([490, 384, 111, 15])
    datos = [0] * 490 + [1] * 384 + [2] * 111 + [3] * 15
    n = sum(f_obs)
    k = 4 
    p_est = (sum(datos)/len(datos)) / 3

    print("p estimado: ", p_est)

    # Probabilidades teoricas p_i 
    p = np.zeros(k)
    for i in range(3):
        p[i] = binom.pmf(i, 3, p_est)
    p[3] = 1 - sum(p)

    # Estadistico de prueba
    T = 0
    for i in range(k):
        T += ((f_obs[i] - n * p[i])**2) / (n*p[i])

    print("Estadistico T: ", T)
    print('p-valor con chi2: ' , '{:.5f}'.format(1-chi2.cdf(T, k-1-1)))

    # Haciendo una simulacion
    def sim(Nsim=1000, n = n, k = k):
        datos = np.zeros(n, int) # Muestra simulada
        N = np.zeros(k, int) # Frecuencias observadas en la simulacion N_i
        p_est = 0.217
        p_valor = 0
        T = 3.018118522843555

        for _ in range(Nsim):

            # Simular las frecuencias
            datos = np.zeros(n, int)
            for j in range(n):
                datos[j] = binom.rvs(3, p_est)
            N*=0 # Frecuencias observadas en la simulacion
            for obs in datos:
                N[obs] += 1
            if sum(N) != n: # Deben ser n observaciones en total
                break

            # Estimacion de p para una Binomial(3, p)
            p_est_sim = (sum(datos)/len(datos)) / 3

            # Estadistico de prueba simulado
            # Probabilidades teoricas p_i estimadas para el Estadistico de Prueba simulado
            prob_sim = np.zeros(k)
            for i in range(3):
                prob_sim[i] = binom.pmf(i, 3, p_est_sim)
            prob_sim[3] = 1 - sum(prob_sim)
            
            T_sim = 0
            for i in range(k):
                T_sim += ((N[i] - n * prob_sim[i])**2) / (n*prob_sim[i])
            
            if T_sim >= T:
                p_valor += 1

        p_valor /= Nsim
        return p_valor

    p_val = sim()
    print('p-valor simulado: ', p_val)

# Ejercicio 4

def ejercicio4():

    def MonteCarlo_inf(fun, Nsim):
        Integral=0
        for _ in range(Nsim):
            u=random()
            Integral+= fun(1/u-1)/(u**2)
        return Integral/Nsim

    def fun(u): 
        return u / (1+u**4)
    
    def media_muestral_IC_X(fun, z_alpha_2=1.96, L=2*0.001):
        d = L / (2 * z_alpha_2)
        u = random()
        media = fun(1/u-1)/(u**2)
        scuad, n = 0, 1
        while n <= 100 or sqrt(scuad/n) > d: 
            n += 1
            u = random()
            X = fun(1/u-1)/(u**2)
            mediaAnt = media 
            media = mediaAnt + (X - mediaAnt) / n
            scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
        return media, scuad, n


    def media_muestal_Y(fun, Nsim):
        u = random()
        media = fun(1/u-1)/(u**2)
        scuad = 0
        sample = [media]
        for i in range(2, Nsim):
            u = random()
            X = fun(1/u-1)/(u**2)
            sample.append(X)
            mediaAnt = media 
            media = mediaAnt + (X - mediaAnt) / i
            scuad = scuad * (1 - 1/(i-1)) + i*(media - mediaAnt)**2
        return media, scuad, sample

    print("\nIntegral")
    print("Monte Carlo: ", MonteCarlo_inf(fun, 10000))
    print("n  |         I       |        S        |        IC(95%)      ")
    print("--------------------------------------------------")
    data = media_muestral_IC_X(fun)
    n = data[2]
    media = round(data[0], 4)
    s = round(sqrt(data[1]), 4)
    IC = []
    IC.append(round(data[0]-1.96*sqrt(data[1]/n), 4))
    IC.append(round(data[0]+1.96*sqrt(data[1]/n), 4))
    print(f"{n}  | {media} | {s} | ({IC[0]},{IC[1]})")

    Nsim = [1000, 5000, 7000]
    for i in Nsim:
        data = media_muestal_Y(fun, i)
        media = round(data[0], 4)
        s = round(sqrt(data[1]), 4)
        IC = []
        IC.append(round(data[0]-1.96*sqrt(data[1]/i), 4))
        IC.append(round(data[0]+1.96*sqrt(data[1]/i), 4))
        print(f"{i}  | {media} | {s} | ({IC[0]},{IC[1]})")
    print("--------------------------------------------------")

print("Ejercicio 2")
ejercicio2() 
print("Ejercicio 3")
ejercicio3()
print("Ejercicio 4")
ejercicio4()
