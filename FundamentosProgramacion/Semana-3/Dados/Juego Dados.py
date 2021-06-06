from tkinter import *
import Util

#crear ventana
v = Tk()
v.title("Juego de Dados")

#Imagenes de los dados
lblDado1=Util.agregarImagen(v, "1.png", 0, 0)
lblDado2=Util.agregarImagen(v, "1.png", 0, 1)

#Etiquetas
Label(v, text="Lanzamientos").grid(row=2, column=0)
Label(v, text="Cenas").grid(row=2, column=1)
#Cajas de texto para mostrar estado de los lanzamientos
txtLanzamientos=Util.agregarCajaTextoSalida(v, 3, 3, 0, "Arial 48 bold")
txtCenas=Util.agregarCajaTextoSalida(v, 3, 3, 1, "Arial 48 bold")


Button(v, text="Lanzar").grid(row=1, column=0)



