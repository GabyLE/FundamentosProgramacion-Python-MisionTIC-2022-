import json

class Contacto():

    #posición del registro a editar
    indice = -1
    #lista de contactos
    contactos = []

    #Método constructor
    def __init__(varClase, id, \
                         nombre, \
                         correo, \
                         movil):
        varClase.id = id
        varClase.nombre = nombre
        varClase.correo = correo
        varClase.movil = movil

    def actualizar(varClase, id, nombre, correo, movil):
        varClase.id = id
        varClase.nombre = nombre
        varClase.correo = correo
        varClase.movil = movil 

    #Obtener la lista de Contactos o un contacto en particular desde un archivo
    @staticmethod
    def obtener(nombreArchivo, id=""):
        with open(nombreArchivo, "r") as archivoJSON:
            datos = json.load(archivoJSON)
            # datos es un diccionario
            for d in datos:
                c = Contacto(d["id"], d["nombre"], d["correo"], d["movil"])
                Contacto.contactos.append(c)

    #Convertir los registros en una matriz de textos
    @staticmethod
    def pasarMatriz():
        matriz = []
        for jesus in Contacto.contactos:
            linea = []
            linea.append(jesus.id)
            linea.append(jesus.nombre)
            linea.append(jesus.correo)
            linea.append(jesus.movil)
            matriz.append(linea)
        return matriz

    #Método para Agregar un Contacto
    @staticmethod
    def agregar(id, nombre, correo, movil):
        c = Contacto(id, nombre, correo, movil)
        Contacto.contactos.append(c)

    #Método para Modificar un Contacto
    @staticmethod
    def modificar(id, nombre, correo, movil):
        if Contacto.indice in range(0, len(Contacto.contactos)):
            Contacto.contactos[Contacto.indice].actualizar(id, nombre, correo, movil)

    #Método para Eliminar un Contacto
    @staticmethod
    def eliminar():
        if Contacto.indice in range(0, len(Contacto.contactos)):
            del Contacto.contactos[Contacto.indice]

    #Método para Ordenar la lista de Contactos
    @staticmethod
    def ordenar():
        for i in range(len(Contacto.contactos)-1):
            for j in range(i+1, len(Contacto.contactos)):
                if Contacto.contactos[i].nombre > Contacto.contactos[j].nombre:
                    #intercambio de contactos
                    t = Contacto.contactos[i]
                    Contacto.contactos[i] = Contacto.contactos[j]
                    Contacto.contactos[j] = t


    #Método para Guardar los Contactos en un archivo
    @staticmethod
    def guardar(nombreArchivo):
        #abrir el archivo para escritura
        with open(nombreArchivo, "w") as archivoJSON:
            #convertir a texto JSON y guardarlo
            json.dump([c.__dict__ for c in Contacto.contactos], archivoJSON)
        

    
