
def esLleno(V,n):
    if V[0] == n:
        return True
    return False

def imprimeVector(V, mensaje = "Vector sin nombre"):
    print("\n", mensaje, end = "")
    m = V[0] + 1
    for i in range(1, m):
        print(V[i], end = ",")

def agregarDato(d, V, n):
    if esLleno(V,n):
        return
    V[0] = V[0] + 1
    V[V[0]] = d

acuMpio = [4,1,2,3,4]
imprimeVector(acuMpio)
agregarDato(98, acuMpio, 5)
imprimeVector(acuMpio)