from tkinter import *
import csv
import Util

nombreArchivo = "ciudades.csv"
campos = ["Departamento", "Municipio"]
#Objeto tabla para despliegue de los datos
tMunicipios = None

def obtenerDeptos():
    global nombreArchivo, campos
    deptos = []
    with open(nombreArchivo, newline='', encoding="utf8") as archivoCSV:
        registros = csv.DictReader(archivoCSV, fieldnames=campos, delimiter=";")
        anterior = ""
        for r in registros:
            if r[campos[0]] != anterior:
                anterior = r[campos[0]]
                deptos.append(anterior)
    return deptos

def obtenerMpios(e):
    global tMunicipios, deptos, campos
    if cmbDepto.current()>=0:
        depto = deptos[cmbDepto.current()]
        with open(nombreArchivo, newline='', encoding="utf8") as archivoCSV:
            registros = csv.DictReader(archivoCSV, fieldnames=campos, delimiter=";")
            datos=[]
            #Buscar el depto
            f=0
            r=registros.__next__()
            while r[campos[0]] != depto:
                r=registros.__next__()
                f += 1
            while r[campos[0]] == depto:
                fila = []
                fila.append(r[campos[1]])
                datos.append(fila)
                r=registros.__next__()
                f += 1

        tMunicipios = Util.mostrarTabla(frm, \
                                    ["Municipio"], \
                                    datos, \
                                    tMunicipios)

v = Tk()

Util.agregarEtiqueta(v, "Departamento:", 0, 0)
deptos=obtenerDeptos()
cmbDepto=Util.agregarLista(v, deptos, 0, 1)

cmbDepto.bind("<<ComboboxSelected>>", obtenerMpios)

frm = Frame(v)
frm.grid(row=1, column=0, columnspan=2)

v.mainloop()