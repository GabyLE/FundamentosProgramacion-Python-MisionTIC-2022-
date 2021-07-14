import random
from  tkinter import *

class Carta:
    
    def __init__(self):
        self.indice = random.randrange(1, 53)

    def mostrarCarta(self,fila, columna, frame):
        # Obtener la imagen desde el archivo
        archivo = "../cartas/Carta" + str(self.indice) + ".gif"
        imgCarta = PhotoImage(file= archivo)

        # Mostrar la imagen
        lblCarta = Label(frame)
        lblCarta.grid(row= fila, column= columna, padx=4, pady=4)
        lblCarta.configure(image = imgCarta)
        lblCarta.image = imgCarta

        return lblCarta