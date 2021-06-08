import xml.etree.ElementTree as datosXML

# super clase
class Territorio():
    # Metodo constructor
    def __init__(varClase, valores):
        varClase.campos = ["Codigo", "Nombre"]
        varClase.valores = valores

    def obtenerRegistro(varClase):
        '''Empaquetar datos'''
        return dict(zip(varClase.campos, varClase.valores))

# clase heredada
class Pais(Territorio):
    # Método constructor que altera el heredado
    def __init__(varClase, valores):
        # hacer referencia a todo lo que tiene la clase padre o super clase
        super().__init__(valores)
        varClase.campos.append("CodigoAlfa2")
        varClase.campos.append("CodigoAlfa3")

    # Método estático: que no depende de la variable de clase varClase
    def obtener():
        dXML = datosXML.parse("Paises.xml")
        nodos = dXML.getroot()
        lista = []
        for n in nodos:
            # p es una instancia objeto Pais()
            p = Pais([n.attrib["Codigo"], n.attrib["Nombre"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
            lista.append(p)
        return lista

# --------------PROGRAMA PRINCIPAL------------------
# obtener la lista de paises
paises = Pais.obtener()
# mostrar los datos del pais ubicado en la posición 30 de la lista
r = paises[30].obtenerRegistro()
print("Nombre del Pais:", r["Nombre"], "\nCodigo Alfa:", r["CodigoAlfa2"])
