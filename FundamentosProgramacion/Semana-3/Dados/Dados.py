from tkinter import *
import random

class Dado:
    # Método constructor
    def __init__(varClase):
        varClase.numero = 1

    def lanzar(varClase):
        '''Generar aleatoriamente el dado'''
        varClase.numero = random.randrange(1,7)

    def mostrar(varClase, lblDado):
        # Cargar la imagen
        imgDado = PhotoImage(file= = "./" + str(varClase.numero) + ".png")
        # Mostrar imagen
        lblDado.config(image = imgDado)
        lblDado.image = imgDado

    def obtenerNumero(varClase):
        return varClase.numero