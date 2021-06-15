# Aplicación para registro de cultivos de una huerta
# Estudiante: Denis Gabriela López Esquivel
print("Registro de cultivos")

#Entrada de datos por consola y definición de variable
nCult = int(input("¿Cuántos cultivos tiene en la huerta? "))

for i in range(nCult):
    #Entrada de datos por consola y definición de variables
    nameCult = input("Nombre del cultivo: ")
    cantCult = int(input(f"¿Cuánt@s {nameCult} tiene en el cultivo? "))
    timeCult = float(input(f"¿Hace cuánto ha estado cultivando {nameCult} (en meses)? "))
    promCult = input("¿Tiene algún problema con el cultivo? (si o no) ")

    #Imprimir datos por consola
    print(".............................")
    print("Nombre: " + nameCult)
    print("Cantidad: " + str(cantCult))
    print("Tiempo: " + str(timeCult) + " meses")
    print("Problema: " + promCult)
    print(".............................")