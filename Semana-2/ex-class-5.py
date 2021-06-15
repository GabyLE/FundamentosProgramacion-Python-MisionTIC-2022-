print("Programa para convertir UCSA")
print("""Opciones: 
    Barril -> 1
    Galón -> 2
    Cuarto -> 3
    Pinta -> 4
    Onza- > 5""")
# ENTRADA
uo = int(input("Seleccione la unidad origen: """))

if uo == 1:
    nuo = "Barriles(es)"
elif uo == 2:
    nuo = "Galón(es)"
elif uo == 3:
    nuo = "Cuarto(s)"
elif uo == 4:
    nuo = "Pinta(s)"
else:
    nuo = "Onza(s)"
co = float(input(f"Cantidad de {nuo}: "))
ud = int(input("Seleccione la unidad de destino: "))

# VALIDACIONES
if uo in range(1,6) and ud  in range(1,6) and co >= 0:
    # PROCESO
    # convertir cantidad a la unidad base onzas
    if uo == 1:
        # Barril
        cd = co * 2688
    elif uo == 2:
        # Galón
        cd = co * 64
    elif uo == 3:
        # Cuarto
        cd = co * 16
    elif uo == 4:
        # Pinta
        cd = co * 8
    else:
        # Onza
        cd = co 

    # convertir desde onzas a otra unidad
    if uo == 1:
        cd = cd / 2688
        nud = "Barril(es)"
    elif uo == 2:
        cd = cd / 64
        nud = "Galón(es)"
    elif uo == 3:
        cd = cd / 16
        nud = "Cuarto(s)"
    elif uo == 4:
        cd = cd / 8
        nud = "Pinta(s)"

else:
    print("Los datos no son válidos")

