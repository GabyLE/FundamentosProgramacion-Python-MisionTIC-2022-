print("Programa para calcular suma de múltiplos de un número")
#entrada
m = int(input("Múltiplo de: "))
n = int(input("Límite de la suma: "))

if m > 0 and n >= m:
    # proceso
    suma = 0
    #for i in range(1,n+1):
        #if i % m == 0:
            #suma += i
    for i in range(m, n+1, m):
        suma += i
else:
    print("Datos inválidos")

print("La sumatoria es:", suma)