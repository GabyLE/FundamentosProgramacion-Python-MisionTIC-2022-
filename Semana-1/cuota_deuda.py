print("Programa para calcular la cuota de una deuda")

#Obtener los datos de entrada
monto = float(input("Monto a prestar:"))
tasa = float(input("Tasa de interes:"))
periodo = float(input("Periodo:"))

#Calculo de la cuota
tasa = tasa/100
x = (1 + tasa)**periodo
cuota = monto*x*tasa/(x-1)

#Muestra el valor de la cuota calculado
print("La cuota es: {0:.2f}".format(cuota))
