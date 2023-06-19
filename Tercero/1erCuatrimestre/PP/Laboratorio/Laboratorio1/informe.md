# Informe Laboratorio 1- Programación Funcional 

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Caldara, Marí­a Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Preguntas](#preguntas)
2. [Conclusiones](#conclusiones)

### Preguntas<a name="preguntas"></a>
1. ¿Por qué están separadas las funcionalidades en los módulos indicados? Explicar detalladamente la responsabilidad de cada módulo.
Los módulos separan funcionalidades con el objetivo de poder abstraer la implementación, de esta manera podemos enfocarnos únicamente en una tarea específica. Esta forma genera un código más ordenado y flexible ante posibles modificaciones y soluciones de errores.
En este caso los módulos están separados según las siguientes funcionalidades:

- Sintaxis: La sintaxis está implementada en el módulo _Dibujo.hs_. Se encarga de definir la 'forma' en cómo se deben estructurar las expresiones que representan un dibujo. Se define la gramática de un lenguaje específico, en este caso, para representar cosas del tipo Dibujo.

- Semántica: La semántica del programa está implementada en el módulo _Interp_. Se encarga de representar el Dibujo descripto en una imagen. Para ello se utiliza la librería _Gloss_ que dados ciertos vectores y funciones, renderiza y muestra por pantalla una imagen del dibujo especificado. 
Este módulo hace una interpretación general sobre el dibujo, por lo tanto interpreta únicamente las funciones definidas en el lenguaje y no se encarga de las figuras básicas.
La interpretación de mi dibujo completo se hace de manera recursiva, modificando los vectores que me definen mi figura básica según la funciones constructoras que se hayan utilizado. Al modificar vectores, la imagen cambiará de acuerdo a ellos. 
_initial_ se encarga de desplegar la configuración de un dibujo en pantalla. 

- Aplicación: Son los usos propios de los módulos descriptos anteriormente. Son dibujos que van a aparecer en pantalla. Están implementados en _Escher.hs_, _Feo.hs_, etc. Estos ejemplos ensamblan y conectan la sintaxis y semántica.  
En estos casos, un dibujo consta de tres partes. Por un lado, se utiliza el lenguaje y las funciones constructoras definidas en _Dibujo.hs_. Es aquí donde se va a especificar el tipo de dato de las figuras básicas.
Por ejemplo, si mi figura va a tener círculos y cuadrados, entonces el tipo de dato será 
data Basica = Circulo | Cuadrado
y a partir de ellas voy a definir mi dibujo. Por ejemplo 
rotar(figura(Circulo)). 
Cabe notar que únicamente en este ítem se utiliza la gramática del lenguaje. 
Por otro lado, debemos dar la interpretación de las figuras básicas usando librería Gloss.
Como cada dibujo depende de las básicas, y estas pueden ser de cualquier tipo, entonces debo definir como se debe interpretar a cada una de ellas.
Una observación es que esta interpretación no se hace en el módulo Interp, pues de hacerlo limitaría la capacidad de cosas que puedo representar y dibujar. Por lo tanto, este módulo está definido para interpretar únicamente las operaciones del lenguaje. 
Luego esta función va a ser utilizada como argumento para la interpretación del dibujo completo.
Por último, debo dar una configuración del dibujo, que se trata de una estructura de dato que representará mi dibujo, asignándole un nombre y su interpretación. 

- _Pred.hs_: Este módulo no es utilizado para formar el dibujo (pero sí en los tests). Sin embargo, tiene funciones de predicados sobre dibujos, que probamos en el test.

- _Main.hs_: Es el módulo principal. Tiene incluídos todos los módulos nombrados anteriormente. Se encarga de ejecutar el dibujo que se le pase como parámetro, o de listar los dibujos disponibles con la flag _'--lista'_


2. ¿Por qué las figuras básicas no están incluidas en la definición del lenguaje, y en vez es un parámetro del tipo?
El tipo polimórfico de datos "Dibujo" se utiliza para representar cualquier tipo de dibujo, independientemente de su contenido o forma. Aunque el tipo "Dibujo" define la estructura básica para representar un dibujo, no especifica qué figuras o elementos se deben utilizar para construirlo.
Por lo tanto, es responsabilidad del usuario definir qué figuras básicas se utilizarán para construir el dibujo. Esto se hace al crear uno nuevo, ya que es en ese momento cuando se definen las figuras y los elementos que se utilizarán para construirlo.
Las figuras básicas se definen al crear un nuevo dibujo y no en el módulo que define las operaciones del lenguaje porque el tipo "Dibujo" es polimórfico y genérico, y no especifica las formas y elementos necesarios para construir un dibujo específico.
El módulo de operaciones del lenguaje _Dibujo.hs_, por su parte, se encarga de proporcionar las herramientas necesarias para manipular y transformar los dibujos, independientemente de cómo se hayan construido.
Además, en el caso de que Dibujo no sea polimórfico,  si definimos las figuras básicas como parte del lenguaje, estaríamos limitando la variedad de dibujos que podríamos crear. Por ejemplo, si solo pudiéramos crear dibujos con círculos, rectángulos y líneas, sería imposible crear dibujos más complejos, como retratos de personas o paisajes naturales.
Por lo tanto, es mucho mejor definir las figuras básicas como parte del dibujo en sí, en lugar de limitarnos a un conjunto fijo de formas y estructuras predefinidas. 


3. ¿Qué ventaja tiene utilizar una función de `fold` sobre hacer pattern-matching directo?
La ventaja que tiene utilizar la función fold sobre hacer pattern-matching directo es que permite expresar la operación de reducción (por ejemplo suma, producto, concatenaciones, etc) de forma más  abstracta, pudiendo así reutilizar código.
Además, al no cubrir casos como pattern-matching, es menos propensa a errores ya que la corrida de la misma se hace una vez, mientras que la otra forma requiere recorrer la estructura de datos reiteradas veces para verificar patrones y aplicar operaciones en los sucesivos pasos. 


### Conclusiones<a name="conclusiones"></a>
En este proyecto de laboratorio, hicimos mucho más que un simple dibujo del estilo de Escher. Podemos decir que construimos un "lenguaje" que interpreta y construye dibujos. Es decir, en Dibujo.hs, tenemos las "reglas", las "bases" constructoras. En Interp.hs tenemos la interpretación, la construcción de esas bases. Y esto, en conjunto, forma algo muy poderoso: nos permite dibujar lo que queramos, nos da la libertad para poder elegir y construir la figura que sea. En otras palabras, podemos afirmar que el conjunto de módulos, forman un pseudo-compilador de dibujos, usando Gloss como herramienta.
De este lab, nos quedamos con la experiencia de haber hecho un proyecto de alto nivel en Haskell, explotando las ventajas del paradigma funcional, conociendo aspectos interesantes del mismo, y aprendiendo muchas cosas nuevas.