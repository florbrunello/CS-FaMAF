import numpy as np
import random

def queDevuelve(p1,p2):
    X = int(np.log(1-random.random())/np.log(1-p1))+1
    Y = int(np.log(1-random.random())/np.log(1-p2))+1
    return min(X,Y)

def geometrica(p):
    u = random.random()
    return int(np.log(1-u)/np.log(1-p))+1

print(queDevuelve(0.05, 0.2))
p_0 = 1 - (1-0.5)*(1-0.2)
print(geometrica(p_0))