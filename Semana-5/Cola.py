class Cola:
    #Metodo constructor
    def __init__(varClase):
        varClase.datos=[]

    def encolar(varClase, dato):
        varClase.datos.append(dato)

    def desencolar(varClase):
        if not varClase.vacia():
            # asigna valor a una variable
            dato = varClase.datos[0]
            # elimina el valor del arreglo
            del varClase.datos[0]
            # retorna la variable con el valor asignado
            return dato
        else:
            return None
    
    def valorTope(varClase):
        if varClase.datos:
            return varClase.datos[-1] #retorna el ultimo elemento
        else:
            return None

    def vacia(varClase):
        return len(varClase.datos)==0
        