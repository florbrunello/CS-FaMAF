import random
import math

#Ejercicio b
def Cauchy_c(): 
    c = 1 / math.sqrt(math.pi)
    while True: 
        # Genera valores entre 0 y c
        u = random.random() * c
        # Genera valores entre -c y c
        v = (random.random() - 0.5) * 2 * c
        if u**2 + v**2 < c**2:
            return v / u
    
# Metodo de razon entre uniformes
def Cauchy():
    while True: 
        u = random.random()
        v = (random.random() - 0.5) * 2
        if u**2 + v**2 < 1:
            return v / u
        
# Ejercicio c
def cauchy_lamda(lamda):
    return lamda * Cauchy()

# Ejercicio d
def est_P(X, lamda, Nsim):
    p = 0
    for _ in range(Nsim):
        x = X(lamda)
        if -lamda < x and x < lamda:
            p += 1
    return p / Nsim

def main(): 
    Nsim = 10000
    print("Estimacion de la probabilidad que el valor generado caiga en (-lamda,lambda)")
    print("Estimacion de P lamda = 1: ", est_P(cauchy_lamda, 1, Nsim))
    print("Estimacion de P: ", est_P(cauchy_lamda, 2.5, Nsim))
    print("Estimacion de P: ", est_P(cauchy_lamda, 0.3, Nsim))
    print("Probabilidad Teorica: 0.5")

if __name__ == "__main__":
    main()