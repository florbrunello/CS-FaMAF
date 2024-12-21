from typing import Literal, Tuple
import random

"""
El parametro de exporiate es la MEDIA (no el LAMBDA) 
OJO <= al ver las u y generar random.expovariate !
"""

print("Ejercicio a")

def E() -> float:
    u: float = random.random()
    if u <= 0.4:                        # Va a la caja 1
        return random.expovariate(1/3)
    elif u <= 0.72:                     # Va a la caja 2
        return random.expovariate(1/4)
    else:                               # Va a la caja 3
        return random.expovariate(1/5)

def P_esperar_menos_4() -> float:
    n: int = 10000
    wins: int = 0
    for _ in range(n):
        if E() <= 4:
            wins += 1

    return wins/n

print(P_esperar_menos_4())


print("Ejercicio b")

def caja_E() -> Tuple[Literal[1, 2, 3], float]:
    u: float = random.random()
    if u <= 0.4:
        return 1, random.expovariate(1/3)
    elif u <= 0.72:
        return 2, random.expovariate(1/4)
    else:
        return 3, random.expovariate(1/5)

def P_caja_talque_espero_menos_4(caja: Literal[1, 2, 3]) -> float:
    n: int = 1000
    successes: int = 0
    fails: int = 0

    while fails + successes < n:
        s_caja, tiempo = caja_E()
        if tiempo > 4:
            if s_caja == caja:
                successes += 1
            else:
                fails += 1

    return successes/n

print(P_caja_talque_espero_menos_4(1))
print(P_caja_talque_espero_menos_4(2))
print(P_caja_talque_espero_menos_4(3))
