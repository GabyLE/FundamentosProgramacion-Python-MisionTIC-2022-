class Nodo():
    def __init__(varClase, nombre, apellido, correo, movil):
        varClase.nombre = nombre
        varClase.movil = movil.strip()
        varClase.correo = correo
        varClase.apellido = apellido
        # apuntador
        varClase.siguiente = None

    def actualizar(varClase, nombre = "", apellido = "",movil = "", correo = ""):
        if nombre != "":
            varClase.nombre = nombre
        if movil != "":
            varClase.movil = movil
        if correo != "":
            varClase.correo = correo
        if apellido != "":
            varClase.apellido = apellido

    def mostrar(varClase):
        print("Nombre Completo:", varClase.apellido, varClase.nombre)
        print("Móvil:", varClase.movil)
        print("Correo:", varClase.correo)

    
