def obtenerDatos(nombreArchivo):
    fechas = []
    precios = []
    bajos = []
    altos = []

    with open(nombreArchivo, 'r') as inputFile:
        lines = inputFile.readlines()
        for line in lines[1:]:
            lst = line.strip().split(",")
            fechas.append(lst[0])
            precios.append(float(lst[4]))
            bajos.append(float(lst[3]))
            altos.append(float(lst[2]))

    return fechas, precios, bajos, altos

def analisisPrecio(precio):
    if precio < 200:
        return "MUY BAJO"
    elif precio >= 200 and precio < 300:
        return "BAJO"
    elif precio >= 300 and precio < 500:
        return "MEDIO"
    elif precio >= 500 and precio < 600:
        return "ALTO"
    elif precio >= 600:
        return "MUY ALTO"

def archivoSalida(fechas, precios):
    with open("analisis_archivo.csv", "w") as outFile:
        outFile.write("Fecha\tConcepto\n")
        for i in range(len(fechas)):
            concepto = analisisPrecio(precios[i])
            linea = "{}\t{}".format(fechas[i], concepto)
            outFile.write(linea)
            outFile.write("\n")

def indexHighest(lista):
    index = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[index]:
            index = i
    return index

def indexLowest(lista):
    index = 0
    for i in range(1, len(lista)):
        if lista[i] < lista[index]:
            index = i
    return index

def solucion():

    fechas, precios, bajos, altos = obtenerDatos("TSLA.csv")
    archivoSalida(fechas, precios)

    i_highest = indexHighest(altos)
    date_highest = fechas[i_highest]
    highest_value = altos[i_highest]

    i_lowest = indexLowest(bajos)
    date_lowest = fechas[i_lowest]
    lowest_value = bajos[i_lowest]
    # precios.sort()
    # return precios
    return date_lowest, lowest_value, date_highest, highest_value

#a, b, c, d = solucion()
a, b, c, d= solucion()

print(a)
print(b)
print(c)
print(d)