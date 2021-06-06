from tkinter import *
import Util
from Dados import Dado

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

# variables globales
lanzamientos = 0
cenas = 0

# Instancias de Dado
d1 = Dado()
d2 = Dado()

# MÉTODOS
def iniciar():
    global lanzamientos, cenas
    lanzamientos = 0
    cenas = 0

    # Mostrar los contadores
    Util.mostrarCajaTexto(txtLanzamientos, lanzamientos)
    Util.mostrarCajaTexto(txtCenas, cenas)
    btnL.configure(state= NORMAL)


def lanzar():
    global lanzamientos, cenas
    # Lazar los dados y mostrar la imagen de los dades
    d1.lanzar()
    d1.mostrar(lblDado1)
    d2.lanzar()
    d2.mostrar(lblDado2)

    # Actualizar contador lanzaminetos
    lanzamientos += 1

    # contador cenas
    if d1.obtenerNumero() + d2.obtenerNumero() >= 11:
        cenas += 1

    # Mostrar los contadores
    Util.mostrarCajaTexto(txtLanzamientos, lanzamientos)
    Util.mostrarCajaTexto(txtCenas, cenas)

btnL = Button(v, text="Lanzar", font= "Consolas 10", command= lanzar)
btnL.grid(row=1, column=0)
btnL.configure(state= DISABLED)
Button(v, text= "Iniciar", font= "Consolas 10", command= iniciar).grid(row= 1, column= 1)

v.mainloop()