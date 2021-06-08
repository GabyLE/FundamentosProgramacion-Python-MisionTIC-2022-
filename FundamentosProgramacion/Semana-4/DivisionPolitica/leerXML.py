# librería para operar datos xml
import xml.etree.ElementTree as datosXML

# abrir el documento xml
dXML = datosXML.parse("Paises.xml")
# obtener la lista de nodos
nodos = dXML.getroot()

# mostrar la lista de nodos de manera OBJETUAL
for n in nodos:
    print(n.attrib["Nombre"])
