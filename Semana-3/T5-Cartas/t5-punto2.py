from tkinter import *
import random

v = Tk()
v.title("Apuntado")
v.minsize(width= 300, height= 200)
v.configure(background= 'green')

# Funciones
def mostrarCarta(fila, columna, archivo):
    # Obtener la imagen desde el archivo
    imgCarta = PhotoImage(file= archivo)

    # Mostrar la imagen
    lblCarta = Label(v)
    lblCarta.grid(row= fila, column= columna)
    lblCarta.configure(image = imgCarta)
    lblCarta.image = imgCarta

def repartir():

    global cartas
    cartas = []
    # Inicializa variable de control fila y columna para mostrar las cartas
    f = 1
    c = 0
    for i in range(0, 10):
        # Generar un número aleatorio entre 1 y 52
        nc = random.randrange(52) + 1

        # Agregar indice de la carta al vector
        cartas.append(nc)

        # Mostrar la carta
        mostrarCarta(f, c, "Carta" + str(nc) + ".gif")
        
        c = c + 1

def ocultarLabel(lbl):
    lbl.grid_forget()

def obtenerIndiceNombre(numeroCarta):
    indice = numeroCarta % 13
    if indice > 0:
        # posicion en el arreglo cartas[]
        indice = indice - 1
    else:
        # si es la carta 13 la posicion en el arreglo es 12
        indice = 12
    return indice

def verificar():
    contadores = [0] *13

    for i in range(len(cartas)):
        # obtiene la posicion en la que se debe aumentar el contador
        p = obtenerIndiceNombre(cartas[i])
        contadores[p] = contadores[p] + 1

    # Mostrar los grupos hallados
    grupos = ["Ninguno", "Non", "Par", "Terna", "Cuarta", "Quinta", "Sexta", "Séptima"]
    nombres = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    f = 1 # Fila para mostrar la verificación
    for i in range(13):
        if contadores[i] >= 2:
            f = f + 1
            Label(text=grupos[contadores[i]] + " de " + nombres[i], font= "Consolas 10", width=10).grid(row= f)

    

# Buttons
Button(v, text= "Repartir", command= repartir, font= "Consolas 10").grid(row= 0, column=0)
Button(v, text= "Verificar", command= verificar, font= "Consolas 10").grid(row=0, column= 1)
v.mainloop()