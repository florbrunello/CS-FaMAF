import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
import math

def exponencial_lamda(lamda):
    U = 1 - random.random()
    return -math.log(U) / lamda

# Simulación sistema de supermercado
def sim(N, S, M, Tf, Tr):
    # Inicialización de variables
    tiempo = 0
    n_defectuosas = 0
    # math.inf indica que un operario está libre
    tiempos_reparacion = [math.inf for _ in range(M)] 
    tiempos_fallo = [exponencial_lamda(1/Tf) for _ in range(N)]
    tiempos_fallo.sort()

    # Supermercado en funcionamiento
    while True:
        # Caso 1: se rompe una máquina antes que otra se repare
        if min(tiempos_reparacion) > tiempos_fallo[0]:
            # Registro del tiempo
            tiempo = tiempos_fallo[0]
            n_defectuosas = n_defectuosas + 1

            # Manejo de cajas de repuesto
            if n_defectuosas < S + 1:
                tiempos_fallo = tiempos_fallo[1:]
                tiempos_fallo.append(tiempo + exponencial_lamda(1/Tf))
                tiempos_fallo.sort()
                # Manejo de el/los operarios
                if math.inf in tiempos_reparacion:
                    i = tiempos_reparacion.index(math.inf)
                    tiempos_reparacion[i] = tiempo + exponencial_lamda(1/Tr)
            # Condición de fallo del sistema
            elif n_defectuosas > S:
                # Finaliza la simulación
                return tiempo 

        # Caso 2: se repara una máquina antes de que otra falle
        elif min(tiempos_reparacion) <= tiempos_fallo[0]:
            # Índice del operario que reparó la máquina
            i = tiempos_reparacion.index(min(tiempos_reparacion))
            # Registro del tiempo
            tiempo = tiempos_reparacion[i]
            n_defectuosas = n_defectuosas - 1
            # Si hay una máquina para reparar, se la asignamos al operario que reparó la máquina
            if n_defectuosas > 0:
                tiempos_reparacion[i] = tiempo + exponencial_lamda(1/Tr)
            # Si no, 'liberamos' al operario
            else:
                tiempos_reparacion[i] = math.inf

def metricas_i(N, S, M, Tf, Tr, long_interv, ej):

    # Generación de 10000 tiempos de fallo del supermercado 
    datos = [sim(N, S, M, Tf, Tr) for _ in range(10000)]
    
    # Cálculo de las métricas
    print(f"\nEjercicio {ej}:")
    print(f"   Esperanza = {np.mean(datos):.4f}")
    print(f"   Desvío estándar = {np.std(datos):.4f}")
    print(f"   Varianza = {np.var(datos):.4f}")
    print(f"   Mínimo = {min(datos):.4f}")
    print(f"   Máximo = {max(datos):.4f}")
    print(f"   Mediana = {np.median(datos):.4f}")

    # Generación de los intervalos para el histograma
    i = 0
    intervalos = []
    cota = max(datos)
    while i < cota:
        intervalos.append(i)
        i += long_interv
    intervalos.append(i)

    # Gráfico del histograma
    plt.figure(figsize=(10, 6))
    sns.histplot(datos, bins=intervalos, kde=True, color='blue')
    plt.title(f'Histograma de Tiempos de Fallo\n N={N} S={S} M={M}')
    plt.xlabel('Tiempo (meses)')
    plt.ylabel('Frecuencia')
    plt.savefig(f'ej{ej}_tiempos.png')

# metricas_i(N, S, M, Tf, Tr, long_interv, ej)

print(f"Métricas obtenidas con valores de 10000 simulaciones de tiempos de fallo")
# Ejercicio 1
metricas_i(7, 3, 1, 1, 1/8, 0.6, 1)

# Ejercicio 2
metricas_i(7, 3, 2, 1, 1/8, 3, 2)

# Ejercicio 3
metricas_i(7, 4, 1, 1, 1/8, 0.9, 3)