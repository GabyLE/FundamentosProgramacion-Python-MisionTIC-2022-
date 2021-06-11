class Nodo():
    def __init__(varClase, nombre, movil, correo):
        varClase.nombre = nombre
        varClase.movil = movil
        varClase.correo = correo
        # apuntador
        varClase.siguiente = None

    def actualizar(varClase, nombre, movil, correo):
        varClase.nombre = nombre
        varClase.movil = movil
        varClase.correo = correo