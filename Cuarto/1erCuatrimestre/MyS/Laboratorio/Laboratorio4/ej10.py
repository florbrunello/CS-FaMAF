from scipy.stats import geom
import numpy as np
import random

def P(j): 
    return 0.5**(j+1) + ((0.5 * (2**(j-1))) / 3**j) 

def geometrica(p):
    u = random.random()
    return int(np.log(1 - u) / np.log(1-p)) + 1

def X(): 
    U = random.random()
    if U < 0.5:
        return geometrica(1/2)
    else:
        return geometrica(1/3)
    
def est_E(X, Nsim):
    e = 0 
    for _ in range(Nsim):
        e += X()
    return e / Nsim

def est_E2(X, Nsim):
    e = 0 
    for _ in range(Nsim):
        e += 0.5 * geom.mean(0.5) + 0.5 * geom.mean(1/3)
    return e / Nsim

def main(): 
    Nsim = 1000
    print("E(X) ≃ ", est_E(X, Nsim))
    print("E(X) ≃ ", est_E2(X, Nsim))
    print("E(X) = 2.5")

if __name__ == '__main__':
    main()    
