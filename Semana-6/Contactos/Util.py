#Importar la libreria para GUI
from tkinter import *
from tkinter.ttk import *

#Importar libreria para Expresiones Regulares
import re


#Importar fuentes de texto
from tkinter import font

def mostrar(txt, valor, soloLectura=True):
    if soloLectura:
        #desbloquear la caja de texto
        txt.configure(state=NORMAL)
    #limpiar la caja de texto
    txt.delete(0, END)
    #Asignar el valor
    txt.insert(0, str(valor))
    if soloLectura:
        #bloquear la caja de texto de nuevo
        txt.configure(state=DISABLED)

def agregarImagen(ventana, archivo, fila, columna, expandir=1):
    #cargar la imagen
    img=PhotoImage(file = archivo)
    #Mostrar imagen en una etiqueta
    lbl=Label(ventana)
    lbl.config(image=img)
    lbl.image=img
    lbl.grid(row=fila, column=columna, columnspan=expandir)
    return lbl

def agregarEtiqueta(ventana, texto, fila, columna, expandir=1):
    Label(ventana, text=texto).grid(row=fila, column=columna, columnspan=expandir)


def agregarTexto(ventana, ancho, fila, columna, expandir=1, habilitado=True):
    txt=Entry(ventana, width=ancho)
    txt.grid(row=fila, column=columna, columnspan=expandir)
    if habilitado:
        txt.configure(state=NORMAL)
    else:
        txt.configure(state=DISABLED)
    return txt

def agregarLista(ventana, opciones, fila, columna, expandir=1):
    cmb=Combobox(ventana)
    cmb.grid(row=fila, column=columna, columnspan=expandir)
    cmb["values"]=opciones
    return cmb

def esReal(texto):
    return True if re.match("^[-]?[0-9]+[.]?[0-9]*$", texto) else False

def esEntero(texto):
    return True if re.match("^[-]?[0-9]+$", texto) else False

def agregarBarra(ventana, imagenes):
    frmBarra = Frame(ventana)
    frmBarra.pack(side=TOP, fill=X)
    botones = []
    for imagen in imagenes:
        #cargar la imagen
        img=PhotoImage(file = imagen)

        btn = Button(frmBarra, image=img)
        btn.image = img
        btn.pack(side=LEFT, padx=2, pady=2)
        botones.append(btn)

    return botones

def mostrarTabla(ventana, encabezados, datos, tabla):
    tabla = VistaTabla(ventana, encabezados, datos, tabla)
    return tabla.obtenerTabla()

class VistaTabla(object):
    #Utiliza ttk.TreeView como una Rejilla de datos
    #Metodo constructor
    def __init__(varClase, ventana, encabezados, datos, arbol=None):
        varClase.arbol = arbol #objeto para el despliegue de la tabla
        varClase.crear(ventana, encabezados, datos)
        varClase.configurar(encabezados, datos)

    #Metodo que crea los objetos para despliegue
    def crear(varClase, ventana, encabezados, datos):
        #crear el contenedor
        frm = Frame(ventana)
        frm.pack(fill=BOTH, expand=True)

        #Crear objeto Treeview con 2 barras de desplazamiento
        if varClase.arbol == None:
            varClase.arbol = Treeview(columns=encabezados, show="headings")
            vsb = Scrollbar(orient="vertical", command=varClase.arbol.yview)
            hsb = Scrollbar(orient="horizontal", command=varClase.arbol.xview)

            varClase.arbol.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            varClase.arbol.grid(column=0, row=0, sticky=N+S+E+W, in_=frm)

            vsb.grid(column=1, row=0, sticky=N+S, in_=frm)
            hsb.grid(column=0, row=1, sticky=E+W, in_=frm)

    #Metodo que define la estructura de los datos a desplegar
    def configurar(varClase, encabezados, datosTabla):
        #Recorrer los encabezados
        for encabezado in encabezados:
            #Asignar el encabezado y comando de ordenamiento
            varClase.arbol.heading(encabezado, text=encabezado.title(),
                command=lambda c=encabezado: varClase.ordenar(varClase.arbol, c, 0))

            #Ajusta el ancho de la columna al texto del encabezado
            varClase.arbol.column(encabezado, width=font.Font().measure(encabezado.title()))

        #limpiar el arbol
        varClase.arbol.delete(*varClase.arbol.get_children())
        #Recorrer los datos
        for fila in datosTabla:
            varClase.arbol.insert('', 'end', values=fila)
            #Ajusta el ancho de la columna si es necesario
            for i, dato in enumerate(fila):
                anchoColumna = font.Font().measure(dato)
                if varClase.arbol.column(encabezados[i],width=None)<anchoColumna:
                    varClase.arbol.column(encabezados[i], width=anchoColumna)

    #Metodo que retorna el objeto TreeView
    def obtenerTabla(varClase):
        return varClase.arbol
                    
    #Metodo que permita ordenar los datos cuando se hace clic en el encabezado
    def ordenar(varClase, arbol, encabezado, descendente):
        #Obtener los valores a ordenar
        datos = [(arbol.set(nodo, encabezado), nodo) \
            for nodo in arbol.get_children('')]

        #Ordenar los datos
        datos.sort(reverse=descendente)
        for i, fila in enumerate(datos):
            arbol.move(fila[1], '', i)
        #Intercambiar el encabezado para que ordene en sentido contrario
        arbol.heading(encabezado, command=lambda encabezado=encabezado: varClase.ordenar(arbol, encabezado, \
            int(not descendente)))

