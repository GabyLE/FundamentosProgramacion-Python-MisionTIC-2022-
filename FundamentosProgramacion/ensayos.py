import random

cartas_P1 = []
cartas_P2 = []

for nc in range(10):
    cartas_P1.append(random.randint(1,53))
    cartas_P2.append(random.randint(1,53))

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


cartaMayor1 = cartaMayorRepartida(cartas_P1)
print(cartas_P1)
print(cartaMayor1)
# aces = [1 , 14, 27, 40]
# ace = []
# no_ace = []


# for i in range(len(cartas_P1)):
#     carta1 = cartas_P1[i]
#     if carta1 in aces:
#         ace.append(carta1)
#     else:
#         no_ace.append(carta1)

# if len(ace) == 0:
#     cartaMayor1 = mayor(no_ace)
# else:
#     cartaMayor1 = mayor(ace)

# print(cartas_P1)
# print(cartaMayor1)






