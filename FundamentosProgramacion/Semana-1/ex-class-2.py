#cargar la librería GUI
from tkinter import *
from tkinter import messagebox
import math
import cmath #numeros imaginarios

v = Tk()
v.title("Raices ecuación cuadrática")

Label(v, text="Coeficiente A:").grid(row=0,column=0)
Label(v, text="Coeficiente B:").grid(row=1,column=0)
Label(v, text="Coeficiente C:").grid(row=2,column=0)

txtA = Entry(v, width=10)
txtA.grid(row=0,column=1)
txtB = Entry(v, width=10)
txtB.grid(row=1,column=1)
txtC = Entry(v, width=10)
txtC.grid(row=2,column=1)

Label(v, text="Raíz X1:").grid(row=4,column=0)
Label(v, text="Raíz X2:").grid(row=5,column=0)

txtX1 = Entry(v, width=30)
txtX1.grid(row=4,column=1)
txtX1.configure(state=DISABLED)

txtX2 = Entry(v, width=30)
txtX2.grid(row=5,column=1)
txtX2.configure(state=DISABLED)

def calcularRaices():
    #obtener datos de entrada
    a = float(txtA.get())
    b = float(txtB.get())
    c = float(txtC.get())

    #proceso
    if a != 0:
        r = b**2 - 4*a*c

        if r > 0:
            x1 = (-b + math.sqrt(r))/(2*a)
            x2 = (-b - math.sqrt(r))/(2*a)
        else:
            x1 = (-b + cmath.sqrt(r))/(2*a)
            x2 = (-b - cmath.sqrt(r))/(2*a)
        
        txtX1.configure(state=NORMAL)
        txtX1.delete(0, END)
        txtX1.insert(0, str(x1))
        txtX1.configure(state=DISABLED)

        txtX2.configure(state=NORMAL)
        txtX2.delete(0, END)
        txtX2.insert(0, str(x1))
        txtX2.configure(state=DISABLED)
    
    else:
        messagebox.showerror("Error al calcular","La ecuación no es cuadrática")

Button(v, text="Calcular", command=calcularRaices).grid(row=3, column=0, columnspan=2)

v.mainloop()