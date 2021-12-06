# 193287_TOLEDO
Proyecto final Programación concurrente

pasos para usar el programa: 
1. en la parte de "Pedido:" ingresar el nombre del pedido (pizza, hamburgesa, tacos, etc)
2. en la parte de "Cantidad" ingresar un numero entero positivo de la cantidad de este pedido que desea meter a la cola 
3. ya teniendo estos dos campos llenos, daremos click en el boton "Tomar pedido" para agregar estos pedidos a la lista de pedidos
4. se mostrara un mensaje el numero de pedido, nombre de el pedido y su tiempo que tardara (en minutos)
5. si se desea hacer otro pedido, volver a hacer pasos 1, 2 y 3
6. cuando ya no quiera pedir más, daremos click en el boton "Pasar pedido". Este creara 3 hilos, cada hilo representara un cocinero. Este tomara un elemento de la lista de pedidos y lo prepaprará (esperará el tiempo estimado de dicho pedido), despues de esto vera si existen aun elementos en la lista de pedidos para agarrar otro y realizarlo. en el caso de que ya no haya mas pedidos, el hilo (cocinero) terminara.


193287-TOLEDO COELLO MARÍA FERNANDA
193761-IBAÑEZ TOLEDO JOSE MIGUEL

nota: profesor el programa funciona bien, su unica excepción es que no logramos configurar los label de la interfaz para que mostrara el pedido que cada chef estaba realizando. la impresion en la consola muestra el proceso de los pedidos.
