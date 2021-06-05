#cargar la libreria para GUI
from tkinter import *  

#crear la ventana
ventana = Tk()  
ventana.title("Cálculo Semana Santa")
ventana.minsize(400,200) #pixeles

#Agregar etiqueta
Label(ventana,text="Año a calcular: ").grid(row=0, column=0)

#Agregar cajas de texto
txtYear = Entry(ventana, width=10)
txtYear.grid(row=0, column=1)

txtFecha = Entry(ventana, width=50)
txtFecha.grid(row=1, column=1)
txtFecha.configure(state=DISABLED)

def obtenerSemanaSanta():
    #print("Programa para calcular el número de días después del 15 de marzo para conocer el día del año que comienza Semana Santa")
    year = int(txtYear.get())

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30

    dias = d + (2*b + 4*c + 6*d +5) % 7
    fecha = 15 + dias
    mes = "Marzo"
    if fecha > 31:
        fecha = fecha - 31
        mes = "Abril"

    txtFecha.configure(state=NORMAL)
    txtFecha.delete(0,END)
    txtFecha.insert(0,"En el año {} el Domingo de Ramos sería el {} de {}".format(txtYear.get(),fecha,mes))
    txtYear.delete(0,END)
    txtFecha.configure(state=DISABLED)
    #insert(posición a la que inicia,texto)
    


#Agregar botón
Button(ventana, text="Calcular", command=obtenerSemanaSanta).grid(row=1,column=0)
ventana.mainloop()


