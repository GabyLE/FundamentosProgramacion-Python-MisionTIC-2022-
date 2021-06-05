from tkinter import *
import random

v = Tk()
v.title("Apuntado")
v.minsize(width= 300, height= 200)
v.configure(background= 'green')

# variables
cartas = []

# Funciones
def mostrarCarta(fila, columna, archivo):
    # Obtener la imagen desde el archivo
    imgCarta = PhotoImage(file= archivo)

    # Mostrar la imagen
    lblCarta = Label(v)
    lblCarta.grid(row= fila, column= columna)
    lblCarta.configure(image = imgCarta)
    lblCarta.image = imgCarta

def repartir():
    # Inicializa variable de control fila y columna para mostrar las cartas
    f = 1
    c = 0
    for i in range(0, 10):
        # Generar un número aleatorio entre 1 y 52
        nc = random.randrange(52) + 1

        # Agregar indice de la carta al vector
        cartas.append(nc)

        # Mostrar la carta
        mostrarCarta(f, c, "Carta" + str(nc) + ".gif")
        
        c = c + 1

# Buttons
Button(v, text= "Repartir", command= repartir).grid(row= 0, column=0)

v.mainloop()