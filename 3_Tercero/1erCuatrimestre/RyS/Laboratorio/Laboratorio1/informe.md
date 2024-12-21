# Informe Laboratorio 1 - Aplicación Cliente

##### Alumna:

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar

## Índice
1. [Consigna](#consigna)
2. [Investigación](#invest)
3. [Bibliografía](#biblio)
4. [Conclusiones](#conclusiones)

### Consigna<a name="consigna"></a>

Investigar qué mecanismos permiten funcionar a nombres de dominio como:
● http://中文.tw/
● https://💩.la
Ayuda: investigue sobre el término “encoding”.

### Investigación<a name="invest"></a>
La codificación implica el uso de un código para cambiar los datos originales
a una forma que pueda ser utilizada por un proceso externo.
El tipo de código utilizado para convertir caracteres se conoce como Código
estándar estadounidense para el intercambio de información (ASCII) (esquema de
codificación más utilizado para archivos que contienen texto). El acceso a
Internet depende de la codificación. Un Localizador Uniforme de Recursos (URL),
la dirección de una página web, solo se puede enviar a través de Internet
utilizando ASCII.
ASCII contiene caracteres imprimibles y no imprimibles que representan letras
mayúsculas y minúsculas, símbolos, signos de puntuación y números. Se asigna un
número único a algunos caracteres.
En un archivo ASCII, un número binario de 7 bits representa cada carácter, que
puede ser letras mayúsculas o minúsculas, números, signos de puntuación y otros
símbolos comunes. Sin embargo, las direcciones URL no pueden contener espacios
y, a menudo, tienen caracteres que no están en el juego de caracteres ASCII.
La codificación de URL, también llamada codificación porcentual, soluciona este
problema mediante la conversión de espacios (a un signo + o con %20) y
caracteres que no son ASCII a un formato ASCII válido.
El esquema ASCII estándar tiene solo de cero a 127 posiciones de caracteres;
128 a 255 no están definidos. El problema de los caracteres indefinidos se
resuelve con la codificación Unicode, que asigna un número a cada carácter
utilizado en todo el mundo.

### Bibliografía<a name="biblio"></a>
https://www.techtarget.com/searchnetworking/definition/encoding-and-decoding
https://www.techopedia.com/definition/948/encoding
