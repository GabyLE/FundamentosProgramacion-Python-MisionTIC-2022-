from Pila import Pila

frase = input("Frase a validar: ")
frase = frase.replace(" ", "").replace("á", "a").lower()

mitad = int(len(frase)/2)

# Crear la pila para guardar los caracteres hasta la mitad
p = Pila()

for i in range(0, mitad):
    p.apilar(frase[i])
i = mitad
if len(frase) % 2 != 0:
    i += 1

esPalindromo = True
while not p.vacia and esPalindromo:
    caracter = p.desapilar()
    if caracter != frase[i]:
        esPalindromo = False
    i += 1

if esPalindromo:
    print("La frase es un palíndromo")
else:
    print("La frase No es palíndromo")