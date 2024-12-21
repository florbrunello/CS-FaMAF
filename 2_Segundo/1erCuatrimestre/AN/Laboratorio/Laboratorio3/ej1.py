"""
Ejercicio 1: 
Programar una funcion en python que evalue el polinomio interpolante p usando la forma
de Lagrange. La funcion debe llamarse “ilagrange” y tener como entrada (x, y, z) donde
x, y ∈ Rn son las coordenadas de los pares a interpolar (o sea p(xi) = yi, i = 1, . . . , n)
y z ∈ Rm son valores para evaluar p. La salida debe ser w ∈ Rm tal que wj = p(zj ), j = 1, . . . , m. 
La sintaxis a utilizar debe ser: w = ilagrange(x, y, z).
"""

def ilagrange(x, y, z):
    """
    Cálculo del polinomio de Lagrange dado por los puntos (x_i, y_i) en los puntos z_i.
    """
    n = len(x)
    w = []  # Generamos una lista vacía donde almacenamos p(z_k)
    for k in z:
        suma = 0
        for i in range(n):
            prod = 1  # Siempre que comenzamos una productoria, usar 1 para iniciar (neutro del producto)
            for j in range(n):
                if i != j:
                    prod = prod * (k - x[j]) / (x[i] - x[j])
            # Sumamos l_i(z_k) * y_i        
            suma = suma + prod * y[i]
        
        w.append(suma)
    
    return w