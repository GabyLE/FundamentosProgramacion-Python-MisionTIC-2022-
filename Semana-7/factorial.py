# subprograma recursivo para el calculo del factorial

def obtenerFactorial(n):
    if n <= 1:
        return 1
    else:
        return n * obtenerFactorial(n - 1)

print("Programa para calcular el factorial de un numero")
numero = int(input("Número a calcular: "))
print("El factorial es", obtenerFactorial(numero))