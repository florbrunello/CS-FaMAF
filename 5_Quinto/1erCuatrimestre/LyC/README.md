##  Trabajo individual de la materia Lenguajes y Compiladores
#### Alumna: Brunello Florencia

Este repositorio contiene la resolución del laboratorio individual de la materia Lenguajes y Compiladores cuyo objetivo es implementar la semántica denotacional para el lenguaje imperativo simple con fallas (LIS + Fallas) utilizando el lenguaje Haskell.
La implementación se encuentra en el archivo lab.hs, el cual modela expresiones enteras, booleanas y comandos del lenguaje, dandoles semántica mediante funciones en Haskell. Además, se incluye el tratamiento de fallas mediante construcciones como Fail y Catch que permiten representar errores y recuperarse de ellos dentro del flujo de ejecución del programa.
Para lograr esto, se definen funciones auxiliares de control que permiten propagar y restaurar correctamente el estado del programa durante la ejecución, respetando el comportamiento esperado de cada construcción semántica.