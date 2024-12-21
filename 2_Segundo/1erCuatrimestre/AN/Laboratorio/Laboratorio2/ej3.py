"""
Ejercicio 3: 

Escribir una funcion que implemente el metodo de Newton para hallar una raiz de
f : R → R partiendo de un punto inicial x0. La funcion debe llamarse “rnewton”, y
tener como entrada (fun,x0,err,mit) donde fun es una funcion que dado x retorna f(x)
y f'(x), x0 es un punto inicial en R, err es la tolerancia deseada del error y mit
 es el numero maximo de iteraciones permitidas. El algoritmo debe finalizar en la 
 k-esima iteracion si se cumple alguna de las siguientes condiciones:
|xk - xk-1| / |xk| < err, |f(xk)| < err, k ≥ mit.
La salida debe ser (hx,hf) donde hx= [x1, . . . , xN ] es una lista que representa el
historico de puntos generados y hf= [f(x1), . . . , f(xN )] el historico de los 
respectivos valores funcionales.
"""

def rnewton (fun, x_0, err, mit):
    hx = []
    hf = []    
    v, dv = fun(x_0)
   
    for it in range (mit):

        if abs(dv)==0: 
            print("No puedo dividir por cero")
            break      

        x_k = x_0 - v / dv
        v, dv = fun(x_k)

        hx.append(x_k)
        hf.append(v)

        if ((abs(v) < err) or (abs(x_0 - x_k) / abs(x_k) < err)):
            print("Salimos")
            break 

        x_0 = x_k

    return hx,hf

"""
Comentarios: 

- Checkeo del ¡error relativo! entre x0 y xk

- No añadir los primeros valore s
        hx.append((x0))
        hf.append(v)    

- for it in range (mit) -> NO (1,mit+1)

- v,dv = fun(x0)

- hx.append(x_k) -> agrego cosas a mi lista  

- Con break dejo de ejecutar el bucle si no se cumple una condicion 

- Tengo que reactualizar x_0 antes de terminar la iteracion 

"""
