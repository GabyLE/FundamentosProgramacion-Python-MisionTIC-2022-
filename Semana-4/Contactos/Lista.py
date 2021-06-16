from Nodo import Nodo

class Lista():
    def __init__(varClase):
        varClase.cabeza = None

    def agregar(varClase, n):
        '''método para agregar un nodo a la lista'''
        if n!= None:
            if varClase.cabeza == None:
                # la lista está vacía
                # El nodo agregado es la cabeza
                varClase.cabeza = n
            else:
                # recorrer la lista hasta el último nodo
                apuntador = varClase.cabeza
                while apuntador.siguiente != None:
                    apuntador = apuntador.siguiente
                # añade siguiente nodo que no apunta a nada, nodo nulo
                apuntador.siguiente = n
                n.siguiente = None

    def desdeArchivo(varClase, nombreArchivo):
        # limpiar lista
        varClase.cabeza = None
        with open(nombreArchivo, "r") as objFile:
            for linea in objFile:
                datos = linea.split(";")
                if len(datos) >= 4:
                    n = Nodo(datos[1], datos[3], datos[2], datos[0])
                    varClase.agregar(n)

    def listar(varClase, prefijo):
        # recorrer la lista hasta el último nodo
        apuntador = varClase.cabeza
        while apuntador != None:
            if prefijo == "" or apuntador.nombre.lower().startswith(prefijo.lower()):
                print(apuntador.nombre, apuntador.correo, apuntador.movil)
            apuntador = apuntador.siguiente

    def obtenerPredecesor(varClase, n):
        predecesor = None
        # El nodo no sea el nulo - la lista no esté vacía - el nodo que se busca no sea el nodo cabeza
        if n != None and varClase.cabeza != None and varClase.cabeza!=n:
            predecesor = varClase.cabeza
            while predecesor != None and predecesor.siguiente!=n:
                predecesor = predecesor.siguiente
        return predecesor
    
    def intercambiar(varClase, n1, n2):
        # ninguno de los dos nodos sea nulo - que no sean el mismo nodo
        if n1 != None and n2 != None and n1 != n2:
            # variable booleana para cambiar siguientes para al final realizar el cambio de siguientes
            cambiarSiguientes = False
            # obtención predecesores
            predecesor1 = varClase.obtenerPredecesor(n1)
            predecesor2 = varClase.obtenerPredecesor(n2)
            # si nodo 1 no es cabeza
            if predecesor1 != None:
                # si nodo1 y nodo2 no son contiguos
                if predecesor1!=n2:
                    # el predecesor de n1 apuntará a n2
                    predecesor1.siguiente = n2
                    cambiarSiguientes = True
                else:
                    # intercambia nodos contiguos
                    n2.siguiente = n1.siguiente
                    n1.siguiente = n2
                    # predecesor del segundo nodo es diferente de nulo (no es cabeza)
                    if predecesor2 != None:
                        predecesor2.siguiente = n1
            else:
                # el primer nodo es el cabeza
                varClase.cabeza = n2
                cambiarSiguientes = True
            # si nodo 2 no es cabeza
            if predecesor2 != None:
                # no son nodos contiguos
                if predecesor2!=n1:
                    predecesor2.siguiente = n1
                    cambiarSiguientes = True
                else:
                    # son nodos contiguos
                    cambiarSiguientes = False
                    n1.siguiente = n2.siguiente
                    n2.siguiente = n1
                    # nodo 1 no es cabeza
                    if predecesor1 != None:
                        predecesor1.siguiente = n2
            else:
                # el nodo dos es cabeza
                varClase.cabeza = n1
                cambiarSiguientes = True

            # intercambia los apuntadores
            if cambiarSiguientes:
                siguiente1 = n1.siguiente
                n1.siguiente = n2.siguiente
                n2.siguiente = siguiente1

    def ordenar(varClase):
        '''Ordenar acendentemente la lista por el nombre alfabéticamente'''
        # hay datos para ordenar?
        if varClase.cabeza != None:
            # inicia en el nodo cabeza
            # el recorrido de la lista se hace con apuntador1
            apuntador1 = varClase.cabeza
            while apuntador1.siguiente != None:
                # el recorrido de los siguienes se hace con apuntador 2
                apuntador2 = apuntador1.siguiente
                while apuntador2 != None:
                    # intercambiar siempre y cuando el nombre siguiente sea menor
                    if apuntador1.nombre > apuntador2.nombre:
                        n1 = apuntador1
                        n2 = apuntador2
                        varClase.intercambiar(n1, n2)
                        # organizar lo apuntadores luego de intercambiarlos
                        apuntador1 = n2
                        apuntador2 = n1
                    # pasar al siguiente apuntador2
                    apuntador2 = apuntador2.siguiente
                apuntador1 = apuntador1.siguiente

    def buscar(varClase, clave):
        '''Buscar un contacto por nombre con una clave'''
        global registro
        registro = {}
        i = 1
        # recorrer lista lisgada
        apuntador = varClase.cabeza
        while apuntador != None:
            if apuntador.nombre.startswith(clave):
                registro[i] = apuntador
                i += 1
            apuntador = apuntador.siguiente
        
        return registro

    def modificar(varClase, nodo, nombre, movil, correo):
        '''Modificar el contacto seleccionado en buscar'''
        if nodo:
            nodo.actualizar(nombre, movil, correo)
            print("\nContacto modificado:")
            nodo.mostrar()
        else:
            print("No hay contacto seleccionado")

    def quitar(varClase, nodo):
        if nodo != None:
            # nodo es cabeza
            if nodo == varClase.cabeza:
                varClase.cabeza = nodo.siguiente
            # nodo en medio
            else:
                anteriorNodo = varClase.obtenerPredecesor(nodo)
                anteriorNodo.siguiente = nodo.siguiente
            # Si nodo es último, el nodo anterior apuntará a None
            nodo = None

    def guardarEnArchivo(varClase, nombreArchivo):
        with open(nombreArchivo, "w") as objFile:
            # recorrer la lista
            apuntador = varClase.cabeza
            while apuntador != None:
                linea = "{};{};{};{}".format(apuntador.cedula, apuntador.nombre, apuntador.correo, apuntador.movil)
                objFile.write(linea)
                objFile.write("\n")
                apuntador = apuntador.siguiente