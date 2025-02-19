"""
Ejercicio 1: 
Programar una funcion en python que integre numericamente usando las reglas compuestas
del trapecio, punto medio y Simpson, nombrarla intenumcomp. La funcion debera ejecutarse:
python> S = intenumcomp(fun,a,b,N,regla) donde fun es la funcion de R en R a ser 
integrada, a,b ∈ Rson los extremos de integracion, N es la cantidad de subintervalos a
usar y regla es un string, que debera ser trapecio, pm o simpson. La salida S debe ser
un numero real.
"""

import numpy as np

def intenumcomp(fun, a, b, N, regla):
    """
    Función que calcula la integral numérica de una función utilizando los métodos compuestos.
    """
    # Primero debemos definir la partición (puntos) de acuerdo
    # a la cantidad de intervalos que se pide.
    puntos = np.linspace(a, b, N + 1)
    # Es útil que las evaluaciones de la función en los
    # puntos generados se guarde como un arreglo de Numpy.
    evals = np.array([fun(x) for x in puntos])
    # Definimos el ancho de cada intervalo
    h = (b - a) / N

    # Iniciamos el valor de la integral en 0 antes de comenzar
    s = 0
    if regla == "pm":
        if N % 2 == 1:
            print("punto medio necesita intervalos pares")
            return None
        # Si queremos acceder a todos los nodos impares de un arreglo de Numpy,
        # podemos utilizar el slicing comienzo:fin:paso, que deberíamos
        # reemplazar por 1::2
        s = h * 2 * np.sum(evals[1::2])

    elif regla == "simpson":
        
        #Chequeo que N sea par
        if (N%2 != 0):
            print("N debe ser par")
            return None

        #h indica la distancia entre cada nodo
        h = (b-a)/N

        #Genero la lista x con los nodos igualemnte espaciados
        x = np.linspace(a,b,N+1)
        #Creo una lista con las evaluaciones de los nodos de x
        f = np.array([fun(xi) for xi in x])

        #Calculo f(x_n)
        fn = f[-1]

        #Genero un nuevo arreglo (matriz) reordenando los datos
        f = np.reshape(f[:-1],(-1,2))

        #Calculo f(x_0)
        f0 = f[0,0]

        f_pares = f[1:,0]
        f_impares = f[:,1]

        I = (h/3)*(f0 + 2*np.sum(f_pares) + 4*np.sum(f_impares) + fn )
        
    elif regla == "trapecio":
        s = fun(a) + fun(b)
        # Podemos acceder a todos los puntos sin los extremos usando [1:-1]
        s = (s + 2 * np.sum(evals[1:-1])) * (h / 2)

    else:
        print("Elija una regla correcta")

    return s

"""
def fun(x):
    return abs(x)

def test_intenumcomp():
    # La integral del valor absoluto nos debería dar 1 entre -1 y 1.
    print(intenumcomp(fun, -1, 1, 101, "pm"))
"""