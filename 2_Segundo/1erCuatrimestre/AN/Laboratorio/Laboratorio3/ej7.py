"""
Ejericio 7: 
Escriba una funcion rinterp(fun,x0,x1,x2,err,mit) que encuentre un cero de la 
funcion fun de la siguiente forma. En cada paso, sea q_2 el polinomio 
interpolante cuadratico de los puntos (x_(n-2), f(x_(n-2)), (x_(n-1), 
f(x_(n-1)) y (x_n, f(x_n). Elegir como x_(n+1) al cero de q_2 que este mas 
cerca de x_n. Comparar su performance con los metodos para encontrar races del
laboratorio 2.
"""

from ej1 import ilagrange

def obtiene_coefs(x,y):
	# x = [x1, x2, x3]
	# y = [y1, y2, y3]
	z = [0,1,-1]
	c, ab1, ab2 = ilagrange(x,y,z)
	# ab1 = a+b+c
	ab1 = ab1 - c
	# ab2 = a-b+c
	ab2 = ab2 - c
	a = (ab1+ab2)/2
	b = (ab2-ab1)/2
	return a, b, c