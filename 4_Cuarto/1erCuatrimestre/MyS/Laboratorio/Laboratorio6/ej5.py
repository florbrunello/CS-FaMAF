import random
import math

# Ejrercicio a
def variable_aleatoria_M():
    U = random.random()
    V = random.random()
    sucesion = [U, V]
    n = 2
    while sucesion[n-2] <= sucesion[n-1]:
        n += 1
        U = random.random()
        sucesion.append(U)
    return n

# Ejercicio c
def media_muestal_X(d=0.01): 
    media = variable_aleatoria_M()
    scuad, n = 0, 1
    #Profe: poner un n grande e imprimirlo ...
    # Al menos 100 por TCL 
    # Como se cumple antes de las 100 iteraciones, haciendo while n <= 10 or scuad/n > d se cumple 
    # pero aproxima mal porque no llega a 100 iteraciones
    while n <= 100 or scuad/n > d:
        n += 1
        X = variable_aleatoria_M() 
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
        print(scuad/n)
    print(scuad/n)
    return media, scuad, n
    
# Ejercicio d
def media_muestral_IC_X(z_alpha_2 = 1.96, L=0.1):
    d = L / (2 * z_alpha_2)
    media = variable_aleatoria_M() 
    scuad, n = 0, 1
    while n <= 100 or math.sqrt(scuad/n) > d: 
        n += 1
        X = variable_aleatoria_M()
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
    return media, scuad, n
    
def main(): 

    print("Ejercicio c")
    media, varianza, n = media_muestal_X()
    print("Estimacion de la media: ", media)
    print("Estimacion de la varianza muestral: 0.008")
    print("Scuad debe ser < 0.01 ", varianza/n)
    print("Cantidad de iteraciones: ", n)

    print("Ejercicio d")
    media, scuad, n = media_muestral_IC_X()
    s = math.sqrt(scuad)
    print("IC del 95% para e: (X - 1.96 S/Raiz(n) , X + S/Raiz(n)) = (", media-1.96*s/math.sqrt(n), ", ", media+1.96*s/math.sqrt(n), ")")

if __name__ == "__main__":
    main()