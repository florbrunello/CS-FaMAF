"""
Ejercicio 6: 
Consideremos la siguiente tabla de datos:

x -3  -2  -1  0  1  2  3
f  1   2   5  10 5  2  1

Interpolar la tabla utilizando los métodos de Lagrange, Newton y el de la 
función interp1d, luego graficar los 3 polinomios juntos. 
¿Cuál polinomio parece más suave?
"""

from ej1 import ilagrange
from ej2 import inewton
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

x = [-3,-2,-1,0,1,2,3]
y = [1,2,5,10,5,2,1]

#Grafico los polinomios en el intervalo -3, 3
z = np.linspace(-3,3,101)

#Genero las interpolaciones de Lagrange y Newton
pol_l = ilagrange(x,y,z)
pol_n = inewton(x,y,z)

#Genero la interpolación mediante un spline y la evalúo en z
pol_spline = interpolate.interp1d(x, y, kind = 'cubic',bounds_error=False, fill_value = 'extrapolate')
pol_spline_plot = [pol_spline(i) for i in z] 

#Genero los tres gráficos
plt.plot(z,pol_n,color='cyan',label='Interpolacion segun Newton')
plt.plot(z,pol_l,color='blue',label='Interpolacion segun Lagrange',linestyle='dotted')
plt.plot(z,pol_spline_plot,color='orange',label='Interpolacion usando Spline Cubico')
plt.grid()
plt.legend()
plt.show()

"""
Observación: 
Los gráficos de Newton y Lagrange se pisan, es por ello que el segundo en 
graficarse debe trazarse con linestyle dotted. 
"""