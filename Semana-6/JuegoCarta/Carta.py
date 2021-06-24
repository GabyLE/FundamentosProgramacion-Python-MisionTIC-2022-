import random
from tkinter import Label, PhotoImage
from Enumerados import *

class Carta():

    # método constructor
    def __init__(varClase):
        # generar numero aleatorio entre 1 y 52
        varClase.indice = random.randrange(1, 53)

    def obtenerPinta(varClase):
        if varClase.indice <= 13:
            return PintaCarta.TREBOL
        elif varClase.indice <= 26:
            return PintaCarta.PICA
        elif varClase.indice <= 39:
            return PintaCarta.CORAZON
        else:
            return PintaCarta.DIAMANTE

    def mostrar(varClase, frm, x, y):
        lbl = Label(frm)
        img = PhotoImage(file= ".\Carta" + str(varClase.indice) + ".gif")
        lbl.config(image = img) # dice al label que no va a ser de texto sino de imagen
        lbl.imgage = img  # asigna la imagen a label
        lbl.place(x=x, y=y) 

    def obtenerIndiceNumero(varClase):
        '''Retorna un numero del 1 al 13 de acuerdo a la carta'''
        n = varClase.indice % 13
        if n == 0:
            n = 13
        return n