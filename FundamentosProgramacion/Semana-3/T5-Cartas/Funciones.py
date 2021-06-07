from tkinter import *

def mostrarCarta(fila, columna, archivo, frame):
    # Obtener la imagen desde el archivo
    imgCarta = PhotoImage(file= archivo)

    # Mostrar la imagen
    lblCarta = Label(frame)
    lblCarta.grid(row= fila, column= columna)
    lblCarta.configure(image = imgCarta)
    lblCarta.image = imgCarta
    
def mayor(lista):
    mayor = 0
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def cartaMayorRepartida(cartas):
    aces = [1, 14, 27, 40]
    ace = []
    no_ace = []
    for carta in cartas:
        if carta in aces:
            ace.append(carta)
        else:
            no_ace.append(carta)
    
    if len(ace) != 0:
        cartaMayor = mayor(ace)
    else:
        cartaMayor = mayor(no_ace)

    return cartaMayor

