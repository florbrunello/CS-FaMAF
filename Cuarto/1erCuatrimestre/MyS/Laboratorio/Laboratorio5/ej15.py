import random
import math

# Ejercicio a
def poisson_NH_adelgazamiento(lamda_t, lamda, T):
    eventos = []
    t = -math.log(1 - random.random()) / lamda
    while t <= T:
        U = random.random()
        if U <= lamda_t(t) / lamda: 
            eventos.append(t)
        t += -math.log(1 - random.random()) / lamda
    return eventos

def lamda_i(t): 
    if 0 <= t and t <= 3:
        return (3 + 4/(t+1))
    else:
        return 0

def lamda_ii(t): 
    if 0 <= t and t <= 5:
        return (t-2)**2-5*t+17
    else:
        return 0

def lamda_iii(t):
    if 2 <= t and t <= 3: 
        return t/2 -1
    elif 3 < t and t <= 6:
        return 1 - t/6
    else:
        return 0

# Ejercicio b
def poisson_adelgazamiento_mejorado(intervalos, lamda_t, lamda, T): 
    j = 0
    t = -math.log(1 - random.random()) / lamda[j]
    NT = 0
    eventos = []
    while t <= T:
        if t <= intervalos[j]:
            V = random.random()
            if V < lamda_t(t) / lamda[j]:
                NT += 1
                eventos.append(t)
            t += -math.log(1 - random.random()) / lamda[j]
        else:  
            t = intervalos[j] + (t - intervalos[j]) * lamda[j] / lamda[j+1]
            j += 1
    return NT, eventos

def b_i():
    # [0,1] (1,2] (2,3]
    intervalos = [1, 2, 3]
    lamda = [7, 5, 13/3]
    return poisson_adelgazamiento_mejorado(intervalos, lamda_i, lamda, 3)

def b_ii():
    # [0,1] (1,2] (2,3] (3,4] (4,5]
    intervalos = [1, 2, 3, 4, 5]
    lamda =  [21, 13, 7, 3, 1]
    return poisson_adelgazamiento_mejorado(intervalos, lamda_ii, lamda, 5)

def b_iii():
    # [2,3] (3,4] (4,5] (5,6]
    intervalos = [3, 4, 5, 6]
    lamda = [0.5, 0.5, 1/3, 1/6]
    return poisson_adelgazamiento_mejorado(intervalos, lamda_iii, lamda, 6)
    
def main():
    print("Adelgazamiento de Poisson No Homogeneo")
    print("Ejercicio a i: ", poisson_NH_adelgazamiento(lamda_i, 7, 3))
    print("Ejercicio a ii: ", poisson_NH_adelgazamiento(lamda_ii, 21, 5))
    print("Ejercicio a iii: ", poisson_NH_adelgazamiento(lamda_iii, 0.5, 6))
    
    print("Adelgazamiento Mejorado de Poisson No Homogeneo")
    print("Ejercicio b i: ", b_i())
    print("Ejercicio b ii: ", b_ii())
    print("Ejercicio b iii: ", b_iii())
    
if __name__ == "__main__":
    main()