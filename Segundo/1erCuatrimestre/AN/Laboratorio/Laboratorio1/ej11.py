"""
Ejercicio 11:

Escribir dos funciones f(x) y g(x) que calculen:
    f(x) = px  2 + 1 - 1
    g(x) = x 2 √ x 2 + 1 + 1
    
Compruebe a mano que ambas expresiones son iguales y luego ejecute las siguientes instrucciones:
    for i in range(20):
    x = 8**-i
    print(f"f(x)={f(x)}, g(x)={g(x)}")
¿Ambas funciones devuelven los mismos resultados? ¿Cual es mas confiable?
"""

def f(x): 
    res = ((x**2+1)**(1/2)) - 1 
    return res

def g(x): 
    res = x**2 / (((x**2+1)**(1/2)) +1)
    return res

for i in range(20):
    x = 8**-i
    print(f"f(x)={f(x)},g(x)={g(x)}")

"""
for i in range(20): -> Son 20 numeros

f(x)=0.41421356237309515,g(x)=0.4142135623730951
f(x)=0.0077822185373186414,g(x)=0.0077822185373187065
f(x)=0.00012206286282867573,g(x)=0.00012206286282875901
f(x)=1.9073468138230965e-06,g(x)=1.907346813826566e-06
f(x)=2.9802321943606103e-08,g(x)=2.9802321943606116e-08
f(x)=4.656612873077393e-10,g(x)=4.6566128719931904e-10
f(x)=7.275957614183426e-12,g(x)=7.275957614156956e-12
f(x)=1.1368683772161603e-13,g(x)=1.1368683772160957e-13
f(x)=1.7763568394002505e-15,g(x)=1.7763568394002489e-15
f(x)=0.0,g(x)=2.7755575615628914e-17
f(x)=0.0,g(x)=4.336808689942018e-19
f(x)=0.0,g(x)=6.776263578034403e-21
f(x)=0.0,g(x)=1.0587911840678754e-22
f(x)=0.0,g(x)=1.6543612251060553e-24
f(x)=0.0,g(x)=2.5849394142282115e-26
f(x)=0.0,g(x)=4.0389678347315804e-28
f(x)=0.0,g(x)=6.310887241768095e-30
f(x)=0.0,g(x)=9.860761315262648e-32
f(x)=0.0,g(x)=1.5407439555097887e-33
f(x)=0.0,g(x)=2.407412430484045e-35

Va de i = 0 a i = 19 
- Para i = 1, tenemos x = 8 ^ (-1) = 1/8. 
- Para i = 9, tenemos x = 8 ^ (-9) = 1/8⁹.
    g(x)=2.7755575615628914e-17 = 2,77556 * 10 ^(-17)
    f(x) = 0

Las funciones no devuelven el mismo resultado. Es conveniente no hacer restas 
de números que en valor absoluto son tan parecidos porque para números muy 
próximos al cero, el redondeo...

import math 

def f(x):
    j = x**2+1
    res = math.sqrt(j) -1

    return res
"""