# Entradas
nc = int(input("Cuántos cultivos tiene en la huerta: "))
huerta = list()

for i in range(nc):
    print("..............................................................................")
    cultivo = input("Ingrese nombre del cultivo: ")
    manten = input("Ingrese el horario de mantenimiento: ")
    regado = input("Ingrese el horario de regado: ")
    abono = input("Ingrese el horario de abono: ")
    etapa = input("Ingrese la etapa y el intervalo: ")

    huerta.append([i+1, cultivo, manten, regado, abono, etapa])

#print(huerta)

while True:
    print("..............................................................................")
    print("CULTIVOS:")
    for cultivo in huerta:
        print("    {}. {}".format(cultivo[0], cultivo[1]))
    print("    {}. Salir".format(nc+1))
    select_cult = int(input("Seleccione un cultivo: "))
    if select_cult == nc + 1: break
    print("..............................................................................")
    select_op = int(input("""OPCIONES:
    1. Horarios de gestión de cultivo
    2. Etapas del cultivo
    3. Salir
    
Seleccione una opción: """))
    select_cult = int(select_cult) - 1
    if select_op == 1:
        print("..............................................................................")
        print("Los horarios de gestión del cultivo {} son:".format(huerta[select_cult][1].upper()))
        print("   1. Mantenimiento: {}".format(huerta[select_cult][2]))
        print("   2. Regado: {}".format(huerta[select_cult][3]))
        print("   3. Abono: {}".format(huerta[select_cult][4]))
    elif select_op == 2:
        print("..............................................................................")
        print("La etapa del cultivo {} es:".format(huerta[select_cult][1].upper()))
        print("    {}".format(huerta[select_cult][5]))
    else:
        break
    