"""
Ejercicio 2: 
Visualizar mediante un grafico la funcion f en el intervalo [0, 6.4], para una lista
de puntos equidistantes separados por una distancia de 0.01 entre si (sin utilizar la
libreria numPy).
"""

from Ejercicio1 import serie_seno
import matplotlib.pyplot as plt

x = [0.01 * i for i in range(0, 640)]
y = [serie_seno(0.01 * xi) for xi in range(0,640)]
plt.plot(x, y)
plt.title("Serie de Taylor del Seno alrededor del cero")
plt.show()

"""
Instrucciones de ejecución: 

Para conseguir el grafico de la funcion entre 0 y 6.4 debo crear muchos puntos
equiespaciados en ese intervalo, para ello uso range y multiplico.
Para ejecutar el archivo basta con ir a la terminal y cargar el mismo. 
"""