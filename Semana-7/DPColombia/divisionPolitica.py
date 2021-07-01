from tkinter import *
from typing import get_origin
import Util
import csv

nombreArchivo = "ciudades.csv"
campos = ["Depto", "Mpio"]
def obtenerDeptos():
    global nombreArchivo, deptos
    deptos = []
    with open(nombreArchivo, newline='', encoding="utf8") as archivoCSV:
        registros = csv.DictReader(archivoCSV, fieldnames= campos, delimiter= ";" )
        # variable SEMAFORO
        anteriorDepto = ""
        for r in registros:
            if r[campos[0]] != anteriorDepto:
                # Cambiar la variable
                anteriorDepto = r[campos[0]]
                deptos.append(anteriorDepto)            

def obtenerMpios(eventArgs):
    global nombreArchivo, deptos, campos, tMpios
    # verificar que haya depto seleccionado
    if cmbDepto.current():
        depto = deptos[cmbDepto.current()]

        with open(nombreArchivo, newline='', encoding="utf8") as archivoCSV:
            registros = csv.DictReader(archivoCSV, fieldnames= campos, delimiter= ";" )

            # buscar el depto
            r = registros.__next__()
            while r[campos[0]] != depto:
                r = registros.__next__()

            datos = []
            # agregar los mpios del depto
            while r[campos[0]] == depto:
                fila = []
                fila.append(r[campos[1]])
                datos.append(fila)
                r = registros.__next__()

            tMpios = Util.mostrarTabla(frm, ["Municipio"], datos, tMpios)
v = Tk()

deptos = []
obtenerDeptos()
tMpios = None
Util.agregarEtiqueta(v, "Departamento", 0, 0)
cmbDepto = Util.agregarLista(v, deptos, 0, 1)
# EVENTOS
cmbDepto.bind("<<ComboboxSelected>>", obtenerMpios)
frm = Frame(v)

v.mainloop()