import tkinter
import random
from multiprocessing import Process
from threading import Thread, Lock
import time
import threading

contador = 1
#colaPedidos = []
pedidos = []


class Pedido:
    def __init__(self, nombre, num, tiempo):
        print("soy un nuevo pedido")
        self.nombre = nombre
        self.numero = num
        self.tiempo = tiempo

    def cocinar(self, tiempo):
        print("su tiempo de elaboracion es:", tiempo, "minutos")


def guardarPedido(nombre, cantidad):
    nuevaCantidad = int(cantidad)
    tiempo = random.randrange(1, 10)
    for i in range(nuevaCantidad):
        nuevoPedido = Pedido(nombre, 1, tiempo)
        pedidos.append(nuevoPedido)
    platillo.delete(0,"end")
    CantidadEntry.delete(0,"end")
    cadena = "pedido: "+cantidad+" "+nombre+" tardara "+str(tiempo)+ " min"
    pedidosLB.config(text=cadena)

def mandarMensaje(mensaje, x):
    if x == 1:
        lbl_cocinero1.config(text=mensaje)
    elif x == 2:
        lbl_cocinero2.config(text=mensaje)
    elif x == 3:
        lbl_cocinero3.config(text=mensaje)

def cocina(numero):
    while pedidos:
        pedido = pedidos.pop()
        print("chef ",numero," preparando ", pedido.nombre, " durara ", pedido.tiempo)
        texto = "chef " + str(numero) + " preparando " + str(pedido.nombre) + " durara " + str(pedido.tiempo)
        #lbl_cocinero1.config(text=texto)
        #mandarMensaje(texto, numero)
        
        time.sleep(pedido.tiempo)
        print("chef ",numero," termino de preparar ", pedido.nombre)
        #lbl_cocinero1.config(text="")
    if (len(pedidos) == 0):
        print("el chef ",numero," termino ")
        mensaje = "chef " + str(numero) + " termino "
        """ if numero == 1:
            lbl_cocinero1.config(text=texto)
        elif numero == 2:
            lbl_cocinero2.config(text=texto)
        elif numero == 3:
            lbl_cocinero3.config(text=texto)
 """
    #lbl_cocinero1.config(text=texto)

def mandarPedido():
    
    if pedidos == []:
        pedidosLB.config(text="no hay ningun pedido para mandar :(")
    else:
        pedidosLB.config(text="realizando pedidos...") #este mensaje no cambia
        #print(pedidos)
        #creamos hilo
        chef1 = Thread(name='cocinero 1', target=cocina, args=(1, ))
        chef2 = Thread(name='cocinero 2', target=cocina, args=(2, ))
        chef3 = Thread(name='cocinero 3', target=cocina, args=(3, ))
        #corremos hilo
        chef1.start()
        chef2.start()
        chef3.start()

        chef1.join()
        chef2.join()
        chef3.join()
        lbl_cocinero1.config(text="1. Termino todos sus pedidos")
        lbl_cocinero2.config(text="2. Termino todos sus pedidos")
        lbl_cocinero3.config(text="3. Termino todos sus pedidos")



        
def validate_entry(text):
    return text.isdecimal()

ventana = tkinter.Tk()
ventana.geometry("900x600")
ventana.title("Restaurante")
label = tkinter.Label(ventana, text= "Restaurante", font="Helvetica 30")
label.pack()
pedidoLB = tkinter.Label(ventana, text="Pedido:", font="Helvetica 20")
pedidoLB.pack()
pedidoLB.place(relx=0.1, rely=0.1)
platillo = tkinter.Entry(ventana)
platillo.pack()
platillo.place(relx=0.23, rely=0.1, relheight=0.05, relwidth=0.55)
cantidadLB = tkinter.Label(ventana, text="Cantidad",  font="Helvetica 20")
cantidadLB.pack()
cantidadLB.place(relx=0.1, rely=0.2)
CantidadEntry = tkinter.Entry(
    validate="key",
    validatecommand=(ventana.register(validate_entry), "%S")
)
CantidadEntry.pack()
CantidadEntry.place(relx=0.23, rely=0.2, relheight=0.05)

boton = tkinter.Button(ventana, text="Tomar pedido", command=lambda: guardarPedido(platillo.get(), CantidadEntry.get()))
boton.pack()
boton.place(relx=0.5, rely=0.2, relheight=0.05)
boton2 = tkinter.Button(ventana, text="Pasar pedido", command=mandarPedido)
boton2.pack()
boton2.place(relx=0.65, rely=0.2, relheight=0.05)
pedidosLB = tkinter.Label(text="", font="Helvetica 20")
pedidosLB.pack()
pedidosLB.place(relx=0.2, rely=0.3)


img = tkinter.PhotoImage(file="cocinero.png")
img_cocinero1 = tkinter.Label(ventana, image = img)
img_cocinero1.pack()
img_cocinero1.place(relx=0.08, rely=0.5)
lbl_cocinero1 = tkinter.Label(ventana, text= "1. Preparando:", font="Helvetica 18")
lbl_cocinero1.pack()
lbl_cocinero1.place(relx=0.20, rely=0.55)

img_cocinero2 = tkinter.Label(ventana, image = img)
img_cocinero2.pack()
img_cocinero2.place(relx=0.08, rely=0.65)
lbl_cocinero2 = tkinter.Label(ventana, text= "2. Preparando:", font="Helvetica 18")
lbl_cocinero2.pack()
lbl_cocinero2.place(relx=0.20, rely=0.70)

img_cocinero3 = tkinter.Label(ventana, image = img)
img_cocinero3.pack()
img_cocinero3.place(relx=0.08, rely=0.80)
lbl_cocinero3 = tkinter.Label(ventana, text= "3. Preparando:", font="Helvetica 18")
lbl_cocinero3.pack()
lbl_cocinero3.place(relx=0.20, rely=0.85)
ventana.mainloop()