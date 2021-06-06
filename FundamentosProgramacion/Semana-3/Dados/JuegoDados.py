from tkinter import *
import Util

#crear ventana
v = Tk()
v.title("Juego de Dados")
v.configure(background= '#0B3442')

#Imagenes de los dados
lblDado1=Util.agregarImagen(v, "1.png", 0, 0)
lblDado2=Util.agregarImagen(v, "1.png", 0, 1)

#Etiquetas
Label(v, text="Lanzamientos", font= "Consolas 10", fg= 'white', bg='#0B3442').grid(row=2, column=0)
Label(v, text="Cenas", font= "Consolas 10",  fg= 'white', bg='#0B3442').grid(row=2, column=1)
#Cajas de texto para mostrar estado de los lanzamientos
txtLanzamientos=Util.agregarCajaTextoSalida(v, 3, 3, 0, "Arial 48 bold")
txtCenas=Util.agregarCajaTextoSalida(v, 3, 3, 1, "Arial 48 bold")


Button(v, text="Lanzar", font= "Consolas 10").grid(row=1, column=0)
Button(v, text= "Iniciar", font= "Consolas 10").grid(row= 1, column= 1)



v.mainloop()