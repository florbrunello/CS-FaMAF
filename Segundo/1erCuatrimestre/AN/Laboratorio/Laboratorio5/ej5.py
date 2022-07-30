"""
Ejercicio 5: 
Calcular las siguientes integrales haciendo uso de la libreria scipy (explorar la funcion
integrate.quad) 
a) I = ∫ −∞ - ∞ e^(-x^2) dx,
b) I = ∫ 0 - 2 x^2 * log (x + √(x^2 + 1)) dx
"""

import scipy.integrate as scp
import numpy as np
#scipy.integrate.quad(func, a, b, args=(), full_output=0, epsabs=1.49e-08, epsrel=1.49e-08, limit=50, points=None, weight=None, wvar=None, wopts=None, maxp1=50, limlst=50): computes a definite integral.

#Inciso a

def funa(x): 
    return np.exp(-x**2)

Ia = scp.quad(funa,-np.inf,np.inf)

#Inciso b

def funb(x):
    root = np.sqrt(x**2+1)
    ln = np.log10(x+root)
    y = x**2 * ln
    return y

Ib = scp.quad(funb, 0, 2)

print(Ia)
print(Ib)