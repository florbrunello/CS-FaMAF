# Informe Laboratorio 1 - MyBash
### Programando nuestro propio shell de Linux

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Bustos, Franco: franco.bustos@mi.unc.edu.ar
- Caldara, María Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Introducción](#introducción)
2. [Compilación y decisiones de implementación](#compilación-y-decisiones-de-implementación)
3. [Modularización](#modularización)
4. [Técnicas de Programación](#técnicas-de-programación)
5. [Herramientas de Programación](#herramientas-de-programación)
6. [Comentarios finales](#comentarios-finales)
7. [Conclusiones](#conclusiones)

#### Introducción 
La idea de este proyecto consiste en codificar un shell al estilo de bash (Bourne Again SHell), con el objetivo de ejecutar comandos simples en modo foreground y background, teniendo la posibilidad de redirección de entrada y salida estándar. Además, se implementa una tubería de comandos(pipe), la cual nos permite enlazar y ejecutar hasta dos de ellos. 
Los detalles de la organización del trabajo se encuentran en los siguientes apartados. 

#### Compilación y decisiones de implementación

* ¿Cómo compilar?

Para compilar los códigos que se encuentran en los diferentes módulos, deberá estar situado dentro de la carpeta principal y luego correr el comando _make_ en la terminal. Una vez compilado, se ejecuta el programa con _./mybash_ .

* Implementación

En cuanto a las decisiones de implementación, antes de empezar a trabajar, establecimos ciertos criterios para obtener un código uniforme y legible. 
Dado que nuestro mybash es más limitado que el bash de la terminal, decidimos diferir del mismo en el funcionamiento de ciertos comandos, según lo que creímos conveniente. Estos son: 
.Ignoramos si los comandos internos tienen redirección I/O. 
.En la ejecución de múltiples comandos, como se utilizan redirecciones, decidimos que no funcione con comandos builtin. 


* Debugging
Para corroborar que las implementaciones funcionaran de forma correcta, utilizamos la test-suite otorgada por la cátedra, la cual testea módulos por separado y el programa completo. Para correr el test completo, ejecutamos _make test_. Luego, cada módulo tiene su respectivo test aislado. Por ejemplo, _make test-command_ para el TAD Command, _make test-parsing_ para el parsing, entre otros. 

* Memory Leaks

Para chequear posibles memory leaks, utilizamos _make memtest_, ubicado en el Makefile de tests que nos brindó la cátedra, el cual utiliza valgrind y nos permite visualizar los bloques de memoria que fueron pedidos pero nunca liberados.

* Ejemplos de funcionamiento de mybash:

._~/mybash>/home/user/so22lab1g05$ help_ Retorna:
    Shell: mybash, versión 1.0.
    Autores: Florencia Brunello, Franco Bustos, María Emilia Caldara, Andrés Ferrero.
    Los comandos internos son:
        cd [dir]:
            Modifica el directorio de trabajo del shell.
            Modifica el directorio actual a DIR. 
            DIR por defecto es el valor de la variable de shell HOME.
        help:
            Muetra información sobre la shell y sus autores,
            además de una breve descripción de todos sus comandos internos.
        exit:
            Sale del intérprete de ordenes.

._~/mybash>/home/user/so22lab1g05$ cd tests_ Retorna: ~/mybash>/home/maria/so22lab1g05/tests$ 

._~/mybash>/home/user/so22lab1g05$  echo hola > hola.txt | cat < hola.txt_ Retorna: hola 

._~/mybash>/home/user/so22lab1g05$ hola_ Retorna: Orden no encontrada

._~/mybash>/home/user/so22lab1g05$ cat >_ Retorna: mybash: error sintáctico cerca del elemento inesperado 'newline'

._~/mybash>/home/user/so22lab1g05$ ls -l | wc_ Retorna:  35     308    1832
 
._~/mybash>/home/user/so22lab1g05$ pi 10000000 &_ Retorna: ~/mybash>/home/user/so22lab1g05$ 

._~/mybash>/home/user/so22lab1g05$ ls -l | grep command | sort -n -r -k 5 | head -n 1 > example.txt_ 
 _~/mybash>/home/user/so22lab1g05$ cat example.txt_ Retorna: -rw-rw-r-- 1 user user 26248 sep 19 18:00 command.o



#### Modularización
La modularización del trabajo consta de 6 módulos: mybash, command, parsing, parser, execute  y builtin. A continuación, la funcionalidad de cada uno de ellos. 

##### MyBash
Es el módulo principal. Utiliza todos los módulos en conjunto, y es el encargado de estar a la espera de un comando a ejecutar a través de la entrada estándar. 

##### Command 
Es el módulo que posee las implementaciones de los TADs scommand (comando simple) y pipeline (secuencia de comandos simples separados por pipe). Su función es representar y manipular comandos. Primero se diseñó la estructura que representa a cada TAD. Para el caso de scommand, creamos una estructura cuyos elementos son un puntero a un comando, junto a sus argumentos, y dos punteros para las redirecciones, una de entrada y otra de salida. Por otro lado, la estructura del pipeline consta de un puntero a una lista de comandos simples y un booleano que indica si el shell debe esperar la terminación del comando antes de permitir ejecutar uno nuevo.
A la hora de implementar las funciones de los TADs, nos basamos fuertemente en los requisitos y garantías que debía cumplir cada función. Asimismo, hicimos uso de las librerias glib, string y dos funciones brindadas por la cátedra (cuya implementación se encuentra en el archivo strextra.c). 

##### Parser 
Módulo previamente compilado, otorgado por la cátedra. Provee funciones necesarias para implementar el módulo parsing.

##### Parsing 
Este módulo corresponde al parseo de un comando, es decir, a leer el comando ingresado por el usuario y armar la estructura de datos correspondiente que nos sirve para implementar la shell. 
Decidimos modularizar parse_pipeline (dada en el .h), agregando una función que parsee un solo comando y que devuelva la estructura scommand. Dado que la función parse_pipeline usa el TAD Parser, el módulo parsing lo implementamos usando las funciones provistas por la cátedra en el módulo parser.h.
En cuanto a la robustez del bash, decidimos que en casos de recibir una entrada inválida formada por un comando y un pipeline, no actúe como la shell la cual espera para recibir el siguiente comando. En particular, preferimos volver a mostrar el prompt. 

##### Builtin 
Implementa las funciones que ejecutan los comandos internos, en mybash son _cd_, _exit_ y _help_. Decidimos modularizar la función builtin_is_internal y crear tres nuevas funciones: builtin_is_exit, builtin_is_cd, builtin_is_help; las cuales, como sus nombres indican, señalan si un comando es exit, cd o help. 

##### Execute 
Este módulo es el encargado de ejecutar el comando que ingresa el usuario y para ello se realizan las llamadas a sistema. En el mismo, se desarrollan los contenidos más interesantes para aprender del proyecto. Para poder ejecutar la función execute_pipeline, cuyo prototipo se encuentra en execute.h, creamos funciones auxiliares, donde en ellas se redirigen entradas y salidas, se arma el arreglo para poder llamar a la función execvp, se ejecuta un comando simple y por último, la que se encarga de ejecutar múltiples comandos.

#### Técnicas de Programación
Las técnicas de programación fueron variando según las tareas asignadas. 
La primera semana de trabajo implementamos las funciones de command.c. Decidimos dividir el trabajo individualmente y una vez finalizado, hicimos una puesta en común para entender el funcionamiento de todo el TAD. 
Luego, debido a la complejidad de lo que debíamos implementar, como fue el caso del módulo parsing, decidimos comenzar a trabajar en grupos de dos (pair programming). En particular, Florencia y María implementaron parsing.c mientras que Andrés y Franco debuggearon command.c. 
Finalmente, la implementación del execute.c constó de varios días de trabajo en grupo. Este lo fuimos construyendo de a poco, comenzando por implementar una función que ejecute un único comando hasta llegar a la implementación de múltiples comandos. 

#### Herramientas de Programación
A lo largo de las semanas hicimos uso de muchas herramientas. La principal fue Bitbucket, donde quedó plasmado a través de commits el trabajo de cada integrante. Paralelamente, hicimos reuniones presenciales y virtuales, por Discord, Google Meet y Zulip. Para interiorizarnos en el desarrollo de algunas funciones, decidimos apoyarnos en videos de Youtube, material escrito y enlaces provistos por la cátedra.  

#### Comentarios finales
Un reporte que podemos hacer en cuanto a los memory leaks es que, por la manera en que están optimizados los TADs de Glib (biblioteca externa), aparecen bytes en la categoría still reachable. Es por ello que usamos la flag -g para poder distinguir cuándo estos leaks refieren a esta librería y cuándo provienen de nuestras implementaciones. 
Como puntos estrella, imprimimos un prompt con el nombre del host, nombre de usuario y camino absoluto, cuyo código se encuentra en el archivo prompt.c. Además, implementamos la ejecución de múltiples comandos usando pipes. 

#### Conclusión
Este trabajo nos da una noción de cómo funcionan los procesos en un sistema operativo, y nos da mayor entendimiento sobre cómo funciona una shell.
Aprendimos a usar llamadas a sistema y cómo funcionan, entender cómo se redireccionan archivos, distinguir cómo se ejecuta un proceso hijo y las diferencias que hay con un proceso padre; también cómo se conectan procesos mediante una tubería, entre otras. 
Además, el hecho de que el trabajo sea grupal nos ayuda a poder interactuar con otras personas, aprender a interpretar e intercambiar ideas, organizar y delegar trabajos, teniendo nuestro primer contacto con un proyecto de complejidad mayor a la que trabajamos en el resto de la carrera. Estamos conformes con el funcionamiento de nuestro mybash y con los conocimientos que hemos adquirido a lo largo de estas semanas. Proyectos como este nos recuerdan la importancia del trabajo en conjunto, herramienta clave para nuestro futuro como programadores/investigadores.