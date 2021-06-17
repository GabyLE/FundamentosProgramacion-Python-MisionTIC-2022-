from Lista import Lista
from Nodo import Nodo

def leerNumero(mensaje):
    numero = 0
    numeroValido = False
    while not numeroValido:
        try :
            numero = float(input(mensaje))
            numeroValido = True
        except:
            print("El dato no es numérico!")
    return numero

def seleccionarRegistro(registro):
    nodoBuscado = None
    # no encontró nada
    if len(registro) == 0:
        print("No se encontraron coincidencias")

    else:
        print("Se encontraron los siguientes contactos:")
        for key in registro:
            print("Registro:", key)
            registro[key].mostrar()
            print("-----------------------------------------------------------")
        lstKeys = list(registro.keys())
        seleccionRegistro = 0
        while seleccionRegistro not in lstKeys:
            seleccionRegistro = leerNumero("\nSelecccione un registro: ")
        nodoBuscado = registro[seleccionRegistro]
        print("\nSeleccionó el siguiente contacto:")
        nodoBuscado.mostrar()
    
    return nodoBuscado


contactos = Lista()
contactos.desdeArchivo("Contactos.txt")

opcionMenu = 0
while opcionMenu != 8:
    print("********** Menú de Contactos **********")
    print("1. Agregar contacto")
    print("2. Listar")
    print("3. Buscar contacto")
    print("4. Modificar contacto")
    print("5. Quitar contacto")
    print("6. Ordenar")
    print("7. Guardar archivo")
    print("8. Salir")

    opcionMenu = leerNumero("Elija una opción: ")
    # Agregar un contacto
    if opcionMenu == 1:
        print("Datos del Contactos a agregar:")
        apellido = input("Apellido: ").upper()
        nombre = input("Nombre: ").upper()
        movil = input("Móvil: ")
        correo = input("Correo: ")
        cedula = input("Cédula: ")
        n = Nodo(apellido + " " + nombre, movil, correo, cedula)
        contactos.agregar(n)
    # Listar contactos
    elif opcionMenu == 2:
        prefijo = input("Mostrar que comience por: ")
        contactos.listar(prefijo)
    # Buscar contacto por nombre
    elif opcionMenu == 3:
        clave = input("Ingrese: ")
        registro = contactos.buscar(clave.upper())
        nodoBuscado = seleccionarRegistro(registro)
    # Modificar contacto seleccionado
    elif opcionMenu == 4:
        print("Registro actual:")
        nodoBuscado.mostrar()
        nombre2 = input("Nombre: ").upper()
        movil2 = input("Móvil: ")
        correo2 = input("Correo: ")
        contactos.modificar(nodoBuscado, nombre2, movil2, correo2)
    # Eliminar contacto seleccionado
    elif opcionMenu == 5:
        contactos.quitar(nodoBuscado)
        print("El contacto fue eliminado exitosamente")
    # Ordenar lista alfabéticamente
    elif opcionMenu == 6:
        contactos.ordenar()
        print("La lista fue ordenada alfabéticamente")
    # Guardar lista de contactos en archivo
    elif opcionMenu == 7:
        contactos.guardarEnArchivo("Contactos.txt")
        print("El lista fue guardada en el archivo 'Contactos.txt'")
    # Salir del aplicativo
    elif opcionMenu != 8:
        print("Opcion no válida")