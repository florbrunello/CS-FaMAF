# Informe Laboratorio 3 - Planificador de procesos

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Bustos, Franco: franco.bustos@mi.unc.edu.ar
- Caldara, Marí­a Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Introducción](#introducción)
2. [Compilación](#compilación)
3. [Debugging](#debugging)
4. [Estudiando el planificador de xv6](#estudiando)
    - [Primera Parte](#primera-parte)
    - [Segunda Parte](#segunda-parte)
    - [Tercera Parte](#tercera-parte)
    - [Cuarta Parte](#cuarta-parte)
5. [Técnicas y Herramientas de Programación](#técnicas)
6. [Conclusiones](#conclusiones)

### Introducción<a name="introducción"></a>

### Compilación<a name="compilación"></a>

### Debugging<a name="debugging"></a>

### Estudiando el planificador de xv6<a name="estudiando"></a>
#### Primera Parte

1) ¿Qué política de planificación utiliza xv6 para elegir el próximo proceso a ejecutarse? 
El sistema operativo xv6 utiliza la política de planificación Round Robin. Dedujimos esto a partir de la función _scheduler()_, la cual recorre un arreglo de procesos llamado 'proc' que almacena estructuras de datos de tipo _struct proc_ y los ejecuta por un segmento de tiempo (quantum). 
Para seleccionar el proceso a ser ejecutado, se chequea el primero cuyo estado sea RUNNABLE. Luego se cambia su estado a RUNNING y ocurre un context switch, implementado en la función _swtch_. Una vez hecho el context switch, comienza a ejecutarse el proceso seleccionado y eventualmente, luego de un período de tiempo, su estado cambiará para así elegir el siguiente proceso con estado RUNNABLE.

2a) ¿Cuánto dura un quantum en xv6?
Un quantum dura 1000000 clocks, aproximadamente 1/10th segundos en qemu. Esta información la obtuvimos de la función _timeinit()_ en start.c, la cual es llamada en la función que analiza los traps a kernel: _kerneltrap()_. Esta última distingue los casos en los que se realizan traps, entre ellos, las interrupciones por tiempo.
Si ocurre una interrupción de tiempo y hay un proceso en estado RUNNING, se llama a la función _yield()_ y se cambia el estado del proceso para que se planifique otro. 

2b) ¿Cuánto dura un cambio de contexto en xv6?

2c) ¿El cambio de contexto consume tiempo de un quantum?

2d) ¿Hay alguna forma de que a un proceso se le asigne menos tiempo?
Vimos que el quantum dura 1000000 clocks, sin embargo, los procesos pueden dejar de ejecutarse antes de ese período de tiempo. En tal caso, se eligirá otro proceso a ejecutar durante el tiempo restante del primer proceso, es decir, el quantum no comenzará de cero. Una raźon por la que puede ocurrir un trap es que las interrupciones del dispositivo no estén habilitadas o que no esté en modo supervisor. 

#### Segunda Parte

#### Tercera Parte

#### CuartaParte

### Técnicas y Herramientas de Programación<a name="técnicas"></a>

### Conclusiones<a name="conclusiones"></a>