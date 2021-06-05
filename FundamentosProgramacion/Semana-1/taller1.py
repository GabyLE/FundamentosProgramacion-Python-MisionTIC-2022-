print("Cálculo de un tiquete aéreo")

c_ida = float(input("Ingrese el valor del trayecto de ida: "))
c_regreso = float(input("Ingrese el valor del trayecto de regreso: "))
porcen = float(input("Ingrese el porcentaje de la tasa aeropuertuarias: "))/100

v_tiquete = (c_ida+c_regreso)*(1+porcen)

print("El valor total del tiquete aéreo es ${}".format(v_tiquete))












