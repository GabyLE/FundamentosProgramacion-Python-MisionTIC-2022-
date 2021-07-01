import csv

class Contacto:

    #posición del registro a editar
    indice = -1
    #lista de contactos
    contactos = []
    #lista de campos
    campos = ["ID", \
               "Nombre", \
               "Correo", \
               "Móvil"
               ]

    #Obtener la lista de Contactos o un contacto en particular desde un archivo
    @staticmethod
    def obtener(nombreArchivo):
        with open(nombreArchivo, newline='') as archivoCSV:
            # registros es un vector de diccionarios
            registros = csv.DictReader(archivoCSV, fieldnames=Contacto.campos, delimiter=";")
            for r in registros:
                Contacto.contactos.append(r)

    #Convertir los registros en una matriz de textos
    @staticmethod
    def pasarMatriz():
        datos = []
        for cn in Contacto.contactos:
            fila = []
            for cm in Contacto.campos:
                fila.append(cn[cm])
            datos.append(fila)
        return datos

    #Método para Agregar un Contacto
    @staticmethod
    def agregar(id, nombre, correo, movil):
        c = dict(zip(Contacto.campos, [id, nombre, correo, movil]))
        Contacto.contactos.append(c)

    #Método para Modificar un Contacto
    @staticmethod
    def modificar(id, nombre, correo, movil):
        if Contacto.indice in range(0, len(Contacto.contactos)):
            Contacto.contactos[Contacto.indice]=dict(zip(Contacto.campos, [id, nombre, correo, movil]))

    #Método para Eliminar un Contacto
    @staticmethod
    def eliminar():
        if Contacto.indice in range(0, len(Contacto.contactos)):
            del Contacto.contactos[Contacto.indice]

    #Método para obtener el actual Contacto
    @staticmethod
    def obtenerActual():
        if Contacto.indice in range(0, len(Contacto.contactos)):
            return Contacto.contactos[Contacto.indice]
        else:
            return None

    #Método para Ordenar la lista de Contactos
    @staticmethod
    def ordenar():
        for i in range(len(Contacto.contactos)-1):
            for j in range(i+1, len(Contacto.contactos)):
                if Contacto.contactos[i][Contacto.campos[1]] >= Contacto.contactos[j][Contacto.campos[1]]:
                    t = Contacto.contactos[i]
                    Contacto.contactos[i] = Contacto.contactos[j]
                    Contacto.contactos[j] = t
                    

    #Método para Guardar los Contactos en un archivo
    @staticmethod
    def guardar(nombreArchivo):
        with open(nombreArchivo, "w", newline='') as archivoCSV:
            registros = csv.DictWriter(archivoCSV, fieldnames=Contacto.campos, delimiter=";")
            for c in Contacto.contactos:
                registros.writerow(c)

        

    
