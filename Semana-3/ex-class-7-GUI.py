from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Varios
import re

v = Tk()
v.title("Cálculos Estadísticos")

# Label
Label(v, text= "Dato",font="Consolas 12").grid(row= 0, column= 0)

# Entry
txt_dato = Entry(v, width= 20, font="Consolas 12")
txt_dato.grid(row= 0, column= 1)

txtCalculo = Entry(v, width= 20, font= "Consolas 12")
txtCalculo.grid(row= 3, column= 1)
txtCalculo.configure(state= DISABLED)

# Combobox
opciones = ["Sumatoria", "Promedio", "Desviación", "Moda", "Mediana"]
cmbOpciones = ttk.Combobox(v, width= 20, font="Consolas 12")
cmbOpciones.grid(row= 3, column=0)
cmbOpciones['values'] = opciones

# ListBox
lstDatos = Listbox(v, font="Consolas 12")
lstDatos.grid(row= 2, column=0, columnspan= 3)

# variables
datos = []
# *********************** FUNCIONES ****************************
def agregar():
    # validaciones
    if re.match("^[-]?[0-9]+[.]?[0-9]*$", txt_dato.get()):
        dato = float(txt_dato.get())
        datos.append(dato)
        Varios.mostrar(lstDatos, datos)
        txt_dato.delete(0, END)

    else:
        messagebox.showerror("", "El dato no es númerico")
        txt_dato.delete(0, END)
    
def quitar():
    # curselection toma el valor del item seleccionado de la lista
    if lstDatos.curselection()[0] >= 0:
        del datos[int(lstDatos.curselection()[0])]
        Varios.mostrar(lstDatos, datos)

def calcular():
    if cmbOpciones.current() == 0:
        suma = Varios.sumatoria(datos)
        Varios.mostrarCajaTexto(txtCalculo, suma)

    elif cmbOpciones.current() == 1:
        promedio = Varios.promedio(datos)
        Varios.mostrarCajaTexto(txtCalculo, promedio)

    elif cmbOpciones.current() == 2:
        desviacion = Varios.desviacion(datos)
        Varios.mostrarCajaTexto(txtCalculo, desviacion)

    elif cmbOpciones.current() == 3:
        moda = Varios.moda(datos)
        Varios.mostrarCajaTexto(txtCalculo, moda)

    elif cmbOpciones.current() == 4:
        mediana = Varios.mediana(datos)
        Varios.mostrarCajaTexto(txtCalculo, mediana)

    else:
        messagebox.showerror("", "Seleccione una opción")

def ordenar():
    datos.sort()
    Varios.mostrar(lstDatos, datos)


# Buttons
Button(v, text= "Agregar", font="Consolas 12", command= agregar).grid(row= 1, column=0)
Button(v, text= "Quitar", font="Consolas 12", command= quitar).grid(row=1, column= 1)
Button(v, text= "Ordenar", font="Consolas 12", command= ordenar).grid(row=1, column= 2)
Button(v, text= "Calcular", font="Consolas 12", command= calcular).grid(row= 4, column= 0, columnspan= 3)

v.mainloop()