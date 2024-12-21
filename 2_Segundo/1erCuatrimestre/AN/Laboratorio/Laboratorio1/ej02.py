"""
Ejercicio 2: 

Comprobar que el epsilon-maquina es 2-52 = 2.2204 * 10-16, escribiendo y comparando
las siguientes dos lineas de comando:
 a = 1 + 2**-53; b = a-1
 a = 1 + 2**-52; b = a-1
"""

# 1 / 2^52 > 1 / 2^53

a = 1 + 2 ** (-52)
b = a - 1
print(b)
print('')

a = 1 + 2 ** (-53)
b = a - 1
print(b)

""" El correcto es 2 ** (-52)
2.22044604925e-16

0.0
"""
