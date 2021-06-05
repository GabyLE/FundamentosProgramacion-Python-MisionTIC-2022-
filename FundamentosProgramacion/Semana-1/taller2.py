from tkinter import *
from tkinter import messagebox

v = Tk()
v.title("Hora Militar")

Label(v, text="Hora (formato H:M)").grid(row=0, column=0)
Label(v, text="a.m. o p.m.").grid(row=1, column=0)

txtHora = Entry(v, width=20)
txtHora.grid(row=0,column=1)

txtMomento = Entry(v, width=20)
txtMomento.grid(row=1,column=1)

def calcular():
    
    hora,min = txtHora.get().split(":")
    hora = int(hora)
    moment = txtMomento.get().lower()

    if moment == "p.m." or moment == "pm" or moment == "p.m":
        hora_M = hora + 12
    elif moment == "a.m." or moment == "am" or moment == "a.m":
        hora_M = hora
    else:
        messagebox.showerror("Advertencia", "Ingrese el momento del día. Mañana (a.m.) o tarde (p.m.)")
        return
    
    messagebox.showinfo("Resultado", "Son las {:02d}:{}".format(hora_M,min))
    txtMomento.delete(0,END)
    txtHora.delete(0,END)
    

Button(v, text="Calcular", command=calcular).grid(row=2, column=0, columnspan=2)

v.mainloop()