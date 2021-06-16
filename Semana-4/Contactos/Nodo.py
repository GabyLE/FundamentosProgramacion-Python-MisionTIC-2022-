class Nodo():
    def __init__(varClase, nombre, movil, correo, cedula):
        varClase.nombre = nombre
        varClase.movil = movil.strip()
        varClase.correo = correo
        varClase.cedula = cedula
        # apuntador
        varClase.siguiente = None

    def actualizar(varClase, nombre = "", movil = "", correo = ""):
        if nombre != "":
            varClase.nombre = nombre
        if movil != "":
            varClase.movil = movil
        if correo != "":
            varClase.correo = correo

    def mostrar(varClase):
        print("Nombre:", varClase.nombre)
        print("Móvil:", varClase.movil)
        print("Correo:", varClase.correo)