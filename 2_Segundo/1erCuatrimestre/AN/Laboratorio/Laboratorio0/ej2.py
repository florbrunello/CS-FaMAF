import random

def suma_aleatorio(Tol):
    s = 0
    contador = 0

    while (s <= Tol):

        s = s + random.random()
        contador = contador + 1

    return s, contador

print(suma_aleatorio(3))