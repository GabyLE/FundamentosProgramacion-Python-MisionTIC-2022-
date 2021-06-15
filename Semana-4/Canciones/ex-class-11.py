# librería para operar con cuadros de diálogo
from tkinter import filedialog
from NotaMusical import NotaMusical

# abre ventana explorador para elegir archivo
nombreArchivo = filedialog.askopenfilename()

if len(nombreArchivo) > 0:
    # abrir el archivo
    with open(nombreArchivo, 'r') as fCancion:
        # recorrer las lineas del archivo
        for linea in fCancion:
            datos = linea.split(",")
            nm = NotaMusical(datos[0], datos[1])
            print(nm.nota, nm.escala, nm.tiempo)
            nm.reproducir()