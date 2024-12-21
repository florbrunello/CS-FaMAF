# Informe Laboratorio 4 - Big Brother FS 

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Bustos, Franco: franco.bustos@mi.unc.edu.ar
- Caldara, Marí­a Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Compilación](#compilación)
2. [Preguntas](#preguntas)
3. [Aclaraciones](#aclaraciones)
4. [Conclusiones](#conclusiones)

### Compilación<a name="compilación"></a>
Previo a la compilación es necesario instalar libfuse-dev glib y check: 
_sudo apt-get install libfuse-dev_.
Luego, correr los siguientes comandos: 
_cd fat-fuse_
_make_
_mkdir mnt_
_./fat-fuse path/to/fsfat.img ./mnt_
Para desmontar el sistema, correr:
_fusermount -u ./mnt_

### Preguntas<a name="preguntas"></a>


1. Cuando se ejecuta el main con la opción -d, ¿qué se está mostrando en la pantalla?


Nos muestra información de debugging en tiempo real, como llamadas a funciones y a syscalls que utilizan los programas de usuario; información de los procesos(pid) y de las operaciones. Nos sirve para observar cómo se va corriendo fuse.

2. ¿Hay alguna manera de saber el nombre del archivo guardado en el cluster 157?
Hay maneras de leer un contenido de un cluster, pero no exactamente el nombre del archivo. Un cluster puede estar vacío, puede tener entradas a directorio y puede tener datos. En este caso, se probó rastrear el número del cluster y con un búfer leer los datos que había. Pudimos ver que para la imagen _bb fs img_, lo que imprime el búfer con los datos es parte del texto correspondiente al archivo 1984.txt. 
De esta manera podemos concluir que no hay una manera de leer el nombre del archivo del cluster 157 pues puede contener datos, entradas a directorio o estar vacío. Si en este caso, el cluster 157 fuese el primer cluster de un archivo, posiblemente podríamos leer el nombre del archivo.  


Si, pero es bastante lenta descubrirlo. Lo primero sería ver en la Tabla FAT a que apunta dicho cluster, de esta forma podemos saber si está vacío o no, en caso de estarlo sabemos que no hay ningún archivo vinculado a dicho cluster. En caso de haberlo nos fijaremos en las entradas del directorio raiz, fijandonos en el cluster inicial de cada archivo y viendo en la tabla FAT si esos llevan eventualmente al cluster 157. En caso de no encontrarlo, nos fijaremos en las entradas que apuntan a directorios y de ahí comprobamos que el cluster no sea el 157, pues si alguno lo es quiere decir que el cluster 157 es de un directorio y a través del padre (la raíz en este caso) podemos saber su nombre, luego vemos el contenido de cada directorio y repetimos como lo hicimos con la raíz. Así eventualmente sabremos el nombre del archivo guardado en el cluster 157. Una forma manual y mas simple de hacerlo también puede ser ejecutando _cat "file"_, ya que en la terminal donde se está montando la imagén mostrará los cluster que se están leyendo para cat, así comprobaremos si un archivo utiliza dicho cluster. En nuestro caso podemos ver que este cluster es utilizado por el archivo 1984.TXT.

3. ¿Dónde se guardan las entradas de directorio? ¿Cuántos archivos puede tener adentro un directorio en FAT32?


La FAT tiene forma de tabla organizada en entradas sucesivas de 32 bits. Una entrada para cada cluster del soporte. Estas entradas permiten conocer el estado de cada uno de estos clusters, es decir saber si son defectuosos o no, si contienen o no información y si así es, si se corresponden con el último cluster del fichero o si en cambio el fichero continúa en algún otro cluster. De los 32 bits de cada entrada solo los 28 primeros (los más bajos) se utilizan para almacenar la dirección de clusters, los cuatro superiores están reservados. 
Las entradas de 32 bits se organizan secuencialmente, una detrás de otra, a lo largo los sectores de la FAT.
En los clusters de la Data Region encontraremos 3 tipos de información:

- FAT 32 Byte Directory Entry Structure: grupos de 32 bytes que contienen la información básica del volumen, de fichero o directorio. La información básica se corresponde a fechas y horas de creación o modificación, cluster donde se encuentra la información etc.

- FAT Long Directory Entry Structure: son las entradas de nombre largo, añadidas en FAT32 para permitir el almacenamiento de nombres de directorio o de fichero mayores de 11 bytes.

- Bytes con el contenido de fichero

El tamaño máximo de un archivo en FAT32 es 4 GiB (232−1 bytes) es por ello que en FAT32, desaparece el área del directorio raíz y, con ella, la limitación fija de número de ficheros que puede contener.

Esto va por el lado de las tablas FAT, el contenido de los clusters de directorios son entradas que contienen información como el nombre de los archivos, su cluster inicial y el tamaño que ocupan dichos archivos o son directorios y muestran el cluster que los vincula. Toda entrada de archivo/directorio que está contenido en el cluster de un directorio se lo considera como el directorio padre de dichos archivos/directorios. Como consideramos que un directorio solo puede contener un solo cluster, la capacidad que tiene este directorio para contener entradas es de a lo sumo el tamaño del cluster (en bytes, acá se considera 512 bytes) dividido el tamaño de las entradas (32) (Cada directorio podría tener un máximo de 16 archivos, sin capacidad para guardar otro directorio).


4. Cuando se ejecuta el comando como ls -l, el sistema operativo, ¿llama a algún programa de usuario? ¿A alguna llamada al sistema? ¿Cómo se conecta esto con FUSE? ¿Qué funciones de su código se ejecutan finalmente? 

Para responder esta pregunta, utilizamos la flag -d al montar la imagen, así podemos ver qué llamadas realiza ls -l.
Este es un ejemplo de lo que imprime la herramienta -d si hacemos ls -l en /mnt, donde sólo tenemos el archivo 1984.txt:

Podemos ver que utiliza programas de usuario dadas por FUSE, implementados en fat_fuse_ops.c: opendir(), que abre el directorio; getattr(), que nos da los atributos de la ruta del archivo; readdir(), que agrega una entrada al directorio; releasedir(), que cierra el directorio. Algunas syscalls que utiliza el sistema operativo (usamos strace para ver esto en detalle) son: brk(), mmap(), open(), close(), read(), getdent(), entre otras. 
Esto se conecta con FUSE ya que la mayoría de estas syscalls se ven modificadas por FUSE, siendo nosotros quienes las podemos ver y modificar, como son el caso de write por ejemplo.

5. ¿Por qué tienen que escribir las entradas de directorio manualmente pero no tienen que guardar la tabla FAT cada vez que la modifican?


La tabla FAT se encarga solamente de enlazar los clusters de los archivos, en cambio las entradas de directorio contienen mas información como son el tamaño de dichos archivos, cual es su primer cluster, su nombre entre otras cosas. 

6. Para los sistemas de archivos FAT32, la tabla FAT, ¿siempre tiene el mismo tamaño? En caso de que sí, ¿qué tamaño tiene?


FAT32 utiliza direcciones de cluster de 32 bits (aunque solo 28 de esos bits se utilizaban realmente). En teoría, esto debería permitir aproximadamente 2^32 clusters, arrojando tamaños de almacenamiento cercanos a los 8 TiB. Sin embargo, debido a limitaciones en la utilidad ScanDisk de Microsoft, el número de clusters direccionables en el sistema de archivos FAT32 es de 268.435.456. 
Los tamaños de cluster predeteminados para FAT32 son los siguientes: 512 bytes, 1 KB, 2 KB, 4 KB, 8 KB, 16 KB o 32 KB.
Luego, suponiendo que cada cluster es de 32 KiB (tamaño máximo de cluster), tenemos que el tamaño de la tabla FAT para sistemas de archivos FAT32 es de 4.177.920 clusters * 32 KiB = 8192 GiB. 


### Aclaraciones<a name="aclaraciones"></a>
En lo que corresponde a la parte II, hay unos comportamientos que se desconoce cómo deberían funcionar.Al montar la imagen se debe hacer un _ls_ para crear el archivo de logs y evitar errores. 
Por otro lado, al registrar las llamadas a write y read, se escribe basura en la primer línea del archivo _fs.log_, pero no interfiere en el registro del resto.
Antes de hacer el último commit, se usó el comando _git-clang-format *.c *.h_ para asegurarse de convertir todo el código a formato clang.

En los test, en mas reciente (test_fs.sh), el último test que hace dentro de conjunto falla, no pudimos resolverlo.

### Conclusiones<a name="conclusiones"></a>

En este trabajo de laboratorio profundizamos el funcionamiento del sistema de archivos que presenta el sistema operativo, en este caso, de tipo FAT. Esto nos facilitó la implementación en userspace.