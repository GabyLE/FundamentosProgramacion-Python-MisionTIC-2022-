print("Hora Militar")

# entradas
h = int(input("Ingrese hora:"))
min = int(input("Ingrese minutos: "))
jor = int(input("Elija la jornada: 1-> a.m. 2-> p.m. : "))

# validaciones
if h in range(1,13) and \
    min in range(0,60) and \
    jor in range(1,3):

    # proceso
    hm = h
    if jor == 2 and hm < 12:
        hm += 12
    elif hm == 12 and jor == 1:
        hm = 0
    
    # salida
    print("La hora militar es {:02d}{:02d}".format(hm, min))

else:
    print("Datos no válidos")



