import random
import math

# Ejercicio a

# Variable Aleatoria Normal Estandar - X ~ N(0, 1) Media (mu) 0 y Varianza (sigma) 1 #

# 1. Metodo Aceptacion - Rechazo | Generacion de variables exponenciales
def normal_aceptacion_rechazo_X(mu, sigma): 
    while True: 
        Y1 = -math.log(random.random())
        Y2 = -math.log(random.random())
        if Y2 >= (Y1 - 1)**2 / 2: 
            if random.random() <= 0.5: 
                return Y1 * sigma + mu
            else: 
                return -Y1 * sigma + mu
            
# 2. Metodo Polar
def metodo_polar_transformaciones_box_muller_X_Y(mu, sigma):
    while True: 
        V1 = 2 * random.random() - 1
        V2 = 2 * random.random() - 1
        if V1**2 + V2**2 <= 1: 
            S = V1**2 + V2**2
            X = V1 * math.sqrt(-2 * math.log(S) / S)
            Y = V2 * math.sqrt(-2 * math.log(S) / S)
            return X * sigma + mu, Y * sigma + mu

# 3. Metodo de Razon entre Uniformes
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

# Ejercicio b

# Estimador de la Esperanza
# Para el metodo de aceptacion-rechazo y el metodo de razon entre uniformes
def est_E(X, mu, sigma, Nsim): 
    p = 0
    for _ in range(Nsim): 
        p += X(mu, sigma)
    return p / Nsim

# Para el metodo polar que devuelve dos valores
def est_E2(X, mu, sigma, Nsim): 
    p = 0
    for _ in range(Nsim): 
        p += X(mu, sigma)[0]
    return p / Nsim

# Estimador de la Varianza
# Para el metodo de aceptacion-rechazo y el metodo de razon entre uniformes
def est_var(X, mu, sigma, Nsim): 
    v = 0
    mean = est_E(X, mu, sigma, Nsim)
    for _ in range(Nsim): 
        v += (X(mu, sigma) - mean)**2
    return v / Nsim

# Para el metodo polar que devuelve dos valores
def est_var2(X, mu, sigma, Nsim): 
    v = 0
    mean = est_E2(X, mu, sigma, Nsim)
    for _ in range(Nsim): 
        v += (X(mu, sigma)[0] - mean)**2
    return v / Nsim

# Estimador de la Desviacion Estandar
# Para el metodo de aceptacion-rechazo y el metodo de razon entre uniformes
def est_sd(X, mu, sigma, Nsim): 
    return math.sqrt(est_var(X, mu, sigma, Nsim))

# Para el metodo polar
def est_sd2(X, mu, sigma, Nsim):
    return math.sqrt(est_var2(X, mu, sigma, Nsim))

def main(): 
    Nsim = 10000
    mu, sigma = 0, 1
    
    print("Estimador de la Esperanza")
    print("Aceptacion-Rechazo: ", est_E(normal_aceptacion_rechazo_X, mu, sigma, Nsim))
    print("Polar: ", est_E2(metodo_polar_transformaciones_box_muller_X_Y, mu, sigma, Nsim))
    print("Razon entre Uniformes: ", est_E(normal_variate_razon_uniformes_X, mu, sigma, Nsim))

    print("Estimador de la Varianza")
    print("Aceptacion-Rechazo: ", est_var(normal_aceptacion_rechazo_X, mu, sigma, Nsim))
    print("Polar: ", est_var2(metodo_polar_transformaciones_box_muller_X_Y, mu, sigma, Nsim))
    print("Razon entre Uniformes: ", est_var(normal_variate_razon_uniformes_X, mu, sigma, Nsim))

    print("Estimador de la Desviacion Estandar")
    print("Aceptacion-Rechazo: ", est_sd(normal_aceptacion_rechazo_X, mu, sigma, Nsim))
    print("Polar: ", est_sd2(metodo_polar_transformaciones_box_muller_X_Y, mu, sigma, Nsim))
    print("Razon entre Uniformes: ", est_sd(normal_variate_razon_uniformes_X, mu, sigma, Nsim))

if __name__ == "__main__":
    main()