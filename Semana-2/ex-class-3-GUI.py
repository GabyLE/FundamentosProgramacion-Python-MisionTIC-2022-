from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import re

v = Tk()
v.title("Pago de subsidio de transporte")

# ENTRADAS
Label(v, text= "Avalúo vehículo").grid(row= 0, column=0)
txtAv = Entry(v, width=15)
txtAv.grid(row=0, column=1)

Label(v, text= "Porcentaje Rentas Municipales").grid(row= 1, column=0)
txtPrm = Entry(v, width=15)
txtPrm.grid(row=1, column = 1)

Label(v, text= "Valor semaforización").grid(row= 2, column=0)
txtVs = Entry(v, width=15)
txtVs.grid(row=2, column=1)

Label(v, text= "Valor multa").grid(row= 3, column=0)
txtVm = Entry(v, width=15)
txtVm.grid(row=3, column=1)

Label(v, text= "Tasa interés mensual").grid(row= 4, column=0)
txtTim = Entry(v, width=15)
txtTim.grid(row=4, column=1)

Label(v, text= "Mes").grid(row=5, column=1)
Label(v, text="Día").grid(row=5, column=3)

meses = ['Enero', 'Febrero', 'Marzo','Abril', 'Mayo', 'Junio', 'Julio', 'Agosto','Septiembre', 'Octubre', 'Noviembre','Diciembre']
#dias = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ]
Label(v, text="Fecha Plazo Descuento").grid(row=6, column=0)
cmbMesFPD = ttk.Combobox(v, width=10)
cmbMesFPD.grid(row=6, column=1)
cmbMesFPD['values'] = meses
txtDiaFPD = Entry(v, width=5)
txtDiaFPD.grid(row=6, column=3)

Label(v,text="Fecha Plazo Final").grid(row=7, column=0)
cmbMesFPF = ttk.Combobox(v, width=10)
cmbMesFPF.grid(row=7, column=1)
cmbMesFPF['values'] = meses
txtDiaFPF = Entry(v, width=5)
txtDiaFPF.grid(row=7, column=3)

Label(v, text="Fecha Pago").grid(row=8,column=0)
cmbMesFP = ttk.Combobox(v, width=10)
cmbMesFP.grid(row=8, column=1)
cmbMesFP['values'] = meses
txtDiaFP = Entry(v, width=5)
txtDiaFP.grid(row=8, column=3)

# Mostrar resultado
txtVI = Entry(v, width=20)
txtVI.grid(row=9, column=1)
txtVI.config(state=DISABLED)

# PROCESO
def CalcularImpuesto():
    # validar los datos de entrada
    # Expresiones Regulares:
    #   "^[0-9]+$" -> Enteros positivos
    #   "^[-]?[0-9]+$" -> Enteros
    #   "^[0-9]+[.]?[0-9]*$" -> Reales positivos
    #   "^[-]?[0-9]+[.]?]0-9]" -> Reales
    if re.match("^[0-9]+$", txtAv.get()) and \
        re.match("^[0-9]+[.]?[0-9]*$", txtPrm.get()) and \
        re.match("^[0-9]+$", txtVs.get()) and \
        re.match("^[0-9]+$", txtVm.get()) and \
        re.match("^[0-9]+[.]?[0-9]*$", txtTim.get()) and \
        re.match("^[0-3]?[0-9]$", txtDiaFP.get()) and \
        re.match("^[0-3]?[0-9]$", txtDiaFPF.get()) and \
        re.match("^[0-3]?[0-9]$", txtDiaFPD.get()) and \
        cmbMesFPD.current() >= 0 and cmbMesFPF.current() >= 0 and cmbMesFP.current() >= 0:
        # obtener datos de entrada
        av = float(txtAv.get())
        prm = float(txtPrm.get())
        vs = float(txtVs.get())
        tim = float(txtTim.get())
        vm = float(txtVm.get())
        # Fechas
        fpd = date(date.today().year, cmbMesFPD.current()+1, int(txtDiaFPD.get()))
        fpf = date(date.today().year, cmbMesFPF.current()+1, int(txtDiaFPF.get()))
        fp = date(date.today().year, cmbMesFP.current()+1, int(txtDiaFP.get())) 

        # PROCESO
        vi = av * 0.01 * (1 + prm/100) + vs # 1% del avalúo - porcentaje sobre 
        if fp < fpd: # si la fecha de pago es antes de la fecha de plazo de descuento
            vi = vi * 0.9 # descuento del 10%
        elif fp > fpf: # si la fecha de pago se pasó de la fecha de plazo final
            dm = abs((fp -fpf).days) / 30 # diferencia de mases fecha de pago y fecha plazo final
            vi = vi * (1 + dm * tim / 100) + vm # el valor del impuesto se le suma el valor de la multa y unos intereses MENSUALES
        
        # Mostrar el resultado
        txtVI.configure(state=NORMAL)
        txtVI.delete(0,END)
        txtVI.insert(0, str(vi))
        txtVI.configure(state=DISABLED)

Button(v, text="Calcular Impuesto", command=CalcularImpuesto).grid(row=9, column=0)

v.mainloop()