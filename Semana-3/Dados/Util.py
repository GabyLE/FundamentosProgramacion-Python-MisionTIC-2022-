from tkinter import *

def agregarImagen(ventana, archivo, fila, columna):
    img = PhotoImage(file=archivo)
    lbl= Label(ventana)
    lbl.config(image=img)
    lbl.image=img
    lbl.grid(row=fila, column=columna)
    return lbl

def agregarCajaTextoSalida(ventana, ancho, fila, columna, fuente):
    txt = Entry(ventana, width=ancho, font=fuente)
    txt.grid(row=fila, column=columna)
    txt.configure(state=DISABLED)
    return txt
    
def mostrarCajaTexto(txt, valor):
    txt.configure(state=NORMAL)
    txt.delete(0, END)
    txt.insert(0, valor)
    txt.configure(state=DISABLED)
