from tkinter import *

from tkinter import messagebox

import re

v = Tk()
v.wm_title("Conversion a Romano")
v.minsize(width=300, height=200)

Label(v, text="Numero Arabigo").grid(row=0)
txtA = Entry(v, width=10)
txtA.grid(row=0, column=1)

txtR = Entry(v, width=20)
txtR.grid(row=1, column=1)
txtR.configure(state=DISABLED)

def Calcular():
    if re.match("^[0-9]+$", txtA.get()):
        a = int(txtA.get())

        #Proceso
        r = ""
        while a > 0:
            if a >= 1000:
                r = r + "M"
                a = a - 1000
            elif a >= 900:
                r = r + "CM"
                a = a - 900
            elif a >= 500:
                r = r + "D"
                a = a - 500
            elif a >= 400:
                r = r + "CD"
                a = a - 400
            elif a >= 100:
                r = r + "C"
                a = a - 100
            elif a >= 90:
                r = r + "XC"
                a = a - 90
            elif a >= 50:
                r = r + "L"
                a = a - 50
            elif a >= 40:
                r = r + "XL"
                a = a - 40
            elif a >= 10:
                r = r + "X"
                a = a - 10
            elif a >= 9:
                r = r + "IX"
                a = a - 9
            elif a >= 5:
                r = r + "V"
                a = a - 5
            elif a >= 4:
                r = r + "IV"
                a = a - 4
            else:
                r = r + "I"
                a = a - 1


        txtR.configure(state=NORMAL)
        txtR.delete(0, END)
        txtR.insert(0, r)
        txtR.configure(state=DISABLED)

    else:
        messagebox.showerror("El dato debe ser un numero entero")

Button(v, text="Convertir", command=Calcular).grid(row=1)
