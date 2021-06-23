from tkinter import *
from tkinter import ttk

def desdeArchivo(nombreArchivo, treeview):
    with open(nombreArchivo, 'r') as objFile:
        for linea in objFile:
            datos = linea.split(";")
            if len(datos) >= 4:
                treeview.insert("", END, text="", values = (datos[0] + " " + datos[1], datos[3].strip(), datos[2]))
        
def limpiarEntry(txtName, txtLastName, txtMovil, txtMail):
    txtName.delete(0, END)
    txtLastName.delete(0, END)
    txtMovil.delete(0, END)
    txtMail.delete(0, END)