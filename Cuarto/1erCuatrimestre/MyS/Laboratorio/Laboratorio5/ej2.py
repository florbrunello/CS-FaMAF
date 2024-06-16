import random

# Ejercicio 2ai
def X(a=2): 
    U = random.random()
    return (1/U)**1/a

# Ejercicio 2aii

# Ejercicio b
def est_E(X, Nsim):
    e = 0
    for _ in range(Nsim):
        e += X()
    return e / Nsim

def main():
    print("Estimacion de E(X) - Distribucion Pareto")
    print("E(X) ≃ ", est_E(X, 10000))
    print("E(X) = 2.0")

if __name__ == '__main__':
    main()