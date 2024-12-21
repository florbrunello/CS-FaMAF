from random import random

def valorPi(Nsim): 
    enCirculo = 0
    for _ in range (Nsim):
        u = 2 * random() - 1
        v = 2 * random() - 1
        if u**2 + v**2 <= 1:
            enCirculo += 1
    return 4 * enCirculo / Nsim

N = [1000,10000,100000]
for i in range(len(N)):
    print('Nsim =',N[i])
    print(f"   {valorPi(N[i]):.4f}")
    
