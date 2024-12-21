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

## Curvas de Nivel

levels = np.linspace(40,80,5)

for level in levels:
	# x+y = level
	y = level - x
	plt.plot(x,y,label=f"nivel={level}")

plt.fill_between(x,restricciones,alpha=0.3)
plt.grid()
plt.legend()
plt.show()