import random
import math

def poisson_homogeneo(lamda, T):
    eventos = []
    t = -math.log(1 - random.random()) / lamda
    while t <= T:
        eventos.append(t)
        t += -math.log(1 - random.random()) / lamda
    return len(eventos), eventos

def llegada_aficionados(): 
    # Cantidad de aubotuses que llegaron en una hora 
    # Tiempo de llegada de cada uno 
    num_autobuses, tiempos = poisson_homogeneo(lamda=5, T=1)
    aficionados = []

    # Cantidad de aficionados que llegaron en cada autobus
    for i in range(num_autobuses):
        num_aficionados = random.randint(20, 40)
        aficionados.append(num_aficionados)

    return aficionados, tiempos

# Otra version
def llegada_aficionados_v2():
    num_autobuses = poisson_homogeneo(lamda=5, T=1)[0]
    aficionados = [0] * num_autobuses

    for i in range(num_autobuses):
        aficionados[i] = random.randint(20, 40)

    return aficionados, sum(aficionados)

def main():
    print("Version 1:")
    aficionados, tiempos = llegada_aficionados()
    print("Aficionados por autobus:")
    print(aficionados)
    print("Tiempo de llegada de cada autobus:")
    print(tiempos)

    print("\nVersion 2:")
    aficionados, total_aficionados = llegada_aficionados_v2()
    print("Aficionados por autobus:")
    print(aficionados)
    print("Total de aficionados:")
    print(total_aficionados)

if __name__ == "__main__":
    main()
