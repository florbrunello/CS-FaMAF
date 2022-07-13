"""
Ejercicio 12:

Escribir una funcion llamada SonOrtogonales([x1,x2],[y1,y2]) que tenga como entrada dos vectores 
x, y ∈ R2 y que devuelva True si los vectores son ortogonales.
Ejecutar las siguientes instrucciones:
    x = [1, 1.1024074512658109]
    y = [-1, 1/x[1]]
    if not SonOrtogonales(x,y):
    print("Algo salio mal...")
    
Explicar lo que sucedio
"""
"""
Otra version
def SonOrtogonales(x,y):
    esc = x[0] * y[0] + x[1] * y[1]
    if (esc == 0): 
        print("Son ortogonales")
        return True
    else: 
        print("No son ortogonales")
        return False
"""   
 
def SonOrtogonales(x,y):
	# x = [x1, x2]
	# y = [y1, y2]
	tol = 1e-10
	prod_punto = x[0]*y[0] + x[1]*y[1]
	# if prod_punto == 0:
	if abs(prod_punto) < tol :
		return True

x = [1,1.102474512658109]
y = [-1, 1/x[1]]
if not SonOrtogonales(x,y): 
    print("Algo salió mal...")
