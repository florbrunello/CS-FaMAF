import random
import math

# Generacion de un Proceso de Poisson Homogeneo
def poisson_homogeneo(lamda, T):
    eventos = []
    t = -math.log(1 - random.random()) / lamda
    while t <= T:
        eventos.append(t)
        t += -math.log(1 - random.random()) / lamda
    return len(eventos), eventos

print(poisson_homogeneo(1, 10))
# (5, [0.14760614830696817, 3.4435780343967886, 4.408026890314264, 
# 5.21918983557668, 8.265563491730635])
# X1, X1+X2, X1+X2+X3, X1+X2+X3+X4, X1+X2+X3+X4+X5 = tiempos de arribo en primeras 10 unidades de tiempo
# 4 eventos en total