from random import random 
import math

def MonteCarlo_ab(fun, a, b, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(a + (b-a)*random())
    return Integral*(b-a)/Nsim 

def MonteCarlo_inf(fun, Nsim):
    Integral=0
    for _ in range(Nsim):
        u=random()
        Integral+= fun(1/u-1)/(u**2)
    return Integral/Nsim

def fun_i(u):
  return math.sin(u)/u

def fun_ii(u):
    return 3/(3+u**4)

# Ejercicio a
def media_muestral_IC_X_i(fun, a, b, z_alpha_2=1.96, L=2*0.001):
    d = L / (2 * z_alpha_2)
    media = fun(a + (b-a)*random())*(b-a)
    scuad, n = 0, 1
    while n <= 100 or math.sqrt(scuad/n) > d: 
        n += 1
        X = fun(a + (b-a)*random())*(b-a)
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
    return media, scuad, n

def media_muestral_IC_X_ii(fun, z_alpha_2=1.96, L=0.001):
    d = L / (2 * z_alpha_2)
    u = random()
    media = fun(1/u-1)/(u**2)
    scuad, n = 0, 1
    while n <= 100 or math.sqrt(scuad/n) > d: 
        n += 1
        u = random()
        X = fun(1/u-1)/(u**2)
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
    return media, scuad, n

# Ejercicio c
def media_muestal_Y_i(fun, a, b, Nsim):
    media = fun(a + (b-a)*random())*(b-a)
    scuad = 0
    sample = [media]
    for i in range(2, Nsim):
        X = fun(a + (b-a)*random())*(b-a)
        sample.append(X)
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / i
        scuad = scuad * (1 - 1/(i-1)) + i*(media - mediaAnt)**2
    return media, scuad, sample

def media_muestal_Y_ii(fun, Nsim):
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

def main(): 

    print("Integral i")
    print("Monte Carlo: ", MonteCarlo_ab(fun_i, math.pi, 2*math.pi, 1000))
    print("n  |         I       |        S        |        IC(95%)      ")  
    print("--------------------------------------------------")
    data = media_muestral_IC_X_i(fun_i, math.pi, 2*math.pi)
    n = data[2]
    media = round(data[0], 4)
    s = round(math.sqrt(data[1]), 4)
    IC = []
    IC.append(round(data[0]-1.96*math.sqrt(data[1]/data[2]), 4))
    IC.append(round(data[0]+1.96*math.sqrt(data[1]/data[2]), 4))
    print(f"{n}  | {media} | {s} | ({IC[0]},{IC[1]})")

    Nsim = [1000, 5000, 7000]
    for i in Nsim:
        data = media_muestal_Y_i(fun_i, math.pi, 2*math.pi, i)
        media = round(data[0], 4)
        s = round(math.sqrt(data[1]), 4)
        IC = []
        IC.append(round(data[0]-1.96*math.sqrt(data[1]/i), 4))
        IC.append(round(data[0]+1.96*math.sqrt(data[1]/i), 4))
        print(f"{i}  | {media} | {s} | ({IC[0]},{IC[1]})")
    print("--------------------------------------------------")
    
    print("\nIntegral ii")
    print("Monte Carlo: ", MonteCarlo_inf(fun_ii, 1000))
    print("n  |         I       |        S        |        IC(95%)      ")
    print("--------------------------------------------------")
    data = media_muestral_IC_X_ii(fun_ii)
    n = data[2]
    media = round(data[0], 4)
    s = round(math.sqrt(data[1]), 4)
    IC = []
    IC.append(round(data[0]-1.96*math.sqrt(data[1]/n), 4))
    IC.append(round(data[0]+1.96*math.sqrt(data[1]/n), 4))
    print(f"{n}  | {media} | {s} | ({IC[0]},{IC[1]})")

    Nsim = [1000, 5000, 7000]
    for i in Nsim:
        data = media_muestal_Y_ii(fun_ii, i)
        media = round(data[0], 4)
        s = round(math.sqrt(data[1]), 4)
        IC = []
        IC.append(round(data[0]-1.96*math.sqrt(data[1]/i), 4))
        IC.append(round(data[0]+1.96*math.sqrt(data[1]/i), 4))
        print(f"{i}  | {media} | {s} | ({IC[0]},{IC[1]})")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
