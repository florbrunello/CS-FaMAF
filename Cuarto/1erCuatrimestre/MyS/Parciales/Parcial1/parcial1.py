# Parcial 1: Brunello, Florencia

import random
import math

def ejercicio3():

    # Integral Monte Carlo en el intervalo (0,inf)
    def MonteCarlo_inf(fun, Nsim):
        Integral=0
        for _ in range(Nsim):
            u=random.random()
            Integral+= fun(1/u-1)/(u**2)
        return Integral/Nsim

    def fun(u):
        return 1 / ( ((u+1)**2) * (math.log(u+2))  )
    
    N = [1000,10000,100000]
    for i in range(len(N)):
        print('Integral para Nsim =',N[i])
        print(f"   {MonteCarlo_inf(fun, N[i]):.6f}")

if __name__ == "__main__":
    ejercicio3()

