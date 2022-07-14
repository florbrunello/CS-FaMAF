"""
Ejercicio 5: 
Leer como utilizar la funcion “interpd1” del paquete “scipy.interpolate” de python en
la pagina https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html
El archivo datos_aeroCBA.dat contiene una matriz con los datos de la pagina
https://www.tutiempo.net/clima/ws-873440.html. Cargar la matriz de datos en python usando 
np.loadtxt y extraer los datos existentes de temperatura media anual registrados en el Aeropuerto 
de Cordoba. Mediante un spline cubico estimar los valores faltantes y graficar. 
Observacion: en algunos casos sera necesario extrapolar.
Implementar la resolucion de este ejercicio en el script “lab3ej5”, que realice el grafico
y devuelva los valores de temperatura media para TODOS los años entre 1957 y 2017.
"""

import numpy as np 
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 

# Cargo los datos desde la url
datos = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos_aeroCBA.dat')

# Los datos que nos interesan son anios (primer columna) y temperatura (segunda columna)
year = datos[:,0]
temp = datos[:,1]

# Selecciono los pares de datos sin faltantes (NaN)
year_int = year[~np.isnan(temp)]
temp_int = temp[~np.isnan(temp)]

# Genero el polinomio interpolante: estimo los valores faltante con un spline cubico
pol = interp1d(year_int, temp_int, kind='cubic', fill_value='extrapolate')

# Pares de puntos interpolados
year_plot = np.arange(1957,2018)
temp_plot = pol(year_plot)

# Gráficos
plt.plot(year_int,temp_int,'o',label='Datos')
plt.plot(year_plot,temp_plot,label='Interpolaciones y extrapolaciones')
plt.legend()
plt.show()