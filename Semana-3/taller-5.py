# ENTRADA
bin = input("Ingrese número decimal: ")

# PROCESO
# variables
grupos =[]
decimales = []
hex = ""

# constantes
hexadecimal = {10:"A", 11:"B",12:"C", 13:"D", 14:"E", 15:"F"}

# Calculo cifras sobrantes al agrupar el número en grupos de 4
sobra = len(bin) % 4
# añade el valor agrupado sobrante a la lista grupos
grupos.append(bin[:sobra])

# añade los grupos de cuatro digitos a la lista grupos
lim_s= sobra + 4
for i in range(sobra,len(bin),4):
    grupos.append(bin[i:lim_s])
    lim_s += 4

# Calculo de binario a decimal con los valores agrupados
for str in grupos:
    pow = 0
    dec = 0
    for i in range(len(str)-1, -1, -1):
        num = int(str[i])
        dec = dec + (2**pow)*num
        pow += 1
    decimales.append(dec)

# Decimal a hexadecimal
for decimal in decimales:
    
    if decimal < 10:
        hex += "{}".format(decimal)
    else:
        hex += hexadecimal[decimal]

# SALIDA
print()
print("Hexadecimal: " + hex)
