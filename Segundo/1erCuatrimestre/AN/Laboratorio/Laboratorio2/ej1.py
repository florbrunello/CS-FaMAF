"""
Ejercicio 1: 

Escribir una funcion que implemente el metodo de biseccion para hallar una raiz de
f : R → R en el intervalo [a, b]. La funcion debe llamarse “rbisec”, y tener como
entrada los argumentos (fun,I,err,mit), donde fun es una funcion que dado x retorna f(x), 
I= [a, b] es un intervalo en R, err es la tolerancia deseada del error y
mit es el numero maximo de iteraciones permitidas. El algoritmo debe finalizar en la
k-esima iteracion si |f(xk)| < err o si k ≥ mit. Los argumentos de salida deben ser
(hx,hf) donde hx= [x1, . . . , xN ] es una lista que representa el historial de puntos medios
y hf= [f(x1), . . . , f(xN )] el historial de los respectivos valores funcionales
"""

# Desde una librería o módulo podemos importar las funciones que 
# querramos usar, no es necesario importar todo al mismo tiempo,
# Por ejemplo para el ejercicio 2 a) necesitamos sólo tangente.
from math import tan
# La librería Matplotlib nos permite graficar, esta importación
# es el uso más común.
import matplotlib.pyplot as plt

def rbisec(fun, I, err, mit):
    """
    Función que aplica el método de bisección, recibe:
    - fun: Función que recibe un x y devuelve un número.
    - I: Intervalo de la forma [a, b].
    - mit: Cantidad máxima de iteraciones.
    - err: Tolerancia para considerar un valor como cero.
    Retorna:
    - hx: Lista (historial) de puntos medios de bisección.
    - hf: Evaluación de la función en esos puntos.
    """
    # Inicio los historiales como listas vacías para agregar
    # puntos con .append()
    hx = []
    hf = []
    # Luego leer la lista I como dos números, se puede hacer de 2 formas
    # a, b = I

    a = I[0]
    b = I[1]

    # Depositamos la evaluación de fun en a y b como u y v, respectivamente
    u = fun(a)
    v = fun(b)

    # Si u y v tienen mismo signo, no podemos seguir
    if u * v > 0:
        print("No se cumplen las hipotesis")
        # Si la función llega a ejecutar un return, no hace nada más después de eso
        return None

    # Comenzamos a iterar, hasta mit iteraciones
    for it in range(mit):
        # Conseguimos el punto medio entre a y b y depositamos la evaluación en w
        """ OJO es b-a, NO a-b"""
        e = (b - a) / 2
        c = a + e
        w = fun(c)
    
        # Agregamos ambos elementos a sus respectivos historiales
        hx.append(c)
        hf.append(w)
        
        # Si la función evaluada en c es suficientemente pequeña en modulo, salimos del for
        """ OJO el err refiere a la funcion, no al valor de x """
        if abs(w) < err:
            # Si usamos f-string, no tenemos que poner comas innecesarias en print
            print(f"Se satisface la tolerancia con valor {w} en {c}")
            #print("se satisface la tolerancia en ", abs(w), " en x = ", c)
            break

        # Si fun(c) y fun(b) tienen distinto signo reemplazo a por c, si no al revés.
        if w * v < 0:
            a = c
            u = w
        else:
            b = c
            v = w
    
    # Puedo retornar más de una variable si las separo con comas en el return
    return hx, hf