from Nodo import Nodo

class Lista():
    def __init__(varClase):
        varClase.cabeza = None

    def agregar(varClase, n):
        '''método para agregar un nodo a la lista'''
        if n!= None:
            if varClase.cabeza == None:
                # la lista está vacía
                # El nodo agregado es la cabeza
                varClase.cabeza = n
            else:
                # recorrer la lista hasta el último nodo
                apuntador = varClase.cabeza
                while apuntador.siguiente != None:
                    apuntador = apuntador.siguiente
                # añade siguiente nodo que no apunta a nada, nodo nulo
                apuntador.siguiente = n
                n.siguiente = None

    def desdeArchivo(varClase, nombreArchivo):
        # limpiar lista
        varClase.cabeza = None
        objFile = open(nombreArchivo, "r")
        for linea in objFile:
            datos = linea.split(";")
            if len(datos) >= 4:
                n = Nodo(datos[1], datos[3], datos[2])
                varClase.agregar(n)

    def mostrar(varClase):
        # recorrer la lista hasta el último nodo
        apuntador = varClase.cabeza
        while apuntador != None:
            print(apuntador.nombre, apuntador.correo)
            apuntador = apuntador.siguiente