from random import random 
import math

# Ejercicio a
def MonteCarlo_01(fun, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(random())
    return Integral/Nsim

def MonteCarlo_inf(fun, Nsim):
    Integral=0
    for _ in range(Nsim):
        u=random()
        Integral+= fun(1/u-1) / (u**2)
    return Integral/Nsim

def g(u):
  return math.exp((1-u)) / math.sqrt(2*(1-u))

def h(u):
  # Es una funcion par
  return 2 * (u**2) * math.exp(-u**2)

#Ejercicio b
def media_muestal_X_i(d, fun): 
    media = fun(random())
    scuad, n = 0, 1
    while n <= 100 or math.sqrt(scuad/n) > d: 
        n += 1
        X = fun(random())
        mediaAnt = media 
        media = media + (X - media)/n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
    return media 

def media_muestal_X_ii(d, fun): 
    u = random()
    media = fun(1/u-1) / (u**2)
    scuad, n = 0, 1
    while n <= 100 or math.sqrt(scuad/n) > d: 
        n += 1
        u = random()
        X = fun(1/u-1) / (u**2)
        mediaAnt = media 
        media = media + (X - media)/n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
    return media 

def main():
    Nsim = 100000
    print("Integral de g(u) = ", MonteCarlo_01(g, Nsim))
    print("Integral de h(u) = ", MonteCarlo_inf(h, Nsim))

    d = 0.01
    print("Estimacion del valor esperado con ECM < d = ", media_muestal_X_i(d, g))
    print("Estimacion del valor esperado con ECM < d = ", media_muestal_X_ii(d, h))

if __name__ == "__main__":
    main()
    