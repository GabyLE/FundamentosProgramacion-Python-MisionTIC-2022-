print("TIENDA ESCOLAR")

capInicial = float(input("¿Cuánto capital tiene? "))
print("---------------------------------------------------------------")
nomProd = []
cantProd = []
valCompra = []
precioVenta = []
gananciaProd = []

contador = 0

while True:
    
    nomProd.append(input("Nombre del producto: "))
    if len(nomProd[-1]) < 1:
        break
    cantProd.append(int(input("Cantidad comprada del producto: ")))
    valCompra.append(int(input("Valor de la compra: ")))
    print("---------------------------------------------------------------")
    contador += 1

for i in range(contador):
    valorUnidad = valCompra[i]/cantProd[i]

    print("El valor por unidad de {} es ${}".format(nomProd[i],valorUnidad))
    precioVenta.append(int(input("¿A qué precio lo desea vender? ")))
    print("---------------------------------------------------------------")

capActual = capInicial - sum(valCompra)

print("El capital actual es de ${}".format(capActual))
print("---------------------------------------------------------------")

for i in range(contador):
    unidVendida = int(input(f"¿Cuántas unidades vendió de {nomProd[i]}? "))
    gananciaProd.append(unidVendida*precioVenta[i])

    unidSobra = cantProd[i] - unidVendida

    print("Valor ventas de {}: ${} ".format(nomProd[i],gananciaProd[i]))
    print("Unidades sobrantes de {}: {}".format(nomProd[i],unidSobra))
    print("---------------------------------------------------------------")

capVendido = sum(gananciaProd)

if capVendido > sum(valCompra):
    print("¡FELICIDADES! Superaste el valor de la inversión")
else:
    print(":( No superaste el valor de la inversión")