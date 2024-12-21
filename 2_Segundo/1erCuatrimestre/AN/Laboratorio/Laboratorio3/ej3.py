"""
Ejercicio 3: 
Considerar la funcion f tal que f(x) = 1/x. Utilizando el ejercicio anterior, 
graficar en una misma figura f y p que interpole {(i, f(i))} i = 1,...,5, 
usando para ambas los puntos equiespaciados z_j = 24/25 + j/25, j = 1,...,101.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from ej1 import ilagrange

x = [1, 2, 3, 4, 5]
y = [1, 1/2, 1/3, 1/4, 1/5]

# Genero 101 puntos entre 1 y 5
z = np.linspace(1, 5, 101)

# Aplico operaciones aritméticas a toda la lista
f_z = 1 / z

# Calculo el polinomio de lagrange en z
w = ilagrange(x, y, z)

plt.plot(z, f_z, label="f(z)")
plt.plot(z, w, label="p(z)")
plt.plot(x, y, "*", label="Puntos")
plt.legend()
plt.show()