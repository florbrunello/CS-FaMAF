import random
import math

NV_MAGICCONST = 4 * math.exp(-0.5) / math.sqrt(2.0)
def normal_variate_razon_uniformes_X(mu, sigma): 
    while True:
        U1 = random.random()
        U2 = 1 - random.random()
        Z = NV_MAGICCONST * (U1 - 0.5) / U2
        ZZ = Z*Z / 4.0
        if ZZ <= -math.log(U2): 
            break
    return Z * sigma + mu

def media_muestal_X(d=0.1):
    media = normal_variate_razon_uniformes_X(0, 1)
    scuad, n = 0, 1
    sample = [media]
    while n <= 100 or math.sqrt(scuad/n) > d:
        n += 1
        X = normal_variate_razon_uniformes_X(0, 1)
        sample.append(X)
        mediaAnt = media 
        media = mediaAnt + (X - mediaAnt) / n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - mediaAnt)**2
    return sample, media, scuad

def main(): 
    datos = media_muestal_X()
    n = len(datos[0])
    media_muestral = datos[1]
    var_muestral = datos[2]

    # Ejercicio a
    print("Numero de datos generados: n =", n)

    # Ejercicio b
    print("Media muestral de los datos generados: X = ", media_muestral)
    
    # Ejercicio c
    print("Varianza muestral de los datos generados: X = ", var_muestral)

if __name__ == "__main__":
    main()
