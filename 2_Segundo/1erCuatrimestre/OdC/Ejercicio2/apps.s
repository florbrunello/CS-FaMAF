/*Ejercicio 2 Odc2022 Brunello Florencia, Caldara María Emilia y Ferrero Andrés */

.equ SCREEN_WIDTH, 		640
.equ SCREEN_HEIGH, 		480
.equ SKY_WIDTH,         480 
.equ SKY_HEIGH,         300
.equ BITS_PER_PIXEL,  	32


.globl main
main:
	// X0 contiene la direccion base del framebuffer
 	mov x20, x0	// Save framebuffer base address to x20	
	//---------------- CODE HERE ------------------------------------

	/*MODULARIZACIÓN */

	mov x14,75	     //Contador de los pixeles que quiero subir el termo
	mov x5,0
loop80:
	bl pintar_fondo
	bl pintar_termo
	bl pintar_tapa
	bl delay 
	add x5,x5,1
	sub x14, x14, 1  
	cbnz x14,loop80
	
	bl delay2 
	bl delay2
	bl pintar_fondo
	bl frame1

	mov x14,123     //Contador de los pixeles que quiero bajar el agua	
loop79:
	bl pintar_agua
	bl delay
	add x5, x5, 1
	sub x14, x14, 1  
	cbnz x14,loop79
	
	bl delay2
	bl pintar_fondo
	bl frame1


	bl delay2
	bl delay2
	mov x14,75	     //Contador de los pixeles que quiero bajar el termo
	mov x5,0
loop78:
	bl pintar_fondo
	bl pintar_termo2
	bl pintar_tapa2
	bl delay 
	add x5,x5,1
	sub x14, x14, 1  
	cbnz x14,loop78


	
	b end


pintar_fondo: 
    /*
     Descripción: 
        Vamos a usar esta etiqueta para modularizar el repinte del fondo del dibujo al mover el termo.
        Algunos datos a saber:
			-usamos x8 para ir guardando el color que queremos pintar en ese momento,
            para su respectiva figura.
            -usamos x1 siempre como contador de la coordenada X. Es decir, me define
            el ancho de lo que quiero pintar en horizontal.
            -usamos x2 siempre como contador de la coordenada Y. Es decir, me define
            el alto de lo que quiero pintar en vertical.
            -Cuando pintamos un círculo, a x4 lo usamos para guardar el resultado
            de la aplicación de la fórmula del círculo.
            -las instrucciones "br lr" que se encuentren son para poder modularizar. 
    */
	
    movz x8, 0xDE, lsl 16      //Guardo en el registro 8 el color beige(para la pared) 
	movk x8, 0xB887, lsl 00
	
	
    mov x11,640     /*x11 = registro que vamos a utilizar para guardar 640, constante que utiliza la 
                            fórmula para calcular la dirección de un pixel*/
    
/*----PINTO FONDO(PARED BEIGE)----*/
	mov x2, SCREEN_HEIGH         // Y Counter 

loop1:
	mov x1, SCREEN_WIDTH         // X Counter
loop0:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop0	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
	cbnz x2,loop1	   // if not last row, jump
	//-------------FIN PARED


	
/*----PINTO CIELO---*/ 
	movz x8, 0x9A,lsl 16        //Color celeste.
	movk x8, 0xE3F2, lsl 00

	mov x3,0            // valor en Y donde empieza
	mov x2, SKY_HEIGH       // Y Size/Counter
ventana:   
	/*Calculo la coordenada X del pixel que quiero actualizar con la 
      fórmula Dirección = Dirección de inicio + 4 * [x + (y * 640)] */
    mul x0,x3,x11
	add x0,x0,160       //160 es el píxel en X donde empieza el marco
	lsl x0,x0,2 
	add x0,x0,x20       //fin cálculo fórmula
	mov x1, SKY_WIDTH      // Contador X, se resetea cada vez que salto a ventana:
loop2:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop2	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,ventana	   // if not last row, jump
	//-------------fin pintar cielo------------


/*----PINTO MARCO VENTANA----*/ 

//Pinto barra vertical izquierda
	mov x3,0            // valor en Y donde empieza
	mov x2, SKY_HEIGH       // Y Size/Counter
	
	//Defino color gris 
	movz x8,0x55,lsl 16
	movk x8, 0x5555,lsl 00 

marco_v:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,160
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,25      // Ancho del marco //
loop3:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop3	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,marco_v
    //---------

//pinto barra del medio
	mov x3,0            // valor en Y donde empieza
	mov x2, SKY_HEIGH       // Y Size/Counter
marco_v2:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,450
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,15      // Ancho del marco 
loop4:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop4	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,marco_v2
	
//pinto barra horizontal inferior del marco 
	mov x3,275      //valor en Y donde empieza
	mov x2,25       // Y Counter

marco_h:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,160
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1, SKY_WIDTH     // Ancho del marco 
loop5:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop5	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,marco_h
//-------------fin pintar marco ventana------------



/*----PINTO MESA----*/ 
//pinto parte superior de la mesa 
	mov x2,15       // Y counter
	mov x3,390      // valor en Y donde empieza

	movz x8,0xFC,lsl 16     //Color para la mesa
	movk x8,0xFCFC ,lsl 00

mesa: 
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,30
	lsl x0,x0,2 	
	add x0,x0,x20
	mov x1,610   // Ancho del marco 
loop6:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop6	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,mesa

//pinto parte de abajo de la mesa
	mov x2,32     
	mov x3,405

	movz x8,0xE8,lsl 16 //Color para parte de abajo
	movk x8,0xE8E8,lsl 00
mesa_sombra: 
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,90
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,550   // Ancho del marco 
loop7:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop7	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,mesa_sombra


//Pata de la Mesa 
	mov x2,75      
	mov x3,405
pata_mesa:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,90
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,28      // Ancho del marco 
loop8:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop8	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,pata_mesa
//-------------fin pintar mesa------------



/*----PINTO MATE
    La forma en la que pintamos el mate es: -Pintamos las patas del mate.
                                            -Pintamos un circulo completo.
                                            -Pintamos un rectángulo del color del fondo que "tape" 
                                            la parte superior del círculo, quedando así formado el mate.
                                            -Por último, pintamos la bombilla.  
    Algo más a agregar: La estrategia que usamos para pintar un círculo es: definir un cuadrado como
    referencia(dentro de este va a ser pintado el círculo). Luego, vamos recorriendo cada píxel dentro
    del cuadrado, y nos fijamos mediante la fórmula (x-a)²+(y-b)² <= r² (donde (a,b)=centro; (x,y)=coordenada
    a chequear si pertenece al círculo; y r=radio), si el pixel donde estoy parado pertence al círculo o no.
    En caso de pertenecer, lo pinto. Si no se cumple, paso al siguiente pixel.                            ----*/ 

//pinto pata izquierda mate
	movz x8,0x80,lsl 16     //Color para patas mate
	movk x8,0x8080 ,lsl 00

	mov x2,10      
	mov x3,380
pata1_mate:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar 
	add x0,x0,270
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,7      // Ancho del marco 
loop11:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop11	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,pata1_mate
	
	
//pinto pata derecha mate
	mov x2,10       
	mov x3,380
pata2_mate:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,305
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,7      // Ancho del marco 
loop12:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop12   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,pata2_mate
	

//pinto CIRCULO MATE
	//Coordenadas del centro: 
	mov x7,290  // x7=a 
	mov x6,345  //x6=b 

	mov x2,80       //Alto del circulo 
	mov x15,250     //es la coordenada x del cuadrado 
	mov x3,305      //coordenada y del cuadrado
	
	movz x8,0x96,lsl 16  //Color que quiero pintar el mate
	movk x8,0x4B00, lsl 00

mate:
	mov x15,250
	add x3,x3,1
	mov x1,80 // Ancho del circulo 

loop9:
	sub x4,x15,x7           //(x-a)
	madd x4, x4, x4, xzr    // (x-a)²
	sub x9,x3, x6           //(y-b)
	madd x9, x9, x9, xzr    //(y-b)²
	add x4, x4, x9          //(x-a)²+(y-b)²
	cmp x4,1600             //1600 =r² 
	b.gt loop10             //Si (x-a)²+(y-b)² > 2500, no pinto y paso al siguiente pixel 
	mul x0,x3,x11	        //y*640. Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,x15           //x+(y*640) 
	lsl x0,x0,2             //4*(x+(y*640)) 
	add x0,x0,x20
	stur w8,[x0]	        // Set color of pixel 
loop10:
	add x15,x15,1  	 	//Sumo en la coord x, x+1  
	sub x1,x1,1	        // decrement X counter
	cbnz x1,loop9	    // If not end row jump
	sub x2,x2,1	         // Decrement Y counter
	cbnz x2,mate         // if not last row, jump


//pinto rectangulo para definir boca del mate
	movz x8,0xDE,lsl 16 //Color para rectangulo mate(ídem pared de fondo)
	movk x8,0xB887 ,lsl 00

	mov x2, 23    
	mov x3,300
cobertura_mate:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar 
	add x0,x0,250
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,80      // Ancho del marco 
loop13:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop13	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,cobertura_mate  // if not last row, jump


//pinto bombilla
	movz x8,0x80,lsl 16     //Color para bombilla
	movk x8,0x8080 ,lsl 00


    mov x15,220   //posición en x donde arranca
    mov x3,280  //posición en y donde arranca 
    mov x2,43   //contador y

loop22: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x15 
    lsl x0,x0,2 
    add x0,x0,x20
	mov x1,5   //contador x
loop23:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x1,x1,1
	cbnz x1,loop23      // if not end row, jump
    add x3,x3,1       //va a la fila siguiente 
    add x15,x15,1       //corre un pixel en las x para la derecha
    sub x2,x2,1       //suma uno al contador cada vez pinto uno 
    cbnz x2,loop22      // if not last row, jump
	
//-------------fin pintar mate------------



/*----PINTO ESCARAPELA----*/ 
//pinto escarapela base(circulo celeste de afuera)
	movz x8, 0x49,lsl 16    //defino color celeste
	movk x8, 0xA4FF, lsl 00
	
	//Coordenadas del centro 
	mov x7,80// x7=a 
	mov x6,100 //x6=b 

	mov x2,100    //Alto del circulo 
	mov x15,30 //es la coordenada x del cuadrado 
	mov x3,50 //coordenada y del cuadrado
	

escarapela:
	mov x15,30
	add x3,x3,1
	mov x1,100 // Ancho del circulo 

loop15:
	sub x4,x15,x7 // (x-a)
	madd x4, x4, x4,xzr// (x-a)²
	sub x9,x3, x6 //(y-b)
	madd x9, x9, x9,xzr//(y-b)²
	add x4, x4, x9 //(x-a)²+(y-b)²
	cmp x4,2500 //2500 =r² 
	b.gt loop14   //Si (x-a)²+(y-b)² > 2500, no pinto y paso al siguiente pixel 
	mul x0,x3,x11	//  y*640. Calculo la coordenada X del pixel que quiero actualizar 
	add x0,x0,x15  //x+(y*640) 
	lsl x0,x0,2    //4*(x+(y*640)) 
	add x0,x0,x20
	stur w8,[x0]	   // Set color of pixel 
loop14:
	add x15,x15,1  	 	//Sumo en la coord x, x+1  
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop15	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
	cbnz x2,escarapela      // if not last row, jump



//pinto escarapela parte blanca(circulo blanco del medio)
	movz x8, 0xFF,lsl 16    //defino color blanco
	movk x8, 0xFFFF, lsl 00
	
	
	//Coordenadas del centro 
	mov x7,80// x7=a 
	mov x6,100 //x6=b 

	mov x2,60    //Alto del circulo 
	mov x3,70 //coordenada y del cuadrado
	mov x15,50 //es la coordenada x del cuadrado 
	

escarapela_b:
	mov x15,50
	add x3,x3,1
	mov x1,60 // Ancho del circulo 

loop16:
	sub x4,x15,x7 // (x-a)
	madd x4, x4, x4,xzr// (x-a)²
	sub x9,x3, x6 //(y-b)
	madd x9, x9, x9,xzr//(y-b)²
	add x4, x4, x9 //(x-a)²+(y-b)²
	cmp x4,900 //900 =r² 
	b.gt loop17   //Si (x-a)²+(y-b)² > 900, no pinto y paso al siguiente pixel 
	mul x0,x3,x11	//  y*640. Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,x15  //x+(y*640) 
	lsl x0,x0,2    //4*(x+(y*640)) 
	add x0,x0,x20
	stur w8,[x0]	   // Set color of pixel 
loop17:
	add x15,x15,1  	 	//Sumo en la coord x, x+1  
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop16	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
	cbnz x2,escarapela_b


//pinto centro escarapela
	movz x8, 0x49,lsl 16 //defino color celeste
	movk x8, 0xA4FF, lsl 00
	
	//Coordenadas del centro 
	mov x7,80// x7=a 
	mov x6,100 //x6=b 

	mov x2,20    //Alto del circulo 
	mov x15,70 //es la coordenada x del cuadrado 
	mov x3,90 //coordenada y del cuadrado
	

escarapela_c:
	mov x15,70
	add x3,x3,1
	mov x1,20 // Ancho del circulo 

loop18:
	sub x4,x15,x7 // (x-a)
	madd x4, x4, x4,xzr// (x-a)²
	sub x9,x3, x6 //(y-b)
	madd x9, x9, x9,xzr//(y-b)²
	add x4, x4, x9 //(x-a)²+(y-b)²
	cmp x4,100 //100 =r² 
	b.gt loop19   //Si (x-a)²+(y-b)² > 900, no pinto y paso al siguiente pixel 
	mul x0,x3,x11	//  y*640. Calculo la coordenada X del pixel que quiero actualizar 
	add x0,x0,x15  //x+(y*640) 
	lsl x0,x0,2    //4*(x+(y*640)) 
	add x0,x0,x20
	stur w8,[x0]	   // Set color of pixel 
loop19:
	add x15,x15,1  	 	//Sumo en la coord x, x+1  
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop18	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
	cbnz x2,escarapela_c

//-------------fin pintar mate------------

	
/*----PINTO ÁRBOL----*/ 
	// pinto tronco 
	movz x8,0x33,lsl 16     //Color para tronco
	movk x8,0x1900 ,lsl 00

	mov x2,275  
	mov x3,0
tronco:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,185
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,55     // Ancho del tronco   
loop24:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	  		// Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop24	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,tronco


//pinto relleno copa del árbol(rectángulo para tapar algunos espacios) 
	movz x8, 0x2B,lsl 16    //defino color
	movk x8, 0x5500, lsl 00

	mov x2,40   
	mov x3,0
relleno:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,185
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,100     // Ancho del tronco   
loop31:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	  		// Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop31	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,relleno



//pinto copa del árbol(las copas las pintamos como círculos)
	movz x8, 0x33,lsl 16        //defino color 
	movk x8, 0x6600, lsl 00
	
	
	//Coordenadas del centro 
	mov x7,260// x7=a 
	mov x6,100 //x6=b 

	mov x2,100    //Alto del circulo 
	mov x15,210 //es la coordenada x del cuadrado 
	mov x3,50 //coordenada y del cuadrado
	

copa_arbol:
	mov x15,210
	add x3,x3,1
	mov x1,100 // Ancho del circulo 

loop25:
	sub x4,x15,x7 // (x-a)
	madd x4, x4, x4,xzr// (x-a)²
	sub x9,x3, x6 //(y-b)
	madd x9, x9, x9,xzr//(y-b)²
	add x4, x4, x9 //(x-a)²+(y-b)²
	cmp x4,2500 //2500 =r² 
	b.gt loop26   //Si (x-a)²+(y-b)² > 2500, no pinto y paso al siguiente pixel 
	mul x0,x3,x11	//  y*640. Calculo la coordenada X del pixel que quiero actualizar 
	add x0,x0,x15  //x+(y*640) 
	lsl x0,x0,2    //4*(x+(y*640)) 
	add x0,x0,x20
	stur w8,[x0]	   // Set color of pixel 
loop26:
	add x15,x15,1  	 	//Sumo en la coord x, x+1  
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop25	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
	cbnz x2,copa_arbol



//pinto copa del árbol 2
	movz x8, 0x4E,lsl 16    //defino color
	movk x8, 0x9209, lsl 00
	
	
	//Coordenadas del centro 
	mov x7,285// x7=a 
	mov x6,50 //x6=b 

	mov x2,100    //Alto del circulo 
	mov x15,235 //es la coordenada x del cuadrado 
	mov x3,0 //coordenada y del cuadrado
	

copa_arbol2:
	mov x15,235
	add x3,x3,1
	mov x1,100 // Ancho del circulo 

loop27:
	sub x4,x15,x7 // (x-a)
	madd x4, x4, x4,xzr// (x-a)²
	sub x9,x3, x6 //(y-b)
	madd x9, x9, x9,xzr//(y-b)²
	add x4, x4, x9 //(x-a)²+(y-b)²
	cmp x4,2500 //2500 =r² 
	b.gt loop28   //Si (x-a)²+(y-b)² > 2500, no pinto y paso al siguiente pixel 
	mul x0,x3,x11	//  y*640. Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,x15  //x+(y*640) 
	lsl x0,x0,2    //4*(x+(y*640)) 
	add x0,x0,x20
	stur w8,[x0]	   // Set color of pixel 
loop28:
	add x15,x15,1  	 	//Sumo en la coord x, x+1  
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop27	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
	cbnz x2,copa_arbol2


//pinto copa del árbol 3
	movz x8, 0x2B,lsl 16    //defino color
	movk x8, 0x5500, lsl 00
	
	
	//Coordenadas del centro 
	mov x7,234// x7=a 
	mov x6,50 //x6=b 

	mov x2,100    //Alto del circulo 
	mov x15,184 //es la coordenada x del cuadrado 
	mov x3,0 //coordenada y del cuadrado
	

copa_arbol3:
	mov x15,184
	add x3,x3,1
	mov x1,100 // Ancho del circulo 

loop29:
	sub x4,x15,x7 // (x-a)
	madd x4, x4, x4,xzr// (x-a)²
	sub x9,x3, x6 //(y-b)
	madd x9, x9, x9,xzr//(y-b)²
	add x4, x4, x9 //(x-a)²+(y-b)²
	cmp x4,2500 //2500 =r² 
	b.gt loop30   //Si (x-a)²+(y-b)² > 2500, no pinto y paso al siguiente pixel 
	mul x0,x3,x11	//  y*640. Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,x15  //x+(y*640) 
	lsl x0,x0,2    //4*(x+(y*640)) 
	add x0,x0,x20
	stur w8,[x0]	   // Set color of pixel 
loop30:
	add x15,x15,1  	 	//Sumo en la coord x, x+1  
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop29	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
	cbnz x2,copa_arbol3
	br lr 

//-------------fin pintar mate------------



/*----PINTO TERMO----*/ 
pintar_termo:
	movz x8,0xA0,lsl 16     //Color para termo
	movk x8,0xA0A0 ,lsl 00
	mov x2,190      // Altura del termo 
	mov x3,200
	sub x3,x3,x5      //Va iterando sobre las y, para que suba el dibujo 

base_t:
	mul x0,x3,x11	   //Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,440
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,60         // Ancho del termo  
loop20:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	       // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop20	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,base_t
	br lr 

pintar_tapa:
	// tapa termo
	movz x8,0x00,lsl 16 //Color para tapa
	movk x8,0x0000 ,lsl 00
	
	mov x2,35      // Y Size marco
	mov x3,175
	sub x3,x3,x5      //Va iterando sobre las y, para que suba el dibujo
tapa_t:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar 
	add x0,x0,440
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,60      // Ancho de la tapa 
loop21:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop21	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,tapa_t
	br lr 



//MODIFICAR 

frame1:	//1era inclinación del termo 
	movz x8,0xA0,lsl 16 //Color para termo
	movk x8,0xA0A0 ,lsl 00

   	mov x7,440   //en las x  Desde donde arranca 
    mov x3,330  //comienzo de las y 
    mov x6,150   //altura q quiero q me haga la linea 


loop32: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x7  
    lsl x0,x0,2 
    add x0,x0,x20
	mov x16,80
loop33:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x16,x16,1
	cbnz x16,loop33
    sub x3,x3,1       //me va a la fila siguiente 
    sub x7,x7,1       //me corre un pixel en las x para la der
    sub x6,x6,1       //suma uno al contador cada vez pinto uno 
    cbnz x6,loop32

	/* Emprolijo parte de arriba */

	//Despintar  parte superior termo 
	movz x8, 0x00,lsl 16 //Negro
	movk x8, 0x0000, lsl 00 
   	mov x7,350  //en las x  Desde donde arranca 
    mov x3,150  //comienzo de las y 
    mov x6,70   //altura q quiero q me haga la linea 
    

loop34: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x7  
    lsl x0,x0,2 
    add x0,x0,x20
	mov x16,50
loop35:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x16,x16,1
	cbnz x16,loop35
    add x3,x3,1       //me va a la fila siguiente 
    sub x7,x7,1       //me corre un pixel en las x para la der
    sub x6,x6,1       //suma uno al contador cada vez pinto uno 
    cbnz x6,loop34
	
	//Despintar parte superior tapa termo 
	movz x8, 0x9A,lsl 16        //Color celeste.
	movk x8, 0xE3F2, lsl 00
   	mov x7,320  //en las x  Desde donde arranca 
    mov x3,150  //comienzo de las y 
    mov x6,70   //altura q quiero q me haga la linea 
    

loop40: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x7  
    lsl x0,x0,2 
    add x0,x0,x20
	mov x16,30
loop41:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x16,x16,1
	cbnz x16,loop41
    add x3,x3,1       //me va a la fila siguiente 
    sub x7,x7,1       //me corre un pixel en las x para la der
    sub x6,x6,1       //suma uno al contador cada vez pinto uno 
    cbnz x6,loop40

	//pinto costado derecho
	movz x8, 0x9A,lsl 16        //Color celeste.
	movk x8, 0xE3F2, lsl 00

    mov x15,340   //posición en x donde arranca
    mov x3,150  //posición en y donde arranca 
    mov x2,43   //contador y

loop42: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x15 
    lsl x0,x0,2 
    add x0,x0,x20
	mov x1,60   //contador x
loop43:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x1,x1,1
	cbnz x1,loop43      // if not end row, jump
    add x3,x3,1       //va a la fila siguiente 
    add x15,x15,1       //corre un pixel en las x para la derecha
    sub x2,x2,1       //suma uno al contador cada vez pinto uno 
    cbnz x2,loop42      // if not last row, jump

	//pinto costado izquierdo
	movz x8, 0x9A,lsl 16        //Color celeste.
	movk x8, 0xE3F2, lsl 00

    mov x15,250   //posición en x donde arranca
    mov x3,200  //posición en y donde arranca 
    mov x2,43   //contador y

loop44: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x15 
    lsl x0,x0,2 
    add x0,x0,x20
	mov x1,60   //contador x
loop45:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x1,x1,1
	cbnz x1,loop45      // if not end row, jump
    add x3,x3,1       //va a la fila siguiente 
    add x15,x15,1       //corre un pixel en las x para la derecha
    sub x2,x2,1       //suma uno al contador cada vez pinto uno 
    cbnz x2,loop44      // if not last row, jump

	/* Emprolijo parte de abajo */

	//Despintar  Triangulo (pared)
	movz x8, 0xDE, lsl 16 
	movk x8, 0xB887, lsl 00
   	mov x7,470  //en las x  Desde donde arranca 
    mov x3,300  //comienzo de las y 
    mov x6,31  //altura q quiero q me haga la linea 
    

loop36: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x7  
    lsl x0,x0,2 
    add x0,x0,x20
	mov x16,90
loop37:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x16,x16,1
	cbnz x16,loop37
    add x3,x3,1       //me va a la fila siguiente 
    sub x7,x7,1       //me corre un pixel en las x para la der
    sub x6,x6,1       //suma uno al contador cada vez pinto uno 
    cbnz x6,loop36


	//Despintar  Triangulo (marco ventana)
	movz x8,0x55,lsl 16
	movk x8, 0x5555,lsl 00 
   	mov x7,484 //en las x  Desde donde arranca 
    mov x3,285  //comienzo de las y 
    mov x6,15  //altura q quiero q me haga la linea 
    

loop38: 
    mul x0,x3,x11   //Cálculo de la posición de memoria del pixel que quiero 
    add x0,x0,x7  
    lsl x0,x0,2 
    add x0,x0,x20
	mov x16,50
loop39:
    stur w8,[x0]      // Set color of pixel N
	add x0,x0,4
	sub x16,x16,1
	cbnz x16,loop39
    add x3,x3,1       //me va a la fila siguiente 
    sub x7,x7,1       //me corre un pixel en las x para la der
    sub x6,x6,1       //suma uno al contador cada vez pinto uno 
    cbnz x6,loop38

	br lr

/*----PINTO AGUA----*/ 

pintar_agua:
	movz x8, 0xCC, lsl 16  //Color para el agua
	movk x8, 0xFFFF, lsl 00

	mov x2,1     // Altura del agua
	mov x3,125
	add x3,x3,x5      //Va iterando sobre las y, para que baje el dibujo 

base_a:
	mul x0,x3,x11	   //Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,303
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,5         // Ancho del agua 
loop46:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	       // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop46	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,base_a
	br lr 


/*----PINTO TERMO FIN CEBADA----*/ 
pintar_termo2:
	movz x8,0xA0,lsl 16     //Color para termo
	movk x8,0xA0A0 ,lsl 00
	mov x2,190      // Altura del termo 
	mov x3,126
	add x3,x3,x5      //Va iterando sobre las y, para que baje el dibujo 

base_t2:
	mul x0,x3,x11	   //Calculo la coordenada X del pixel que quiero actualizar
	add x0,x0,440
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,60         // Ancho del termo  
loop47:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	       // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop47	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,base_t2
	br lr 
 
pintar_tapa2:
	// tapa termo
	movz x8,0x00,lsl 16 //Color para tapa
	movk x8,0x0000 ,lsl 00
	
	mov x2,35      // Y Size marco
	mov x3,91
	add x3,x3,x5      //Va iterando sobre las y, para que baje el dibujo
tapa_t2:
	mul x0,x3,x11	//Calculo la coordenada X del pixel que quiero actualizar 
	add x0,x0,440
	lsl x0,x0,2 
	add x0,x0,x20
	mov x1,60      // Ancho de la tapa 
loop48:
	stur w8,[x0]	   // Set color of pixel N
	add x0,x0,4	   // Next pixel
	sub x1,x1,1	   // decrement X counter
	cbnz x1,loop48	   // If not end row jump
	sub x2,x2,1	   // Decrement Y counter
    add x3, x3, 1
	cbnz x2,tapa_t2
	br lr 


delay:
	mov x7,0x1FFFF00		//defino constante delay
dy:
	sub x7,x7,1
	cbnz x7,dy
	br lr 


delay2:
	mov x7,0x1FFFFFFF		//defino constante delay
dy2:
	sub x7,x7,1
	cbnz x7,dy2
	br lr 


end:
	//---------------------------------------------------------------

InfLoop: 
	b InfLoop
  
