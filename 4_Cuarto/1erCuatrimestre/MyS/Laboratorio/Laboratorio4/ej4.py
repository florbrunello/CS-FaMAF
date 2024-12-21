import random
import time

# Ejercicio a
def aceptacion_rechazo():
    # Valores y probabilidades de X
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    
    # Valores y probabilidades de Y
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    q = [1/10] * 10
    
    c = max([p[i] / q[i] for i in range(10)])

    while True:
        Y = random.randint(1, 10)
        U = random.random()
        if U < p[Y-1] / (c * q[Y-1]):
            return Y

# Ejercicio b
x_reordenados = [2, 5, 1, 9, 6, 3, 7, 10, 4, 8]
p_reordenados = [0.14, 0.12, 0.11, 0.11, 0.10, 0.09, 0.09, 0.09, 0.08, 0.07]

def discretaX(p=p_reordenados,x=x_reordenados):
    U = random.random()
    i, F = 0, p[0]
    while U >= F:
        i += 1
        F += p[i]
    return x[i]

def X_TI(): 
    # x = [1,2,3,4,5,6,7,8,9,10]
    # p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.1, 0.09, 0.07, 0.11, 0.09]
    U = random.random()
    if U < 0.11:
        return 1
    elif U < 0.25:
        return 2
    elif U < 0.34:
        return 3
    elif U < 0.42:
        return 4
    elif U < 0.54:
        return 5
    elif U < 0.64:
        return 6
    elif U < 0.73:
        return 7
    elif U < 0.8:
        return 8
    elif U < 0.91:
        return 9
    else:
        return 10

def X_TI_Mejora():
    U = random.random()
    if U < 0.14:
        return 2
    elif U < 0.25:
        return 1
    elif U < 0.34:
        return 3
    elif U < 0.42:
        return 4
    elif U < 0.54:
        return 5
    elif U < 0.64:
        return 6
    elif U < 0.73:
        return 7
    elif U < 0.8:
        return 8
    elif U < 0.91:
        return 9
    else:
        return 10

# Ejercicio c
a = [1] * 11 + [2] * 14 + [3] * 9 + [4] * 8 + [5] * 12 + [6] * 10 + [7] * 9 + [8] * 7 + [9] * 11 + [10] * 9

def urnaX(A=a, k=100): 
    I = int(random.random() * k)
    return A[I]

# Ejercicio d 
def sim(X, Nsim): 
    start = time.time()
    for _ in range(Nsim):
        X()
    end = time.time()
    return end-start

def main():
    Nsim = 10000
    print("Tiempo de ejecución de X_Rechazo: ", sim(aceptacion_rechazo, Nsim))
    print("Tiempo de ejecución de X_Transformada: ", sim(discretaX, Nsim))
    print("Tiempo de ejecución de X_Urna: ", sim(urnaX, Nsim))

if __name__ == "__main__":
    main()
