import random
import math

def est_pi():
    U = 2 * random.random() - 1
    V = 2 * random.random() - 1
    return (U**2 + V**2) <= 1

# Ejercicio a
def estimador_p(d=0.01): 
    p = 0
    n = 0
    while n <= 100 or math.sqrt(p * (1-p) / n) > d: 
        n += 1
        X = est_pi()
        p = p + (X-p) / n
    return p

# Ejercicio b
def estimador_p_IC(z_alfa_2=1.96, L=0.1):
    d = L / ( 2 * z_alfa_2 )
    p = 0
    n = 0
    while n <= 100 or math.sqrt(p * (1-p) / n ) > d:
        n += 1
        X = est_pi()
        p = p + (X - p) / n
    return p, n

def main():
    
    # Ejercicio a
    pi_a = estimador_p()
    print("Estimacion de pi: ", 4*pi_a)

    # Ejercicio b
    pi_b, n = estimador_p_IC()
    print("Estimacion de pi: ", 4*pi_b)
    # IC = (X - 1.96 * Raiz(X*(1-X)/n) , X + 1.96 * Raiz((X*(1-X))/n)
    aux = math.sqrt(pi_b*(1-pi_b)) / math.sqrt(n)
    inf = (4*pi_b - 1.96 * aux)
    sup = (4*pi_b + 1.96 * aux)
    print("IC del 95% para pi: (", inf, ",", sup, ")")
    print("Son necesarias ", n, " muestras ejecuciones para obtener el IC")

if __name__ == "__main__":
    main()