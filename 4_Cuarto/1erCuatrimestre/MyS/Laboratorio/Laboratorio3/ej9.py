from random import randint

# randint: genera numeros aleatorios enteros en un intervalo
# random: genera numeros aleatorios entre 0 y 1
# Resultado exacto 0.55 (periodico)

def est_puntaje(NSim):
    suma = 0
    for _ in range (NSim):
        d1 = randint(1,6)           # Tiro el dado la primera vez
        if d1 == 1 or d1 == 6:
            d2 = 2*randint(1,6) 
            if d2 > 6:              # Cuento las veces que gané (me paso de 6)
                suma += 1
        else:
            d2 = randint(1,6) 
            d3 = randint(1,6) 
            s = d2 + d3
            if s > 6: 
                suma += 1
    return suma/NSim                # Calculo el promedio de veces que gané

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
    print('Aproximacion para Nsim =',N[i])
    print(est_puntaje(N[i]))

# Opcion b

def D(): 
    d1 = randint(1,6)
    if d1 == 1 or d1 == 6: 
        d2 = 2*randint(1,6) 
        return d2

    else: 
        d2 = randint(1,6) 
        d3 = randint(1,6) 
        return d2 + d3

def P(NSim):
    suma = 0
    for _ in range (NSim):
        x = D()
        if x > 6:
            suma += 1
    return suma/NSim 

for i in range(len(N)):
    print('Aproximacion para Nsim =',N[i])
    print(P(N[i]))
