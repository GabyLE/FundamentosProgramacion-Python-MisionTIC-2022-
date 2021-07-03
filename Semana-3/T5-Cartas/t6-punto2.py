from tkinter import *
# Importa el modulo ttk que contine el widget Notebook
from tkinter import ttk
import random
# Importa funciones auxiliares
import Funciones as fun
from tkinter import messagebox

# Ventana
root = Tk()
root.title("Juego de Cartas")
root.configure(bg= "#2D2A55")

# Contenedor de Notebook
frmTab = Frame(root)
frmTab.grid(row=1, column=0, columnspan=3)

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

# FUNCIONES
def repartir():

    global cartas_P1, cartas_P2
    cartas_P1 = []
    cartas_P2 =[]
    # Inicializa variable de control fila y columna para mostrar las cartas
    f = 1
    c = 0
    cond = 0
    while cond != -1:
        # Genera número aleatorio
        nc1 = random.randint(1, 52)
        nc2 = random.randint(1, 52)
        # algoritmo para asegurarse de que no se repitan cartas entre las 10 repartidas ni los dos jugadores
        if len(cartas_P1) < 10:
            if nc1 not in cartas_P1 and nc1 not in cartas_P2:
                cartas_P1.append(nc1)
        if len(cartas_P2) < 10:
            if nc2 not in cartas_P2 and nc2 not in cartas_P1:
                cartas_P2.append(nc2)
        if len(cartas_P2) == 10 and len(cartas_P1) == 10:
            cond = -1
    
    for i in range(0, 10):
        nc1 = cartas_P1[i]
        nc2 = cartas_P2[i]
        # Mostrar la carta
        fun.mostrarCarta(f, c, "cartas/Carta" + str(nc1) + ".gif", tab1)
        fun.mostrarCarta(f, c, "cartas/Carta" + str(nc2) + ".gif", tab2)
        
        c = c + 1

def cartaMayor():
    cartaMayor1 = fun.cartaMayorRepartida(cartas_P1)
    cartaMayor2 = fun.cartaMayorRepartida(cartas_P2)

    aces = [1, 14, 27, 40]
    if cartaMayor1 in aces and cartaMayor2 in aces:
        if cartaMayor1 > cartaMayor2:
            ncMayor = cartaMayor1
            mensaje = "Gana el Jugador 1"
        else:
            ncMayor = cartaMayor2
            mensaje = "Gana el Jugador 2"
    elif cartaMayor1 in aces:
        ncMayor = cartaMayor1
        mensaje = "Gana el Jugador 1"
    elif cartaMayor2 in aces:
        ncMayor = cartaMayor2
        mensaje = "Gana el Jugador 2"
    else:
        if cartaMayor1 > cartaMayor2:
            ncMayor = cartaMayor1
            mensaje = "Gana el Jugador 1"
        else:
            ncMayor = cartaMayor2
            mensaje = "Gana el Jugador 2"
    
    fun.mostrarCarta(0, 2, "cartas/Carta" + str(ncMayor) + ".gif", root)
    messagebox.showinfo("Ganador", mensaje)


# Boton
Button(root, text= "Repartir", font="Consolas 10", command= repartir).grid(row=0, column=0)
Button(root, text= "Carta Mayor", font="Consolas 10", command= cartaMayor).grid(row=0, column=1)

root.mainloop()