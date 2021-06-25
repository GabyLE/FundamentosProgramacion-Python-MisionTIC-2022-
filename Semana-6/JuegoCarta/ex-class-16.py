#Importar la libreria para interfaces graficas
from tkinter import *

#Importar la libreria para PESTAÑAS
from tkinter.ttk import Notebook

#importar CAJA DE MENSAJES
from tkinter import messagebox
from Jugador import Jugador

from Baraja import Baraja


#Crear una ventana
v = Tk()
v. title("Juego del Apuntado")
v.minsize(width=300, height=200)

#Crear el menu principal
mnuP = Menu(v)
#Agregar a la ventana
v.config(menu=mnuP)

# instancias de los dos Jugadores
j1 = Jugador()
j2 = Jugador()

# baraja del juego
b = Baraja()

def repartir():
    global j1, j2
    j1.repartir(b)
    j2.repartir(b)

    j1.mostrar(f1)
    j2.mostrar(f2)

def verificar():
    global j1, j2

    # pregunta por el indice de la pestaña seleccionada
    if nbJ.index(nbJ.select()) == 0:
        messagebox.showinfo("JUGADOR 1", j1.verificar())
    elif nbJ.index(nbJ.select()) == 1:
        messagebox.showinfo("JUGADOR 2", j2.verificar())

def salir():
    v.destroy()
    quit()

#opciones del menu
mnuJ = Menu(mnuP)
mnuJ.add_command(label="Repartir", command=repartir)
mnuJ.add_command(label="Verificar", command=verificar)
mnuP.add_cascade(label="Juego", menu=mnuJ)

mnuP.add_command(label="Salir", command=salir)

#Definir las pestañas del juego
nbJ = Notebook(v)
nbJ.pack(fill="both", expand="yes")

f1 = Frame(nbJ, bg="green")
f2 = Frame(nbJ, bg="lightblue")

nbJ.add(f1, text="Jugador 1")
nbJ.add(f2, text="Jugador 2")


v.mainloop()


