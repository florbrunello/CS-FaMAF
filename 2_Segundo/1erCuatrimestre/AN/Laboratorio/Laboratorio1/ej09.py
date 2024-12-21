"""
Ejercicio 9: 

Escribir una funcion, llamada horn, que implemente el algoritmo de Horner para la evaluacion de polinomios.
La sintaxis de llamada a la rutina deberia ser:
 p = horn(coefs, x)
donde p es el valor del polinomio, coefs es un vector con los coeficientes del polinomio,
de mayor a menor grado y x es el valor de la variable independiente. Es decir que si, por
ejemplo, hacemos:
 p = horn([1, -5, 6, 2],2)
entonces la variable p almacenara el valor p(2) donde p(x) = x
3 - 5x
2 + 6x + 2
"""

def horn(coefs, x):
    """
    Función que calcula el valor del polinomio cuyos coeficientes son parte 
    de la lista coefs y devuelve como resultado la evaluación del polinomio en x.
    Por ejemplo, coefs = [1, 2, -3] -> x² + 2x - 3
    y horn([1, 2, -3], 2.0) = 5.
    """

    # Primero, obtenemos la longitud de la lista, para poder iterar sobre ella.
    n = len(coefs)
    # Definimos la variable b, que será la de salida, como el primer coeficiente.
    b = coefs[0]
    for idx in range(1, n):
        # Iteramos desde el segundo elemento de coefs hasta el último
        # siguiendo la fórmula del teórico
        b = coefs[idx] + x * b
    
    return b

# Finalmente probamos la función, este resultado debería ser 2.
p = horn([1, -5, 6, 2], 2)
print(p)

"""
#coefs = [5,4,3,2,1]
#x = 8
#p(x) = 5x⁴ + 4x³ + 3x² + 2x + 1
#p(8)

def horn (coefs,x):
    b_k = coefs[0]
    i = len(coefs) - 1

    for k in range(0,i):
        b_k = coefs[k+1] + x * b_k

    return b_k

res = horn([1, -5, 6, 2],2)
print(res)
"""
