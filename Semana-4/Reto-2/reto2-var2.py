from math import sqrt
# import numpy as np

def tamMatriz(l):
    x1 = -0.5 + (sqrt(1 + 8 * l)) / 2
    x2 = -0.5 - (sqrt(1 + 8 * l)) / 2
    if x1 > 0:
        n = x1
    else:
        n = x2
    return n

def solucion(a):
    l = len(a)
    n = int(tamMatriz(l))
    # construye matriz de ceros nxn
    # matriz = np.zeros((n,n))
    matriz = []
    for i in range(n):
        matriz.append([0]*n)
    # llenar la matriz
    k = 0
    for fila in range(n):
        for columna in range(fila + 1):
            matriz[fila][columna] = a[k]
            k += 1
    

    return matriz

lst = [33, 66, 32, 75, 35, 79]
matriz = solucion(lst)
print(matriz)


# l = [8, 60, 72, 35, 26, 75, 15, 12, 33, 54]
# matriz_correcta = np.array([[ 8.,  0.,  0.,  0.], [60., 72.,  0.,  0.], [35., 26., 75.,  0.], [15., 12., 33., 54.]])
# matriz_estudiante = np.array(solucion(l))
# print("LISTA ENTREGADA:\n", l,"\n")
# print("===SALIDA ESPERADA===\nMatriz:\n", matriz_correcta,"\n")
# print("===TU SALIDA===\nMatriz:\n", matriz_estudiante,"\n")

# for i in range(matriz_correcta.shape[0]):
#     for j in range(matriz_correcta.shape[1]):
#         if matriz_correcta[i,j] != matriz_estudiante[i,j]:
#             print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")
#             exit()
# print("Todo se ve correcto, ¡Procede a calificar tu código!")