"""
Ejercicio 2: 

Utilizar la funcion rbisec para:
a) Encontrar la menor solucion positiva de la ecuacion 2x = tan(x) con un error menor
a 10-5 en menos de 100 iteraciones. ¿Cuantas iteraciones son necesarias cuando comenzamos 
con el intervalo [0.8, 1.4]? Usar la siguiente sintaxis:
hx, hy = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)

b) Encontrar una aproximacion a √3 con un error menor a 10-5. Para esto, considere
la funcion x 7→ x 2 - 3 (que debe llamarse fun_lab2ej2b).

c) Graficar conjuntamente f y los pares (xk, f(xk)) para las dos funciones anteriores y
con al menos dos intervalos iniciales distintos para cada una.
"""

# Inciso A

from ej1 import rbisec
from math import tan

def fun_labej2a(x):
    return tan(x) - 2*x

# Obtengo el historial de puntos visitados
hx, hf = rbisec(fun_labej2a, [0.8, 1.4], 100, 1e-5)
print(f"Son necesarias {len(hx)} iteraciones")
print(hx)

# Inciso C
import matplotlib.pyplot as plt
import numpy as np

hx, hf = rbisec(fun_labej2a, [0.8, 1.4], 100, 1e-5)
hx2, hf2 = rbisec(fun_labej2a, [4.5, 4.7], 100, 1e-5)

#   OPCION 1

# Creamos una lista de 21 puntos equiespaciados entre 0 y 2 y sus valores:
# puntos = [0, 0.1, 0.2, ... , 1.9, 2]
# evals = [f(0), f(0.1), ..., f(1.9), f(2)]
puntos = [0]
evals = [fun_labej2a(0)]
for idx in range(1, 60):
    puntos.append(idx * 0.1)
    evals.append(fun_labej2a(idx * 0.1))

# Graficamos puntos en X y evals en Y
plt.plot(puntos, evals, label="f(x) = tan(x)-2x")

#   OPCION 2

#x = np.linspace(0,8,120)
#plt.plot(x,np.tan(x)-(2*x),"g", label="f(x) = tan(x)-2x")

# Grafico el historial de puntos visitados, con asteriscos.
plt.plot(hx, hf, '*',label="Puntos medios[0.8,1.4]")
plt.plot(hx2,hf2,'*',label="Puntos medios[4.5,4.7]")

# Marco el punto final con un círculo negro, para mejorar la visualización.
plt.plot(hx[-1], hf[-1], 'ok')
plt.plot(hx2[-1], hf2[-1], 'ok')

# Le doy un título al gráfico.
plt.title("Puntos Visitados - Grafico A")

# Muestro lo que digan los labels
plt.legend()

# Muestro el gráfico.
plt.show()