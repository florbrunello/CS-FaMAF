# Informe Laboratorio 2 - Semáforos en XV6 

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Bustos, Franco: franco.bustos@mi.unc.edu.ar
- Caldara, Marí­a Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Introducción](#introducción)
2. [Compilación](#compilación)
3. [Implementación y Estructura de Datos](#implementación-y-estructura-de-datos)
4. [Funcionamiento de syscalls xv6](#funcionamiento-de-syscalls-xv6)
5. [Funcionamiento de pingpong](#funcionamiento-de-pingpong)
6. [Debugging](#debugging)
7. [Técnicas y Herramientas de Programación](#técnicas-y-herramientas-de-programación)
8. [Conclusiones](#conclusiones)


### Introducción<a name="introducción"></a>
Este proyecto consiste en la implementación de un sistema de semáforos para el sistema operativo xv6. Un semáforo es una herramienta que nos permite controlar la ejecución de los procesos y el acceso a algún recurso en común con el fin de evitar problemas de concurrencia.
Para ello, definimos cuatro funciones (syscalls), donde cada una de ellas nos permite una operación en un semáforo. A continuación, explicaremos cómo implementamos el proyecto para que esto sea posible. 

### Compilación<a name="compilación"></a>
Para correr el SO xv6, es necesario tener instalado el emulador Qemu.
Además, por problemas de compilación en la computadora de uno de nuestros compañeros, decidimos usar una versión mas vieja de xv6. Esta es: https://github.com/mit-pdos/xv6-riscv.git

* ¿Cómo compilar?
Se compila y ejecuta xv6, con el comando _make qemu_.

### Implementación y Estructura de Datos<a name="implementación-y-estructura-de-datos"></a>
La implementación del semáforo consiste en 4 syscalls, que están definidas en sem.c, dentro de kernel. En espacio user, decidimos crear un programa de usuario _pingpong_, que se encuentra en pingpong.c . El mismo imprime ping y luego pong en consola una cantidad de veces definida por un _rally_ dado por el usuario. 

##### Decisiones de Implementación
- Para la escritura del código, decidimos respetar la estructura de xv6, que pudimos analizar observando el resto de los archivos.

- Para las syscalls, cuando se ejecutan con éxito, devuelven una variable entera con valor 1 (Salvo sem_open()). En caso de error, retornan 0.

- Estructura de datos del semáforo: Decidimos implementarlo con una capacidad máxima de 100 semáforos, en un arreglo global en memoria estática (Como está en espacio kernel, no nos tenemos que preocupar por el acceso a esta variable desde otros programas), donde cada posición del mismo representa un semáforo, y un lock que declaramos de manera global. También utilizamos una variable global sem, que nos sirve para mantener el channel adecuado entre sleep() y wakeup() dentro de sem_down y sem_up.

- Con respecto al sem_open(), decidimos que solamente reciba un solo argumento, que es el valor arbitrario con el que queremos inicializar el semáforo. Y que en caso de que la llamada se realice correctamente, devuelva la posición del lugar donde se guardó dicho semáforo + 1 (+1 permite que en caso de error, retorne 0). De esta forma, basta con hacer:
```c
int sem_example;
int value = _valor_arbitrario_;
sem_example = sem_open(value);
```
Así, _sem\_example_ es un nuevo semáforo que ya puede ser usado para las demás syscalls. Decidimos implementarlo de esta manera por las siguientes ventajas:
    - **Flexibilidad**. Los procesos no necesitan antes de ser ejecutados saber que semáforos están abiertos y cuales no, pues sem_open busca automaticamente un lugar donde guardalos. Así, se pueden crear múltiples programas sin necesitar una tabla en la cual comprobar si se están guardando los semáforos en una posición correcta.
    - **Evita errores**. Los semáforos se van abriendo y cerrando con el tiempo. Puede ocurrir que dos programas utilicen una misma posición de semáforo para hacer sem_open(). Mientras se ejecuten en tiempos distintos, no hay ningún problema. Pero puede llegar a ocurrir errores si se ejecutan a la vez.
    - **Seguridad**. El espacio de Kernel es un lugar restringido para el usuario, no vemos conveniente que desde el espacio de usuario se puedan ir modificando libremente las variables que se encuentran en espacio de kernel, como es el caso del arreglo donde se encuentras los valores de cada semáforo. Mejor que el kernel sea el que se encargue de las tareas del espacio kernel.

- El valor que devuelve sem_open() en espacio user no es directamente el valor de la posición del arreglo de semáforos del espacio kernel, para que coincidan se ven forzados a pasar a través de una función lineal (f(x) = x - 1). Esto es consecuencia de la implementación de sem_open(), que no puede devolver -1 en caso de error (Todas las syscall devuelven un entero positivo).

- Con respecto al sem_close(), inicializamos todos los semáforos en -1, y con este valor los interpretamos como "cerrados". De esta manera nos aseguramos de no hacer sem_open() a un semáforo que ya estaba abierto (decimos abierto cuando su valor es >=0) y en las demás syscall, verificar que no se está trabajando con un semáforo cerrado. Añadimos esta solución ya que no nos parecía correcto la ambigüedad de comportamiento que generaba hacer open a un semáforo abierto o hacer sem_up/sem_down a uno cerrado. De este modo, lo único que hace sem_close() es asignarle -1 como valor al semáforo que se desea cerrar. Es recomendable utilizar sem_close() únicamente cuando estemos seguros de que ningún otro proceso esté utilizando el semáforo mandado como argumento, para así evitar errores inesperados. 

##### Funcionamiento del semáforo
- No toma valores negativos, su valor mínimo es 0.
- Bloquea al proceso cuando el semáforo está valiendo 0 e intentamos hacer sem_down. En cualquier otro caso, la decrementación es natural.
- Se desbloquean los procesos que fueron bloqueados por sem_down, si es que el semáforo vale 0. Luego se incrementa el valor siempre.

### Funcionamiento de syscalls xv6 <a name="funcionamiento-de-syscalls-xv6"></a>
- acquire(): Mediante un lock, su función es limitar la ejecución de un proceso que accede a datos compartidos, haciendo que corra en un único CPU, evitando así problemas de concurrencia y que varios procesos compartan el mismo recurso. De esta manera, si declaramos acquire(&lock), estamos iniciando una parte del código llamado sección crítica. De esta forma, si otro proceso quiere usar el mismo recurso que está usando el proceso que llamó al lock, deberá esperar hasta que el lock sea liberado para poder usarlo. 
Se utilizó esta syscall en partes del proceso donde había que realizarle modificaciones al arreglo de semáforos, asegurándonos así de que no haya otro proceso que pueda realizarle otras modificaciones al mismo tiempo.  

- release(): Recibe como parámetro un lock. Con la llamada a esta syscall, se libera el lock (sección crítica) del código que había sido inicializada con acquire(). Una vez liberado, los demás procesos pueden utilizar el recurso. 

- sleep(): Recibe como parámetro un void *, también llamado channel, que es un valor identificatorio que toman los procesos, y como segundo parámetro, un struct spinlock. sleep() pone "a dormir" al proceso que realizó la syscall, relacionandolo además con el channel que utiliza como argumento, y libera el lock que tomó como argumento. Esto último implica que, cuando un proceso se deja de ejecutar, le da el control a otro para que pueda correr y así evitar los deadlocks. Esta llamada se utiliza en situaciones donde hay un proceso que quiere acceder a un recurso que está siendo utilizado por otro y tiene un lock, como no puede acceder, entonces debe esperar a que el otro proceso lo libere.  

- wakeup(): Tiene como parámetro un channel, donde pone en estado RUNNABLE(listo para ejecutarse) a todos los procesos que se encuentren en el mismo. Es decir, "despierta/desbloquea" los procesos a los que se les hizo un sleep(). En el caso de que se haga wakeup() a un proceso que ya se encontraba listo para ejecutarse, la syscall no hace nada.

- argint(): Tiene 2 parámetros. El primero es el n.º del parámetro que queremos que reciba la función. El segundo es un puntero a la variable donde se va a guardar el valor. Su función es hacer que se guarde el n-ésimo argumento de la función en una variable que definimos dentro del programa. Debido a que las syscalls en xv6 están definidas con parámetro (void) en _syscalls.c_, con el fin de proteger el kernel de algún parámetro inadecuado pasado por el usuario, decidimos hacerlo de la misma manera, y usar argint() para guardar los parámetros que le da el usuario. En otras palabras, esta función nos sirve como herramienta para "transformar" variables a parámetros ya que no los podemos definir directamente en la declaración de la syscall.

### Funcionamiento de pingpong<a name="funcionamiento-de-pingpong"></a>
Para implementar el programa pingpong accedimos, desde el espacio de usuario, a las syscall previamente explicadas. El programa debe escribir por stdout "ping" y "pong" la cantidad de veces que dicten el rally (argumento que toma el comando pingpong).
Lo primero que hicimos fue definir dos semáforos, uno llamado sem_ping, el cual corresponderá con el proceso padre, y otro sem_pong, quien corresponderá con el proceso hijo. Luego, al llamar a sem_open, asignamos 1 como valor al contador de sem_ping, y 0 al contador de sem_pong, pues queremos que primero se imprima "ping". 
Una vez hecho el fork, ambos procesos comienzan a correr. Por un lado, la implementación del proceso padre consta de un bucle determinado por el rally, pues queremos imprimir rally veces la cadena "ping". En la primer iteración imprime ping una única vez y automáticamente habilita a sem_pong mediante la llamada a sem_up. Luego, en la próxima iteración del bucle, sem_ping quedará bloqueado, que será habilitado por el proceso hijo una vez haya imprimido pong. La implementación del proceso hijo es similar. Esta también consta de un bucle que, en la primer iteración imprime pong, luego desbloquea ping y vuelve a bloquearse para "darle paso" a ping nuevamente. 
Una vez finalizadas las rally iteraciones en ambos procesos, en caso de no haber habido errores se cierran ambos semáforos. Por el contrario, si hubieron errores ya sea luego de hacer una system call o fork, se imprimirá un mensaje.
Notar que cuando despertamos al otro proceso con sem_up, luego volvemos a bajar su semáforo con sem_down, esto es así porque queremos que los semáforos siempre estén a un solo sem_down de bloquear al proceso que "corresponde a su semáforo".

### Debugging<a name="debugging"></a>
Contábamos con la herramienta gdb, pero dado que se nos informaba por stdout cuando sucedía un error grave y cual era, decidimos debuggear mediante printf, ya sea en el espacio user o espacio kernel. Nos informabamos de los valores de nuestras variables en un momento dado a través de esta función y así podíamos darnos cuentas que era en realidad lo que estaba sucediendo.

### Técnicas y Herramientas de Programación<a name="técnicas-y-herramientas-de-programación"></a>
La principal herramienta de trabajo fue Bitbucket, donde quedó plasmado a través de commits el trabajo de cada integrante. Para interiorizarnos en el funcionamiento de xv6, usamos su documentación y nos apoyamos en videos de Youtube y enlaces provistos por la cátedra.
Como técnica de programación decidimos dividirnos el trabajo haciendo pair programming. Luego compartimos los conocimientos entre las parejas.

### Conclusiones<a name="conclusiones"></a>
En este trabajo profundizamos conocimientos sobre cómo interactúan procesos con los recursos y los problemas que conlleva el multiprocesamiento, con concurrencia y demás. Incorporamos términos como _lock_, _sección crítica_, _lost wakeup_ ,_deadlock_, y también aprendimos sobre el funcionamiento de syscalls _sleep()_, _wakeup()_, _argint()_,_acquire()_, _release()_. 

