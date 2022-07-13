"""
Ejercicio 4:

Escribir una funcion que, ingresando a > 0, retorne una aproximacion de √3 a. 
La aproximacion debe realizarse usando el metodo de Newton del ejercicio anterior para resolver
x 3 - a = 0 con un error menor a 10-6 mediante el uso de la funcion x → x 3 - a.
"""

from ej3 import rnewton 

def buscar_raiz_cubica(a): 
    fun = lambda x: (x**3 -a, 3 * x**2)
    """
    lo de arriba es lo mismo que hacer lo siguiente (adentro de la funcion!!!)
    def fun(x):
        return x ** 3 - a, 3 * x ** 2
    """    
    hx, hf = rnewton(fun,a,1e-8, 100)
    return hx,hf

hx, hf = buscar_raiz_cubica(27.0)
print(hx[-1]) 

"""
from ej3 import rnewton

def fun_raiz_cuadrada_de_cuatro(x): 
    f = x**2-4
    df = 2 * x
    return f,df

hx, hf = rnewton(fun_raiz_cuadrada_de_cuatro, 3.0, 1e-7, 100)
print(hx,hf)

Comentarios: 

- rnewton devuevle dos listas. Ojo a donde lo asigno

- La f que le paso devuelve dos cosas !
"""

