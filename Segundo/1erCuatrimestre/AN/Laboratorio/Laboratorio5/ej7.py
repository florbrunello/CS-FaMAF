"""
Ejercicio 7:
Se desea implementar una regla de cuadratura adaptiva, es decir, una cuadratura 
compuesta que utilice mas subintervalos en la zona en que la aproximacion obtenida 
sea peor. Para ello, notamos S(a,b) a la regla de Simpson en el intervalo [a,b]. 
Si notamos c = (a+b)/2, se tiene que: |S(a,b) -S(a,c) -S(c,b)| 15 ≈E(a,c,b),donde 
E(a,c,b) es el error cometido al aplicar la regla compuesta: S(a,c) + S(c,b). 
Implementar un programa que reciba como input una funcion f, un intervalo [a,b] y 
una tolerancia e y calcule las cuadraturas: q = S(a,b), q1 = S(a,c) y q2 = S(c,b). 
Si |q-q1 -q2|< 15e, se devuelve el valor q1 + q2. En caso contrario, se aplica el mismo
criterio para integrar f en los intervalos [a,c] y [c,b], con una tolerancia e2.
Probar el programa calculando ∫ 1 0 xe-x2 dx = 1 2 (1 -e-1). Comparar los resultados 
(y los tiempos de ejecucion) con los obtenidos por la regla de Simpson compuesta.
"""

from ej1a import simpson

def simpson_simple(fun,a,b):
	return simpson(fun,a,b,2)

def simpson_adap_recursiva(fun,a,b,err):
	c = (a+b)/2
	q = simpson_simple(fun,a,b)
	q1 = simpson_simple(fun,a,c)
	q2 = simpson_simple(fun,c,b)
	if abs(q-q1-q2) < 15*err:
		I = q1 + q2
	else:
		q1 = simpson_adap_recursiva(fun,a,c,err/2)
		q2 = simpson_adap_recursiva(fun,c,b,err/2)
		I = q1 + q2
	return I

def simpson_adap(fun,a,b,err):
	q = simpson_simple(fun,a,b)
	stack = [[a,b,q,err]]
	I = 0.
	while stack:
		cur_int = stack.pop(-1)
		cur_a = cur_int[0]
		cur_b = cur_int[1]
		cur_q = cur_int[2]
		cur_err = cur_int[3]
		c = (cur_a + cur_b) / 2
		q1 = simpson_simple(fun,cur_a,c)
		q2 = simpson_simple(fun,c,cur_b)
		if abs(cur_q - q1 - q2) < 15*cur_err:
			I += q1 + q2
		else:
			# partir el intervalo
			# agregar ambas mitades a la pila
			stack.append([cur_a,c,q1,cur_err/2])
			stack.append([c,cur_b,q2,cur_err/2])
	return I

import numpy as np
import time

fun = lambda x : x*np.exp(-x**2)

err = 1e-15

I_exacta = 0.5*(1-np.exp(-1))

start = time.time()

I_recursiva = simpson_adap_recursiva(fun,0,1,err)

print(f"Simpson adaptativo recursivo demoró {time.time()-start} y calculó {I_recursiva}")

start = time.time()

I_no_recursiva = simpson_adap(fun,0,1,err)

print(f"Simpson adaptativo no recursivo demoró {time.time()-start} y calculó {I_no_recursiva}")

cota_d4f = 156

N_simpson = int(np.ceil((cota_d4f/(err*180))**(1/4)))

start = time.time()

I_compuesta = simpson(fun,0,1,N_simpson)

print(f"Simpson compuesta demoró {time.time()-start} y calculó {I_compuesta}")