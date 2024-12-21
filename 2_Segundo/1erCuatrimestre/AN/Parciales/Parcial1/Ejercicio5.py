"""
Ejercicio 5: 
Encontrar las dos raices positivas de serie seno(x) comenzando con puntos iniciales
3 y 6, con una cantidad maxima de 100 iteraciones y una tolerancia de 1e-5. ¿Cuantas 
iteraciones requiere cada busqueda? ¿Que ocurre al iniciar la busqueda en 4.5?
"""

from Ejercicio1 import serie_seno
from Ejercicio4 import rsteffensen

hx1, hf1 = rsteffensen(serie_seno, 3.0, 1e-5, 100)
print(hx1,hf1)
print(f"Cantidad de iteraciones: {len(hx1)}")

hx2, hf2 = rsteffensen(serie_seno, 6.0, 1e-5, 100)
print(hx2,hf2)
print(f"Cantidad de iteraciones: {len(hx2)}")

hx3, hf3 = rsteffensen(serie_seno, 4.5, 1e-5, 100)
print(hx3,hf3)
print(f"Cantidad de iteraciones: {len(hx3)}")

"""
Respuestas: 

¿Cuantas iteraciones requiere cada busqueda? 
    Notar que en cada caso se hizo un print(len(hx_i)), para i = 1,2,3. Esto nos indica el largo de 
    la lista hx (sería indistinto realizarlo con hf) y se corresponde con las cantidades de 
    iteraciones realizadas en cada búsqueda. Al compilarlo obtenemos los siguientes resultados: 
        a) Comenzando en 3.0 = 1 iteracion 
        b) Comenzando en 6.0 = 69 iteraciones 
        b) Comenzando en 4.50 = 100 iteraciones

¿Que ocurre al iniciar la busqueda en 4.5?
    Al iniciar la busqueda en 4.5, el algoritmo, en particular el for, realiza todas las iteraciones
    posibles (100) puesto que no va a converger, es decir, nunca obtendremos un resultado cuyo error 
    sea menor al permitido (tolerancia). En cambio, para el caso a y b, salimos del for y convergemos
    a la primer y segunda raiz respectivamente.
"""