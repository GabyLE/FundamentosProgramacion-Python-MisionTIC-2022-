from tkinter import *
from tkinter import messagebox
import re
import math

# DISEÑO DE LA VENTANA
v = Tk()
v.title("Serie de Taylor función Coseno")
# etiquetas
Label(v, text="Elementos n").grid(row=0, column=0)
Label(v, text="Valor de x").grid(row=1, column=0)
Label(v, text="error").grid(row=3, column=0)
# entradas
txtN = Entry(v, width=10)
txtN.grid(row=0, column=1)
txtX = Entry(v, width=10)
txtX.grid(row=1, column=1)

# salida
txtSenX = Entry(v, width=30)
txtSenX.grid(row=2, column=1)
txtSenX.configure(state="readonly")

txtError = Entry(v, width=30)
txtError.grid(row=3, column=1)
txtError.configure(state="readonly")

# PROCESO
def calcular():
    # validar datos de entrada
    if re.match("^[-]?[0-9]+[.]?[0-9]*$", txtN.get()) and \
        re.match("^[-]?[0-9]+[.]?[0-9]*$", txtX.get()):

        n = int(txtN.get())
        x = float(txtX.get())
        suma = 0
        for i in range(n+1):
            suma += (-1)**i/(math.factorial(2*i))*x**(2*i)

        error =  abs((suma - math.cos(x)) / math.cos(x)) * 100      

        txtSenX.configure(state="normal")
        txtSenX.delete(0,END)
        txtSenX. insert(0, str(suma))
        txtSenX.configure(state="readonly")

        txtError.configure(state="normal")
        txtError.delete(0,END)
        txtError. insert(0, str(error))
        txtError.configure(state="readonly")
            
    else:
        messagebox.showerror("", "Datos no válidos para la gráfica")


# botón
btnG = Button(v, text="cos(x)", command=calcular)
btnG.grid(row=2, column=0)

v.mainloop()

