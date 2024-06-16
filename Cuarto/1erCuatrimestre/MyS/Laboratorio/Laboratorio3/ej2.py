import random

def X() -> float:
    u: float = random.random()
    w1: float = random.random()
    w2: float = random.random()
    if u < 1/2:
        return w1 + w2
    else:
        w3: float = random.random()
        return w1 + w2 + w3


def P_ganar(n) -> float:
    prob: int = 0
    for _ in range(n):
        if X() >= 1:
            prob += 1

    return prob/n


N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
    print('Probabilidad de asertar para Nsim =',N[i])
    print(P_ganar(N[i]))

""" 
import numpy as np


w = np.zeros((200))
for _ in range(10000000):
    x = random.random() + random.random()
    x = floor(x*100)
    w[x] += 1

import matplotlib.pyplot as plt
plt.plot([])
plt.show() 
"""
