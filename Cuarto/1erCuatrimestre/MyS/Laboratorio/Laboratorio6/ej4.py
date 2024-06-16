import random
import math 

# Ejercicio a
def n():
    suma = 0
    n = 0
    while suma <= 1:
        suma += random.random()
        n += 1
    return n

def est_E_N(NSim):
    suma_e = 0              
    for _ in range(NSim):
        suma_e += n()
    return suma_e/NSim

# Ejercicio b
def est_V_N(NSim):
    suma = 0 
    for _ in range(NSim):
        suma += (3*math.e - math.e**2) / NSim
    return suma/NSim

def media_muestal_Y(Nsim):
    media = n()
    scuad = 0
    for i in range(2, Nsim):
        X = n()
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / i
        scuad = scuad * (1 - 1/(i-1)) + i*(media - mediaAnt)**2
    return media, scuad

# Ejercicio c
def media_muestral_X(fun, z_alpha_2=1.96, L=0.025):
    d = L / (2 * z_alpha_2)
    media = fun()
    scuad, n = 0, 1
    while n <= 100 or math.sqrt(scuad/n) > d: 
        n += 1
        X = fun()
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
    return media

def main():
    
    Nsim = 1000
    
    print("Ejercicio b")
    var_aprox = est_V_N(Nsim)
    data = media_muestal_Y(Nsim)
    scuad = data[1]
    s = math.sqrt(scuad)
    # Varianza muestral: 0.00069394
    print(" Varianza del estimador N :", (3*math.e - math.e**2)/Nsim)
    print(" Aproximacion Varianza del estimador N:", var_aprox)
    print(" Estimador de maxima verosimilitud de la varianza muestral: ", scuad/Nsim)
    
    print("Ejercicio c")
    media = media_muestral_X(n)
    # Intervalo de Confianza del 95% para e: (X - 1.96 S/Raiz(n) , X + S/Raiz(n)) = (2.594, 2.6973)
    print(" Intervalo de Confianza del 95% para e: (", media - 1.96 * s/math.sqrt(Nsim), media + 1.96 * s/math.sqrt(Nsim), ")")

if __name__ == "__main__":
    main()