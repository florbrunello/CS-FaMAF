"""
Ejercicio 1: 
En 2017, el huracan Irma fue el mas intenso que impacto en Estados Unidos desde el 
huracan Katrina en 2005, con rafagas de viento de hasta 285 km/h. Durante el 10 de 
septiembre, el centro del huracan ingreso al estado de Florida y en los datos en el 
archivo irma.csv se muestran las coordenadas del mismo cada 3 horas, durante 24 horas. 
La primer columna denota la hora, la segunda la longitud y la tercera muestra la 
latitud.
(a) Realice un grafico que muestre los puntos de los datos (nota: la longitud indica
el eje X y la latitud el eje Y).
(b) Interpolar las funciones longitud(t) y latitud(t) utilizando los metodos de 
interpolacion de Lagrange y Spline cubico y estimar las longitudes y latitudes del ojo
del huracan cada una hora. Realice un grafico que muestre los puntos de los datos y 
las trayectorias calculadas con ambos metodos de interpolacion.
"""

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np 
import csv

filepath = open('/home/usuario/Escritorio/AN/Parcial2/irma.csv')
datos = np.loadtxt(filepath,float,delimiter=",")

horas = datos[:, 0]
longitud = datos[:, 1]
latitud = datos[:, 2]

#Inciso A

#Grafico la longitud y latitud
plt.plot(longitud,latitud,'*',label="Puntos de los datos")
plt.legend()
plt.show()

#Inciso B

#Longitud

#Creo un arreglo con las horas del 0 al 24 
estimacion = np.arange(25)

def ilagrange(x, y, z):
    
    #Cálculo del polinomio de Lagrange dado por los puntos (x_i, y_i) en los puntos z_i.
    n = len(x)
    #Genero una lista vacía donde almaceno p(z_k)
    w = []  

    for k in z:
        suma = 0
        for i in range(n):
            #Siempre que comenzamos una productoria, usamos 1 para iniciar (neutro del producto)
            prod = 1 
            for j in range(n):
                if i != j:
                    prod = prod * (k - x[j]) / (x[i] - x[j])
            #Sumo l_i(z_k) * y_i        
            suma = suma + prod * y[i]
        
        w.append(suma)
    
    return w

#Interpolo las horas y longitudes con el método de lagrange y lo evaluo en las 24 horas
w = ilagrange(horas,longitud, estimacion)

#Scipy, para poder usar Spline es necesario agregar el argumento kind="cubic"
#Interp1d nos devuelve una función que podemos evaluar en la cantidad de puntos que interpolo
z = interp1d(horas, longitud, kind="cubic")

plt.plot(estimacion,w,label="Interpolacion con Lagrange - Longitud")
plt.plot(horas,z(horas),label="Interpolacion con Spline Cubico - Longitud")
plt.plot(horas,longitud,'*',label="Puntos")
plt.legend()
plt.show()

#Latitud

#Interpolo las horas y latitudes con el método de lagrange y lo evalúo en las horas
y = ilagrange(horas,latitud, estimacion)
#Interpolo las horas y latitudes con Spline Cubico
p = interp1d(horas, latitud, kind="cubic")

plt.plot(estimacion,y,label="Interpolacion con Lagrange - Latitud")
plt.plot(horas,p(horas),label="Interpolacion con Spline Cubico - Latitud")
plt.plot(horas,latitud,'*',label="Puntos")
plt.legend()
plt.show()