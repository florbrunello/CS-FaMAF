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

# Inciso B

# Importamos nuestra implementación de bisección
from ej1 import rbisec

def fun_labej2b(x):
    """
    Función que nos devuelve la raíz cuadrada de x menos 3, 
    para encontrar x**2 = 3.
    """
    return x**2 - 3

# Obtenemos nuestro historial de puntos y evaluaciones
hx, hf = rbisec(fun_labej2b, [0,2], 1e-5, 100)
# Imprimimos en pantalla el último valor de x
print(f"La aproximacion de la raíz de 3 obtenida es {hx[-1]}")

# Inciso C

# Importamos el módulo de gráficos de matplotlib
import matplotlib.pyplot as plt

hx, hf = rbisec(fun_labej2b, [0,2], 1e-5, 100)
hx2, hf2 = rbisec(fun_labej2b, [-2,0],1e-5, 100)

# Graficamos el historial de puntos con marcador estrella
plt.plot(hx, hf, '*',label="Puntos medios[0,2]")
plt.plot(hx2, hf2, '*',label="Puntos medios[-2,0]")

# Creamos una lista de 21 puntos equiespaciados entre 0 y 2 y sus valores:
# puntos = [-2, -1.9 , ... , -0.1 , 0]
# evals = [f(-2), f(-1.9), ..., f(-0.1), f(0)]
puntos = [-2]
evals = [fun_labej2b(-2)]
for jdx in range(-21, 1):
    puntos.append(jdx * 0.1)
    evals.append(fun_labej2b(jdx * 0.1))

# Graficamos puntos en X y evals en Y
plt.plot(puntos, evals)

# Creamos una lista de 21 puntos equiespaciados entre 0 y 2 y sus valores:
# puntos = [0, 0.1, 0.2, ... , 1.9, 2]
# evals = [f(0), f(0.1), ..., f(1.9), f(2)]
puntos2 = [0]
evals2 = [fun_labej2b(0)]
for idx in range(1, 21):
    puntos2.append(idx * 0.1)
    evals2.append(fun_labej2b(idx * 0.1))

# Graficamos puntos en X y evals en Y
plt.plot(puntos2, evals2)

# Marco el punto final con un círculo negro, para mejorar la visualización.
plt.plot(hx[-1], hf[-1], 'ok')
plt.plot(hx2[-1], hf2[-1], 'ok')

# Le doy un título al gráfico.
plt.title("Puntos Visitados - Grafico B")

# Muestro lo que digan los labels
plt.legend()

# Mostramos ambos gráficos al mismo tiempo
plt.show()
