"""
Ejercicio 4: 
Italia fue el pais mas afectado por el Coronavirus, comenzando con 14 casos 
desde el 22 de febrero de 2020 y con una cantidad de infectados que crecio
exponencialmente por mas de un mes. Obtener los datos almacenados en el 
archivo covid_italia.csv y realizar un ajuste exponencial de la forma
y(x) = a*(e ** (bx)). Realizar un grafico que contenga los datos y su ajuste.
"""

import matplotlib.pyplot as plt
import numpy as np

#Leo los datos del archivo: unicamente la cantidad de casos 
    #Delimiter: delimitador para usar para analizar el contenido del archivo txt.
    #Usecols: índices de la columna que se leerán.
y_casos = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/covid_italia.csv',delimiter=",", usecols=1)

#Genero una lista del 1 a la cantidad de casos (eje x)
x = [i for i in range(len(y_casos))]

"""
Ajuste exponencial: transformo la expresion para realizar un ajuste lineal de la forma
y(x) = a*(e ** (bx))
ln(y) = ln (a*(e ** (bx)))
ln(y) = ln(a) + bx 

ln(a) = e ^ ln(a) = a
b = b
"""

#Actualizo la tabla de datos y -> ln(y)
y_log = np.log(y_casos)

#Obtengo los coeficientes del polinomio que ajusta los datos con un polinomio de grado 1 (modelo lineal)
coefs = np.polyfit(x,y_log,1)
y_plot = np.polyval(coefs, x)

b = coefs[0]
log_a = coefs[1]
a = np.exp(log_a)

print(f'Coeficiente A = {a}, Coeficiente B = {b}.')

#No puedo plotear (x, a * np.exp(b*x)) pues x es una lista y b un numero
y_plot_exp = [a * np.exp(b*xi) for xi in x]

#Grafico los datos del archivo y el ajuste obtenido
plt.plot(x,y_casos,'o',label="Datos")
plt.plot(x,y_plot_exp,label="Ajuste exponencial")
plt.plot(x, y_plot, label="Ajuste lineal")
plt.legend()
plt.show()




