# Informe Laboratorio 2 - HFTP

##### Integrantes del grupo: 

- Brunello, Florencia: florenciabrunello@mi.unc.edu.ar
- Caldara, Marí­a Emilia: maemiliacaldara@mi.unc.edu.ar
- Ferrero, Andrés: andres.ferrero@mi.unc.edu.ar

## Índice 
1. [Preguntas](#preguntas)
2. [Estructura del Servidor](#estructura)
3. [Decisiones de Diseño](#decisiones)
4. [Conclusiones](#conclusiones)

### Preguntas<a name="preguntas"></a>
1. ¿Qué estrategias existen para poder implementar este mismo servidor pero con capacidad de atender múltiples clientes simultáneamente? Investigue y responda brevemente qué cambios serían necesario en el diseño del código. Los servidores que atienden múltiples clientes son llamados servidores concurrentes. Una de las estrategias para implementarlo se basa en usar threads. Cuando recibe la conexión de un cliente, se crea un nuevo proceso que se encarga de atender las peticiones del cliente.
Asimismo, existe la programación multiprocessing que consiste en que cada cliente se ejecuta en su propio proceso. Así, el servidor maneja múltiples clientes en simultáneo utilizando diferentes núcleos de procesador. Finalmente, la función "select" en Python es una estrategia que permite al servidor manejar múltiples clientes en simultáneo sin hacer uso de hilos ni múltiples procesos. Esta función sirve para monitoriar sockets en busca de actividad.

2. Pruebe ejecutar el servidor en una máquina del laboratorio, mientras utiliza el cliente desde otra, hacia la ip de la máquina servidor. ¿Qué diferencia hay si se corre el servidor desde la IP “localhost”, “127.0.0.1” o la ip “0.0.0.0”?
La diferencia que hay entre que el server corra como localhost es que en este caso, unicamente procesos cliente que se encuentren en la misma máquina pueden conectarse al server. 127.0.0.0 es una dirección de loopback, esto quiere decir que es una dirección especial que los hosts utilizan para dirigir el tráfico hacia ellos mismos. Crea un método de acceso directo para las aplicaciones y servicios TCP/IP que se ejecutan en el mismo dispositivo para comunicarse entre sí. 
En cambio, 0.0.0.0 se trata de lo que sería una dirección no enrutable, lo que quiere decir que no se encuentra ligada a ninguna dirección remota en particular, representa una IP desconocida o una dirección IP inválida.
En el contexto de los servidores, 0.0.0.0 significa todas las direcciones IPv4 en la máquina local . Si un host tiene dos direcciones IP, 192.168.1.1 y 10.1.2.1, y un servidor que se ejecuta en el host escucha en 0.0.0.0, será accesible en ambas direcciones IP. En el contexto del enrutamiento, 0.0.0.0 generalmente significa la ruta predeterminada, es decir, la ruta que conduce al "resto de" Internet en lugar de a algún lugar de la red local.
En los dispositivos cliente como PC’s muestran la dirección 0.0.0.0 cuando no están conectados a ninguna red TCP/IP. Un dispositivo puede obtener esta dirección por defecto si no está en línea. 

### Estructura del Servidor <a name="estructura"></a>
La estructura del servidor se basa en la escucha de mensajes de conexión de clientes en el puerto TCP 19500. El protocolo utilizado para la transferencia de archivos entre el cliente y el servidor es HFTP (Home-made File Transfer Protocol).
Cuando un cliente envía un comando al servidor a través de la conexión TCP, el servidor procesa el comando y verifica si es válido. Si el comando es válido, el servidor realiza la acción solicitada, como la transferencia de un archivo, la eliminación de un archivo o la creación de un directorio. Si el comando no es válido, el servidor envía una respuesta de error al cliente.
El servidor recibe pedidos de forma consecutiva hasta que el cliente decida cerrar la conexión o se produzca un error en la comunicación. En tal caso, el servidor finaliza la conexión y podrá recibir nuevas solicitudes de conexión de clientes.

### Decisiones de Diseño <a name="decisiones"></a>
Para evitar ataques DoS, en read_line elegimos chequear que la cantidad en bytes del comando no supere los 4096 bytes. Sin embargo, estará comentado en la entrega, ya que en caso de no estar comentado, no pasa el test de big_filename, ya que este tiene un tamaño > 5*2^20.

### Conclusiones<a name="conclusiones"></a>
En este laboratorio pudimos comprender en mayor profundidad cómo funciona la arquitectura cliente-servidor. Si bien estuvimos desde el lado del servidor, pudimos entender aún más al cliente, que si bien lo vimos en el laboratorio 1, no requería tanto entendimiento de ambas partes como este. 
A través de este HFTP, pudimos ver cómo las máquinas se conectan entre sí, cómo las peticiones a un servidor se transforman, procesan, y responden.
