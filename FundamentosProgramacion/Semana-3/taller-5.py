from tkinter import *
import random

v = Tk()
v.title("Apuntado")
v.minsize(width= 300, height= 200)
v.configure(background= 'green')

# Button
Button(v, text= "Repartir", command= repartir).grid(row=0, column=0)
Button(v, text="Chequear", command=verificar).grid(row=0, column=1)

v.mainloop()
