from tkinter import *
from Carta import Carta
from Jugador import Jugador
from Baraja import Baraja
from tkinter.ttk import Notebook
from tkinter import messagebox
import Funciones as f

# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, 'E:/misiontic-2022/fundamentosprogramacion/semana-7/utilidades')
import Util

# iconos
iconos = ["icons/repartir.png", "icons/mayor.png"]

# tooltip para los botones
txtToolTip = ["Repartir", "Carta Mayor"]

baraja = Baraja()

jugadores = []
jugadores.append(Jugador())
jugadores.append(Jugador())

tabs = []

# ventana
v = Tk()
v.title("Juego Cartas")


# barra botones
frmBarra = Frame(v)
frmBarra.grid(row=0, column=0, sticky=NW)
botones = Util.agregarBarra(frmBarra, iconos, txtToolTip)

# PESTAÑAS JUGADORES
# contenedor de notebook
frmNb = Frame(v)
frmNb.grid(row=1, column=0, columnspan=3)
# control de las pestañas
nb = Notebook(frmNb)

# creación de las pestañas
tabs.append(Frame(nb,bg = "green")) # jugador 1
tabs.append(Frame(nb,bg = "green")) # jugador 2
# añade pestañas
nb.add(tabs[0], text = "Jugador 1")
nb.add(tabs[1], text = "Jugador 2")
nb.pack(expand=YES, fill=BOTH)

def repartir():
    jugadores[0].repartir(baraja)
    jugadores[1].repartir(baraja)
    jugadores[0].mostrar(tabs[0])
    jugadores[1].mostrar(tabs[1])

def verificar():
    cartasMayores = []
    for i in range(len(jugadores)):
        cartasMayores.append(f.cartaMayorRepartida(jugadores[i].cartas))

    cartaMayor = f.cartaMayorRepartida(cartasMayores)
    cartaMayor.mostrarCarta(0,1,v)

    messagebox.showinfo("Ganador", "Gana el Jugador " + str(cartasMayores.index(cartaMayor)+1))


    # print(cartaMayor.indice)
    # print(cartasMayores.index(cartaMayor))

botones[0].configure(command = repartir)
botones[1].configure(command = verificar)



v.mainloop()