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
    # Sobrecarga: que la funcion realice otro algoritmo dependiendo de una condición
    def obtener(codigo = ""):
        dXML = datosXML.parse("Paises.xml")
        nodos = dXML.getroot()

        if codigo == "":
            lista = []
            for n in nodos:
                # p es una instancia objeto Pais()
                p = Pais([n.attrib["Codigo"], n.attrib["Nombre"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
                lista.append(p)
            return lista
        else:
            for n in nodos:
                if n.attrib["Codigo"] == codigo:
                    return Pais([n.attrib["Codigo"], n.attrib["Nombre"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
            return None

class Departamento(Territorio):
    def __init__(varClase, valores):
        super().__init__(valores)

    def obtener(codigo = ""):
        # Abrir el documendo XML
        dXML = datosXML.parse("Departamentos.xml")
        # Obtener lista de nodos
        nodos = dXML.getroot()
        if codigo == "":
            # Obtener la lista de departamentos
            lista = []
            for n in nodos:
                lista.append(Departamento([n.attrib["Codigo"], n.attrib["Nombre"]]))
            return lista
        else:
            # Buscar el departamento que corresponda al codigo
            for n in nodos:
                if n.attrib["Codigo"] == codigo:
                    return Departamento([n.attrib["Codigo"], n.attrib["Nombre"]])
            return None

    def obtenerMunicipio(varClase):
        r = varClase.obtenerRegistro()
        return Municipio.obtener(codigoDepto = r["Codigo"])

class Municipio(Territorio):
    def __init__(varClase, valores, codigoDepartamento):
        super().__init__(valores)
        varClase.departamento = Departamento.obtener(codigoDepartamento)

    def obtener(codigo = "", codigoDepto = ""):
        # Abrir el documendo XML
        dXML = datosXML.parse("Municipios.xml")
        # Obtener lista de nodos
        nodos = dXML.getroot()
        if codigo == "":
            # Obtener la lista de departamentos
            lista = []
            for n in nodos:
                agregar = True
                if codigoDepto != "" and n.attrib["CodigoDepartamento"] != codigoDepto:
                    agregar = False
                if agregar:
                    lista.append(Municipio([n.attrib["CodigoMunicipio"], n.attrib["Nombre"]], \
                        n.attrib["CodigoDepartamento"]))
            return lista
        else:
            # Buscar el departamento que corresponda al codigo
            for n in nodos:
                if n.attrib["CodigoMunicipio"] == codigo:
                    return Municipio([n.attrib["CodigoMunicipio"], n.attrib["Nombre"]], \
                    n.attrib["CodigoDepartamento"])
            return None


# --------------PROGRAMA PRINCIPAL------------------
# obtener la lista de paises
'''paises = Pais.obtener()
# mostrar los datos del pais ubicado en la posición 30 de la lista
r = paises[30].obtenerRegistro()
print("Nombre del Pais:", r["Nombre"], "\nCodigo Alfa:", r["CodigoAlfa2"])
'''
# obtener un país por su código
'''pais = Pais.obtener("031")
if pais != None:
    print(pais.obtenerRegistro())
else:
    print("No se encontró país con ese código")'''

# obtener lista de departamentos
'''deptos = Departamento.obtener()
# mostrar los datos de los Departamentos consultados
for d in deptos:
    r = d.obtenerRegistro()
    print("Nombre del Departamento:", r["Nombre"], "Codigo:", r["Codigo"])'''

# obtener municipio y el departamento al que pertenece
'''mpios = Municipio.obtener("05107")
r = mpios.obtenerRegistro()
print(r["Nombre"], "ubicado en", mpios.departamento.obtenerRegistro()["Nombre"])'''

# obtener un departamento por su codigo
codigo = input("Código del depto a consultar: ")
depto = Departamento.obtener(codigo)
if depto != None:
    rd = depto.obtenerRegistro()
    print("Los municipios del depto", rd["Nombre"], "son:")
    # obtener la lista de municipios para un departamento
    # mpios = Municipio.obtener(codigoDepto=rd["Codigo"])
    mpios = depto.obtenerMunicipio()
    for m in mpios:
        print(m.obtenerRegistro()["Nombre"])
else:
    print("No existe departamento con ese codigo")