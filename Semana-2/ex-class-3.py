from datetime import date
from datetime import datetime

print("Calculo impuesto rodamiento")
print(".................................................................")
# ENTRADA
av = float(input("Avalúo vehículo: "))
prm = float(input("Porcentaje Rentas Municipales: "))
vs = float(input("Valor semaforización: "))
vm = float(input("Valor multa: "))
tim = float(input("Tasa interés mensual: "))

# Para el mismo año
print(".................................................................")
print("Fecha plazo con descuento:")
print("Mes: ENE->1 FEB->2 MAR->3 ABR->4 MAY->5 JUN->6 JUL->7 AGO->8 SEP->9 OCT->10 NOV->11 DIC->12")
mfpd = int(input("Mes elegido: "))
dfpd = int(input("Día: "))
afpd = int(input("Año: "))
print(".................................................................")
print("Fecha plazo final:")
print("Mes: ENE->1 FEB->2 MAR->3 ABR->4 MAY->5 JUN->6 JUL->7 AGO->8 SEP->9 OCT->10 NOV->11 DIC->12")
mfpf = int(input("Mes elegido: "))
dfpf = int(input("Día: "))
afpf = int(input("Año: "))
print(".................................................................")
print("Fecha pago:")
print("Mes: ENE->1 FEB->2 MAR->3 ABR->4 MAY->5 JUN->6 JUL->7 AGO->8 SEP->9 OCT->10 NOV->11 DIC->12")
mfp = int(input("Mes elegido: "))
dfp = int(input("Día: "))
afp = int(input("Año: "))
print(".................................................................")

# PROCESO
fpd = date(afpd, mfpd, dfpd)
fpf = date(afpf, mfpd, dfpd)
fp = date(afp, mfpd, dfpd)

vi = av * 0.01 * (1 + prm / 100) + vs

if fp <= fpd:
    vi = vi * 0.9
else:
    if fp > fpf:
        dm = (fp - fpf).days / 30
        vi = vi * (1 + dm * tim/100) + vm

print("El valor del impuesto es:", vi)