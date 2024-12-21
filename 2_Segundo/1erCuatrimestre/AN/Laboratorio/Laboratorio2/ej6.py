"""
Ejercico 6: 

Se quiere usar la formula de iteracion x_(n+1) = 2^(x_n-1) para resolver la ecuacion 2x = 2^x
Utilizar la funcion del ejercicio anterior para investigar si converge; y en caso afirmativo,
estudiar hacia que valores lo hace para distintas elecciones de x0, tomando un numero
maximo de 100 iteraciones y un error menor a 10^(-5). Usar la siguiente sintaxis:
hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
"""

import math
from ej5 import ripf

def fun_lab2ej6(x):
	return math.pow(2,x-1)

for x0 in range (5):
	hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
	print(hx[-1])

"""
Resultado: 

0.9999840760746218
1.0
2.0
Traceback (most recent call last):
  File "/home/usuario/Escritorio/AN/Lab02/ej6.py", line 18, in <module>
    hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
  File "/home/usuario/Escritorio/AN/Lab02/ej5.py", line 17, in ripf
    x_k = fun(x_0)
  File "/home/usuario/Escritorio/AN/Lab02/ej6.py", line 15, in fun_lab2ej6
    return math.pow(2,x-1)
OverflowError: math range error

Casos: 
	x0 = 0 -> Converge a 1
	x0 = 1 -> Converge a 1
	x0 = 2 -> Converge a 2
	x0 = 3 -> Overflow
	x0 = 4 -> Overflow
	...
	
"""