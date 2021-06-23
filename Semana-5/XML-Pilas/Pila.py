class Pila:
    #Metodo constructor
    def __init__(varClase):
        varClase.datos=[]

    def apilar(varClase, dato):
        varClase.datos.append(dato)

    def desapilar(varClase):
        if not varClase.vacia:
            dato=varClase.datos.pop()
            return dato
        else:
            return None
    
    def valorTope(varClase):
        if varClase.datos:
            return varClase.datos[-1] #retorna el ultimo elemento
        else:
            return None

    def vacia(varClase):
        if len(varClase.datos)==0:
            return True
        else:
            return False
