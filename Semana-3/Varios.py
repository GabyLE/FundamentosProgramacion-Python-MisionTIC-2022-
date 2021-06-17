from tkinter import *

def mostrar(lstDatos, datos):
    '''Mostrar los datos en la ListBox'''
    # limpiar lista
    lstDatos.delete(0, END)
    for i in range(0, len(datos)):
        # agregar datos a la lista
        lstDatos.insert(END, str(datos[i]))
        
def mostrarCajaTexto(cajaTxt, valor):
    '''Mostrar el resultado en la caja de texto'''
    cajaTxt.configure(state= NORMAL)
    cajaTxt.delete(0, END)
    cajaTxt.insert(0, str(valor))
    cajaTxt.configure(state= DISABLED)

def sumatoria(datos):
    suma = 0
    for i in range(0, len(datos)):
        suma += datos[i]
    return suma

def promedio(datos):
    p = 0
    if len(datos) > 0:
        p = sumatoria(datos) / len(datos)
    return p

def desviacion(datos):
    d = 0
    if len(datos) > 1:
        p = promedio(datos)
        s = 0
        for i in range(0, len(datos)):
            s += abs(datos[i] - p)
        d = s / (len(datos) - 1)
    return d

def moda(datos):
    '''Retorna la moda de los datos'''
    frec_lst = {}

    for i in datos:
        frec_lst[i] = frec_lst.get(i, 0) + 1

    mayor = 0
    for key, value in frec_lst.items():
        if value > mayor:
            mayor = value
            moda = key
    return moda

def mediana(datos):
    '''Retorna la mediana de los datos'''
    n = len(datos)
    new_lst = datos[:]
    new_lst.sort()
    if n % 2 != 0:
        mediana = new_lst[n//2]
    else:
        pos_2 = n//2 
        pos_1 = pos_2 - 1
        mediana = (new_lst[pos_1] + new_lst[pos_2])/2
    return mediana