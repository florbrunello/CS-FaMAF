"""
Ejercicio 8: 

Escribir dos funciones en Python para la resolucion de ecuaciones de segundo grado ax2 +
bx + c = 0. Una de ellas, que llamaremos mala, implementando la tradicional formula
de Baskhara y la otra, que llamaremos buena, usando una manera eficiente para evitar
cancelacion de dgitos significativos. La sintaxis de la llamada a las funciones debera ser:
[x_1, x_2] = buena(a,b,c)
y analogamente para mala
"""

# Importamos la función de raiz cuadrada de la librería math
from math import sqrt

def mala(a,b,c):
    """
    Esta función calcula las raíces usando Bhaskhara para ambas.
    Recibe a, b y c (pensando en el polinomio a*x**2 + b*x + c)
    y devuelve una lista con las dos raíces.
    """
    if (b**2 - 4*a*c) < 0:
        print("El discriminante es negativo, no vamos a encontrar raíces reales.")
        return None

    x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2.0 * a)
    x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2.0 * a)

    return [x_1, x_2]


def buena(a, b, c):
    """
    Casi lo mismo que mala, sólo que usamos Bhaskhara para calcular la raíz
    más lejana al cero y luego usamos que x_1 * x_2 = c / a para conseguir la
    segunda raíz. Esto permite eliminar errores numéricos.
    """
    if (b**2 - 4*a*c) < 0:
        print("El discriminante es menor que 0, intente de nuevo")
        return None

    # encontrar la raiz más lejana al cero en valor absoluto.
    if b > 0:
        x_1 = (-b - sqrt(b**2 - 4*a*c)) / (2.0 * a)
    else:
        x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2.0 * a)

    x_2 = (c / a) / x_1

    return [x_1, x_2]

print(mala(1,-40,2))
print(buena(1,-40,2))

#No olvidar ((b**2 - 4*a*c) > 0)
#return [x_1,x_2]

"""
def buena (a,b,c):

    if (b>0):
        x_1 = ((-b) - (b**2-4*a*c))/2*a
    
    else: 
        x_1 = ((-b) + (b**2-4*a*c))/2*a
        x_2 = c / (a + x_1)
    
    return (x_1,x_2)
"""