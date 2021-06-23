from Cola import Cola

class Punto():

    def __init__(varClase, x, y):
        varClase.x = x
        varClase.y = y

    def esIgual(varClase, punto):
        return varClase.x == punto.x and varClase.y == punto.y

class Laberinto():

    def __init__(varClase, laberinto, xEntrada, yEntrada, xSalida, ySalida):
        varClase.entrada = Punto(xEntrada, yEntrada)
        varClase.salida = Punto(xSalida, ySalida)
        varClase.laberinto = laberinto

        # Matriz
        varClase.filas = len(laberinto)
        varClase.columnas = len(laberinto[0])

    def mostrar(varClase):
        
        for fila in range(0, varClase.filas):
            linea=""
            for columna in range(0, varClase.columnas):
                if varClase.laberinto[fila][columna] == 1:
                    linea += "|"
                elif varClase.laberinto[fila][columna] == 0:
                    linea += " "
                elif varClase.laberinto[fila][columna] == -1:
                    linea += "*"
                else:
                    linea += str(varClase.laberinto[fila][columna])
            print(linea)

    def asignar(varClase, punto, valor):
        varClase.laberinto[punto.x][punto.y] = valor

    def estaLibre(varClase, punto):
        return varClase.laberinto[punto.x][punto.y] == 0

    def resolver(varClase):
        cola = Cola()
        varClase.asignar(varClase.salida, 0) # marcar el punto de entrada
        punto = varClase.entrada # donde estoy ubicado
        cola.encolar(punto)
        varClase.asignar(punto, -1) # Asignarlo a -1 para evitar retroceder y repetir la búsqueda
        # la cola no puede estar vacia
        while not cola.vacia(): 
            punto = cola.desencolar()
            if punto.esIgual(varClase.salida): # Salida encontrada, ruta de salida
                return True # Devuelve true cuando se encuentra una ruta
            # 4 -> arriba, abajo, deracha, izquierda
            for di in range(0, 4): # escanea cíclicamente cada posición
                heAvanzado = False
                if di == 0 and punto.x>0:
                    # avanzar a la IZQUIERDA
                    heAvanzado = True
                    puntoInteres=Punto(punto.x-1, punto.y)
                elif di ==1 and punto.y < varClase.columnas-1:
                    # avanzar hacia ABAJO
                    heAvanzado = True
                    puntoInteres=Punto(punto.x, punto.y+1)
                elif di ==2 and punto.x < varClase.filas-1:
                    # avanza a la DERECHA
                    heAvanzado = True
                    puntoInteres=Punto(punto.x+1, punto.y)
                elif di == 3 and punto.y > 0:
                    # avanza hacia ARRIBA
                    heAvanzado = True
                    puntoInteres = Punto(punto.x, punto.y - 1)
                
                if heAvanzado:
                    if varClase.estaLibre(puntoInteres):
                        cola.encolar(puntoInteres)
                        varClase.asignar(puntoInteres, -1)

        return False

