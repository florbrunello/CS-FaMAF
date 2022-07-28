"""
Ejercicio 2: 
Maximizar la función x + y en la siguiente región:
    50x + 24y ≤ 2400
    30x + 33y ≤ 2100.
Graficar la región factible y las curvas de nivel de la función.
"""

import matplotlib.pyplot as plt
import numpy as np

#Creo un arreglo de 100 elementos equiespaciados entre 0 y 50
x = np.linspace(0,50,100)

y1 = (2400 - 50*x)/24
y2 = (2100 - 30*x)/33

#Comparo los 100 puntos de las rectas y1 e y2
restricciones = np.minimum(y1,y2)
restricciones = np.maximum(restricciones,0)

plt.plot(x,y1)
plt.plot(x,y2)
plt.fill_between(x,y1,alpha=0.5)
plt.fill_between(x,y2,alpha=0.5)
plt.show()