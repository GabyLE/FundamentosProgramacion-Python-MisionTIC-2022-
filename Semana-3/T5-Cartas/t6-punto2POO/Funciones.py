from Carta import Carta

def mayor(lista):
    cm = lista[0]
    for c in lista[1:]:
        if c.indice > cm.indice:
            cm = c
    return cm

def cartaMayorRepartida(cartas):
    aces = [1, 14, 27, 40]
    ace = []
    no_ace = []
    cartaMayor = None
    for carta in cartas:
        if carta.indice in aces:
            ace.append(carta)
        else:
            no_ace.append(carta)
    
    if len(ace) != 0:
        cartaMayor = mayor(ace)
    else:
        cartaMayor = mayor(no_ace)
    
    return cartaMayor