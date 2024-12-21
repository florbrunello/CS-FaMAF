"""
Ejercicio 3: 
Encontrar las dos raices positivas con el metodo de biseccion, con una cantidad 
maxima de 100 iteraciones y una tolerancia de 1e-5 (estimar los intervalos de 
busqueda a partir del grafico). Los argumentos de salida deben ser (hx,hf) donde
hx = [x1,...,xN] es una lista que representa el historial de puntos medios y 
hf = [f(x1),...,f(xN)] el historial de los respectivos valores funcionales.
"""

from Ejercicio1 import serie_seno

def rbisec(fun, I, mit, err):
    hx = []
    hf = []
    a, b = I

    u = fun(a)
    v = fun(b)

    if u * v > 0:
        print("no se cumplen las hipotesis")
        return None

    for it in range(mit):
        e = (b - a) / 2
        c = a + e
        w = fun(c)
    
        hx.append(c)
        hf.append(w)
        
        if abs(w) < err:
            print(f"se satisface la tolerancia con valor {w} en {c}")
            break

        if w * v < 0:
            a = c
            u = w
        else:
            b = c
            v = w
    
    return hx, hf

hx1, hf1 = rbisec(serie_seno,[1.5,3.5], 100, 1e-5)
print(f"La aproximacion de la 1er raiz de la serie de taylor del seno en el intervalo [1.5,3.5] es {hx1[-1]}")

hx2, hf2 = rbisec(serie_seno,[4.5,5.5], 100, 1e-5)
print(f"La aproximacion de la 2da raiz de la serie de taylor del seno en el intervalo [4.5,5.5] es {hx2[-1]}")


"""
Instrucciones de ejecución: 

Si quisieramos consultar la lista que representa el historial de puntos medios y el historial de 
los respectivos valores funcionales podemos añadir el siguiente código: 

print(f"Lista que representa el historial de puntos medios: {hx1}")
print(f"Lista que representa el historial de los respectivos valores funcionales.: {hf1}")

print(f"Lista que representa el historial de puntos medios: {hx2}")
print(f"Lista que representa el historial de los respectivos valores funcionales.: {hf2}")

Notar que para la ejecución en sí solo basta con compilar el archivo, luego obtendremos las raices 
buscadas. 
"""
