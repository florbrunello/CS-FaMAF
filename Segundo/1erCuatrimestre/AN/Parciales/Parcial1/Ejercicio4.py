"""
Ejercicio 4: 
Modifique el programa del metodo de Newton para transformarlo en el metodo de 
Steffensen (sin derivadas). La funcion debe llamarse rsteffensen, y tener como
entrada los argumentos (fun,x0,err,mit), donde fun es una funcion que dado x 
retorna f (x), x0 es el punto inicial, err es la tolerancia deseada del error
y mit es el numero maximo de iteraciones permitidas. El algoritmo debe finalizar 
en la k-esima iteracion si |f(xk)| < err o si k ≥ mit. Los argumentos de salida
deben ser (hx,hf) donde hx = [x1,...,xN] es una lista que representa el historial
de puntos generados y hf= [f(x1),...,f(xN)] el historial de los respectivos 
valores funcionales.
"""

def rsteffensen(fun, x0, err, mit):
    hx=[]
    hf=[] 
    f = fun(x0)

    for it in range(mit):
        
        if (abs((fun(x0+f)-f))==0):
            print("No puedo dividir por cero")
            break 

        x_k = x0 -((f**2)/(fun(x0+f)-f))
        f = fun(x_k) 
        hx.append(x_k) 
        hf.append(f)

        if (abs(f)<err): 
            print("Salimos")
            break 

        x0 = x_k

    return hx,hf 

"""
Instrucciones de ejecución: 

#Ejemplo de implementación: 

def fun_raiz_cuadrada_de_cuatro(x): 
    f = x**2-4
    return f

hx, hf = rsteffensen(fun_raiz_cuadrada_de_cuatro, 3.0, 1e-7, 100)
print(hx,hf)

Al compilar el ejemplo obtendremos el resultado de llamar a la funcion rsteffensen donde 
se busca calcular la raiz cuadrada de cuartro (notar que el ultimo elemento de 
la lista hx es 2.0000000000789546). 
"""