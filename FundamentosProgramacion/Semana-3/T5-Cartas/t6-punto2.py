from tkinter import *
# Importa el modulo ttk que contine el widget Notebook
from tkinter import ttk
import random

# Ventana
root = Tk()
root.title("Juego de Cartas")
root.configure(bg= "#2D2A55")

# Contenedor de Notebook
frmTab = Frame(root)
frmTab.grid(row=1, column=0, columnspan=2)

# Control de las pestañas
tabControl = ttk.Notebook(frmTab)

# Creación de las pestañas
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# Adding the tab
tabControl.add(tab1, text= "Jugador 1")
tabControl.add(tab2, text= "Jugador 2")

# Packin the tab control to make the tabs visible
tabControl.pack(expand= 1, fill = "both")

# Funciones
def mostrarCarta(fila, columna, archivo, frame):
    # Obtener la imagen desde el archivo
    imgCarta = PhotoImage(file= archivo)

    # Mostrar la imagen
    lblCarta = Label(frame)
    lblCarta.grid(row= fila, column= columna)
    lblCarta.configure(image = imgCarta)
    lblCarta.image = imgCarta

def repartir():

    global cartas_P1, cartas_P2
    cartas_P1 = []
    cartas_P2 =[]
    # Inicializa variable de control fila y columna para mostrar las cartas
    f = 1
    c = 0
    for i in range(0, 10):
        # Generar un número aleatorio entre 1 y 52
        nc1 = random.randrange(52) + 1
        nc2 = random.randrange(52) + 1

        # Agregar indice de la carta al vector
        cartas_P1.append(nc1)
        cartas_P2.append(nc2)

        # Mostrar la carta
        mostrarCarta(f, c, "Carta" + str(nc1) + ".gif", tab1)
        mostrarCarta(f, c, "Carta" + str(nc2) + ".gif", tab2)
        
        c = c + 1

def cartaMayor():
    t = 0

# Boton
Button(root, text= "Repartir", font="Consolas 10", command= repartir).grid(row=0, column=0)
Button(root, text= "Carta Mayor", font="Consolas 10", command= cartaMayor).grid(row=0, column=1)

root.mainloop()