from random import expovariate
from random import random
import numpy as np
import math

# Integral Monte Carlo en el intervalo (0,1)
def MonteCarlo_01(fun, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(random())
    return Integral/Nsim

# Integral Monte Carlo en el intervalo (a,b)
def MonteCarlo_ab(fun, a, b, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(a + (b-a)*random())
    # Aquí multiplico una sola vez por (b-a)
    return Integral*(b-a)/Nsim 

# Integral Monte Carlo en el intervalo (0,inf)
def MonteCarlo_inf(fun, Nsim):
    Integral=0
    for _ in range(Nsim):
        u=random()
        Integral+= fun(1/u-1)/(u**2)
    return Integral/Nsim

# Ejercicio a

def g_a(u):
  return (1 - u**2)**(3/2)

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
  print('Integral para Nsim =',N[i])
  print(MonteCarlo_01(g_a,N[i]))
  print('-------------------')
print('El valor real aproximado es 3pi/16 ~',3*np.pi/16)

# Ejercicio b

def g_b(u):
  return (u/(u**2 - 1))

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
  print('Integral para Nsim =',N[i])
  print(MonteCarlo_ab(g_b,2,3,N[i]))
  print('-------------------')
print('El resultado exacto es ln(8/3)/2',np.log(8/3)/2)

# Ejercicio c

def g_c(u):
  return u/((u**2 + 1)**(2))

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
  print('Integral para Nsim =',N[i])
  print(MonteCarlo_inf(g_c,N[i]))
  print('-------------------')
print('El valor exacto es 1/2')

# Ejercicio d

def g_d(u):
  return 2*np.exp(-u**2)

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
  print('Integral para Nsim =',N[i])
  print(MonteCarlo_inf(g_d,N[i]))
  print('-------------------')
print('El valor exacto es sqrt(\pi) ~',math.sqrt(np.pi))

# Integrales múltiples, 2 variables

# Integral Monte Carlo en el intervalo (0,1)x(0,1)
def MonteCarlo_01_2(fun, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(random(), random())
    return Integral/Nsim

# Integral Monte Carlo en el intervalo (a,b)x(c,d)
def MonteCarlo_ab_2(fun,a,b,c,d, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(a + (b-a)*random(), c + (d-c)*random())
    return Integral*(b-a)*(d-c)/Nsim

# Integral Monte Carlo en el intervalo (0,inf)x(0,inf)
def MonteCarlo_inf_2(g, Nsim):
    Integral=0
    for _ in range(Nsim):
        u1=random()
        u2=random()
        Integral+= g(1/u1-1, 1/u2-1)/((u1**2)*(u2**2))
    return Integral/Nsim

# Ejercicio e

def g_e(u,v):
  return np.exp((u + v)**2)
    
N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
  print('Integral para Nsim =',N[i])
  print(MonteCarlo_01_2(g_e,N[i]))
  print('-------------------')
print('El valor exacto es 4.89916 por wolfram alpha')

# Ejercicio f

def I(x, y):
    if y < x:
        return 1
    else:
        return 0

def g_f(x, y):
    return np.exp(-(x+y))*I(x, y)

N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
  print('Integral para Nsim =',N[i])
  print(MonteCarlo_inf_2(g_f,N[i]))
  print('-------------------')
print('El valor exacto es 1/2')
     