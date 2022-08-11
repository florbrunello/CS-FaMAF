"""
Ejercicio 2: 
Se desea encontrar la cantidad aproximada de metros cubicos de tierra que deben ser
removidos para nivelar a 0 metros un terreno de 12m * 10m. Este terreno particular 
puede verse como un cierto perfil a lo largo de 10m.
Del perfil a ser considerado tenemos las siguientes mediciones (en metros):

xi     0  1.5 2  2.9   4 5.6   6 7.1 8.05 9.2  10 11.3  12
f(xi) 0.1 0.2 1 0.56 1.5 2.0 2.3 1.3  0.8 0.6 0.4  0.3 0.2

(a) Realice un grafico de los datos utilizando puntos discretos.
(b) Modificar el metodo del trapecio para integrar funciones en intervalos de longitud
arbitraria (no equidistantes). Crear una funcion (trapecio adaptativo) que, dadas la 
particion y los valores de la funcion en la particion, devuelva la aproximacion de la
integral usando este metodo.
(c) Usando la funcion trapecio adaptativo calcular la cantidad (aproximada) de metros
cubicos de tierra que deben ser removidos para nivelar a 0 metros el terreno considerado.
"""

import matplotlib.pyplot as plt

#Inciso A

x = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
y = [0.1, 0.2, 1, 0.56, 1.5, 2, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]

plt.plot(x,y,'*',label='Gráfico de Puntos Discretos - Mediciones')
plt.legend()
plt.show()

#Inciso B

def trapecio_adaptativo(x,y):
    
    w=0

    for j in range (len(x)-1):
        a = x[j]
        b = x[j+1]
        
        w = w + ((b-a) / 2)*(y[j] + y[j+1])
    
    return w

#Inciso C

integracion = trapecio_adaptativo(x,y)
print(f'Debo remover {10 * integracion} metros cúbicos de tierra para nivelar a 0 metros el terreno\n')