#Importar la libreria para interfaces graficas
from tkinter import *

#Importar la libreria para PESTAÑAS
from tkinter.ttk import Notebook

#importar CAJA DE MENSAJES
from tkinter import messagebox

#Crear una ventana
v = Tk()
v. title("Juego del Apuntado")
v.minsize(width=300, height=200)

#Crear el menu principal
mnuP = Menu(v)
#Agregar a la ventana
v.config(menu=mnuP)

def repartir():
    messagebox.showinfo("Probando Menu", "Hizo clic en REPARTIR")

def verificar():
    messagebox.showinfo("Probando Menu", "Hizo clic en VERIFICAR")

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

nbJ.add(f1, text="Martin Estrada Contreras")
nbJ.add(f2, text="Raúl Vidal")





