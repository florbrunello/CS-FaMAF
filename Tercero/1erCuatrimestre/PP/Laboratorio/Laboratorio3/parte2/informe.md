# Informe Laboratorio 3 - Programación Orientada a Objetos 

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Caldara, Marí­a Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Resumen](#resumen)
2. [Introducción](#introduccion)
3. [Compilación](#compilacion)
4. [Elección del código](#eleccion)
5. [Desarrollo](#desarrollo)
6. [Decisiones de Implementación](#decisiones)
7. [Conclusión](#conclusion)

### Resumen<a name="resumen"></a>
Implementación de la recuperación de documentos por palabras clave en un lector automático de feeds utilizando una arquitectura distribuida. 

### Introducción<a name="introduccion"></a>
En este proyecto, a partir de la re-implementación del lector automático de feeds del laboratorio 2 utilizando una arquitectura distribuida, hicimos las modificaciones necesarias para lograr la recuperación de documentos por palabras clave. Para lograr esto, comparamos y seleccionamos unos de los códigos desarrollados individualmente.

### Compilación<a name="compilacion"></a>
Para compilar el proyecto, se deben seguir los siguientes pasos: 
1) Descargar visual studio code
2) Instalar la versión OpenJDK 11.0.19 de Java. 
3) Importar dentro del directorio las librerías necesarias, para ello ir a la sección de "Referenced Libraries" dentro del Java Project. Una vez allí, añadir los jars propios de Spark y el jar de la librería para json (obtenida desde el link https://mvnrepository.com/artifact/org.json/json/20230227).
4) Ejecutar el programa usando la funcionalidad para ejecutar que provee el entorno. 
5) Para reuperar documentos por palabras clave, usar los mismos argumentos que usa Visual y además agregarle argumento -search.  

En nuestro caso, la terminal puede verse algo así: 

    Para obtener los feeds:
    -  /usr/bin/env /usr/lib/jvm/java-11-openjdk-amd64/bin/java @/tmp/cp_9n2zqrak4anzw0zd8a1ei6py0.argfile FeedReaderMain
    Para obtener las entidades nombradas: 
    -  /usr/bin/env /usr/lib/jvm/java-11-openjdk-amd64/bin/java @/tmp/cp_9n2zqrak4anzw0zd8a1ei6py0.argfile FeedReaderMain -ne
    Para obtener un documento por palabra clave:
    -  /usr/bin/env /usr/lib/jvm/java-11-openjdk-amd64/bin/java @/tmp/cp_9n2zqrak4anzw0zd8a1ei6py0.argfile FeedReaderMain -search

Esto puede variar dependiendo de la configuración de cada computadora.

### Elección del código<a name="eleccion"></a>
A la hora de comparar los distintos enfoques utilizados en la etapa individual, podemos identificar ventajas y desventajas en cada estrategia, así como en las implementaciones en sí.
En cuanto a la comparación de los métodos de investigación notamos que la investigación basada en código de ejemplo, si bien es "rápida" en el sentido de poder obtener un código en concreto, puede resultar limitada o acotada ya que cuando se necesita implementar una tarea ligeramente más específica difícilmente haya un código que haga excatamente lo que se pide. Es por ello que esta estrategia podría utilizarse en una etapa inicial para familiarizarse con la estructura general que debe tener el código. 
Por otro lado, internet ofrece la ventaja de ser muy completo ya que podemos encontrar mucha documentación. La dificultad que presenta es saber buscar una fuente confiable porque al haber una sobrecarga de información yace en la capacidad del que investiga de seleccionar la respuesta más óptima. 
Finalmente, la estrategia que mejor nos resultó fue la de inteligencia articicial, en particular Chat GPT. Si bien no otuvimos el código directo de la misma, el hecho de poder consultar cosas específicas y obtener respuestas orientativas nos ahorró mucho tiempo a la hora de desarrollar un proyecto como este. 
En cuanto a la compración de las implementaciones en sí podemos notar como ventajas en común de los tres códigos, estas son: utilizar la interfaz de programación JavaRDD de Apache Spark para realizar operaciones distribuidas, utilizar la clase SparkSession para crear y configurar una sesión de Spark así como también funciones map-reduce para operar y transformar los datos de manera concisa y la clase JavaPairRDD para trabajar con pares clave-valor en Spark.
En particular, el código de Andrés tiene la ventaja de aprovechar el cálculo distribuído para todas las tareas, además de ser el más consiso, y la desventaja que encontramos es que no indica el número máximo de núcleos (cores) configurados para el uso de Spark. El código de Florencia tiene como ventaja la forma compacta en la que se filtran las entidades nombradas mediante el uso de "filter" y guardas. La desventaja es el uso de un bucle para crear la lista de entidades y luego reducirlas con map-reduce en lugar de hacerlo todo junto. Finalmente, el código de María tiene como ventaja que utiliza el cálculo distribuído para las tareas pero como desventaja que no filtra las entidades nombradas que están en el diccionario.
En conlusión, a la hora de elegir un método de investigación para llevar a cabo la segunda parte del laboratorio podemos ver que cada estrategia ofrece distintas ventajas y desventajas. Consideramos que la mejor fue el uso de una inteligencia artificial. Es por ello que para incorporar la funcionalidad de recuperar documentos por palabras clave, hicimos uso de Chat GPT tomando como código de base el implementado por Andrés.


### Desarrollo<a name="desarrollo"></a>
Este trabajo fue desarrollado en conjunto con el objetivo de obtener un lector automático de feeds que permita la recuperación de documentos por palabras clave. Para esto, se compararon las soluciones individuales de cada integrante del grupo y se seleccionó una de ellas para implementarla en el proyecto.
Para el desarrollo, nos basamos en el código elegido y a partir de ahí realizamos las modificaciones pertinentes para la funcionalidad requerida. Utilizamos como herramienta y ayuda para el desarrollo de este trabajo GitHub Copilot y en menor medida chatGPT. 
La funcionalidad se incorpora en el main, donde si el usuario desea obtener el documento, se debe ejecutar el programa con -search. Esto permite imprimir la entidades nombradas de distintos feeds, y luego de eso, se le pide que ingrese una palabra clave. Si la palabra clave se encuentra en el diccionario, se imprime el documento que la contiene, es decir, el artículo que contiene esa palabra.

### Decisiones de Implementación<a name="decisiones"></a>
Se tomaron algunas decisiones con respecto a la implementación del código. Las mismas fueron que imprima únicamente las entidades nombradas que reconocía la heurística pero además las que estaban declaradas en nuestro diccionario y si el usuario quiere buscar un documento por palabra clave, entonces debe ejecutar el programa con la opción -search. 

### Conclusión<a name="conclusion"></a>
En este laboratorio aprendimos sobre la eficacia de la utilización de la arquitectura distribuida basada en Spark y las ventajas que ofrecen cada una de las estrategias de investigación utilizadas en la etapa individual. Mediante la comparación de diversas fuentes como código de ejemplo, información en línea y chat GPT, implementamos una herramienta más versátil para el procesamiento de información en grandes colecciones de documentos. Finalmente, desarrollamos una funcionalidad adicional para recuperar documentos por palabras clave.


 
