# Informe Laboratorio 2 - Programación Orientada a Objetos 

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Caldara, Marí­a Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Compilación](#compilacion)
2. [Decisiones de Implementación](#decisiones)
3. [Organización y Jerarquía de Clases](#organizacion)
4. [Conclusión](#conclusion)


### Compilación<a name="compilacion"></a>
Para compilar el archivo programa recomendamos utilizar una herramienta de auto-building como Maven o, la que usamos nosotros, herramientas externas de compilación de Visual Studio Code. 
La línea de comando para compilar y ejecutar el proyecto debería tener el siguiente formato: 
/usr/bin/env /usr/lib/jvm/java-11-openjdk-amd64/bin/java @/tmp/cp_8s80jkprnvgu68b22hepk7fg4.argfile FeedReaderMain  -ne 


### Decisiones de Implementación<a name="decisiones"></a>
Las entidades que considera como tal QuickHeuristic pero que no están listadas en nuestro diccionario, es decir, que no se listan en cathegoryMap o themeMap, son ignoradas.


### Organización y Jerarquía de clases<a name="organizacion"></a>
Este proyecto está organizado en cinco carpetas dentro de la carpeta principal src:
- feed: esta carpeta contiene los paquetes Article y Feed, donde feed  modela la lista de articulos de un determinado feed y article modela el contenido de un articulo (es decir, un item en el caso del rss feed).
- httpRequest: se encarga de realizar el pedido de feed al servidor de noticias. Dentro de la misma, se define el package httpRequest.
- namedEntity: por un lado tenemos las clases RandomHeuristic y QuickHeuristic que heredan de la clase abstracta Heuristic. Estas reconocen entidades nombradas (substrings que se encuentran dentro del string de texto). Por otro lado están las carpetas category y themes que organizan las entidades nombradas en una jerarquía de clases. Finalmente, se encuentran los "cruces" de estas categorías y temas tales como PersonFutbol o PersonPolitics. 
- parser: en el package parser está definida la clase subscription parser que implementa el parser del archivo de suscripcion y rss parser que implementa el parser de feed de tipo rss. 
- subscription: consta del package subscription donde se define la clase subscription que abstrae el contenido del archivo de suscripcion y single subscription que abstrae el contenido de una sola suscripcion que ocurre en lista de suscripciones.
Finalmente, FeedReaderMain lee feeds RSS de un archivo de subscripción y los procesa. Si se ejecuta sin argumentos, lee el archivo de suscripción por defecto, solicita cada feed a través de una solicitud HTTP y luego llama a un parser RssParser para extraer los datos necesarios. Finalmente, imprime los artículos del feed de manera legible para el usuario. Si se ejecuta con el argumento "-ne", también calcula las entidades nombradas en cada artículo utilizando una heurística rápida y las muestra en una tabla de entidades nombradas legible para el usuario.


### Conclusión<a name="conclusion"></a>
En este proyecto de laboratorio se implementó un lector automático de feeds utilizando Java bajo el paradigma orientado a objetos. 
El usuario puede establecer los sitios y tópicos de los cuales obtener los feeds a través de un archivo en formato .json y se mostrarán de forma legible y amigable. Además, se agregó una funcionalidad para computar heurísticamente las entidades nombradas mencionadas en la lista de feeds. En resumen, se logró desarrollar una herramienta útil y eficiente para la lectura y análisis de feeds en java pudiendo así ver la complejidad del procesamiento del lenguaje natural. 
Además, a pesar de que ninguno de los integrantes del grupo estaba familiarizado con la programación orientada a objetos, pudimos distinguir características que lo diferencian del resto de los paradigmas. 
