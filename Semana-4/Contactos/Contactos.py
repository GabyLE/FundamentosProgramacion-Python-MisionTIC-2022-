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

contactos = Lista()
contactos.desdeArchivo("Contactos.txt")

opcionMenu = 0
while opcionMenu != 7:
    print("********** Menú de Contactos **********")
    print("1. Agregar contacto")
    print("2. Listar")
    print("3. Buscar contacto")
    print("4. Modificar contacto")
    print("5. Quitar contacto")
    print("6. Ordenar")
    print("7. Salir")

    opcionMenu = leerNumero("Opcion escogida?")

    if opcionMenu == 1:
        print("Datos del Contactos a agregar:")
        nombre = input("Nombre?")
        movil = input("Móvil?")
        correo = input("Correo?")
        n = Nodo(nombre, movil, correo)
        contactos.agregar(n)
    elif opcionMenu == 2:
        contactos.mostrar()
    elif opcionMenu == 3:
        print("No implementado")
    elif opcionMenu == 4:
        print("No implementado")
    elif opcionMenu == 5:
        print("No implementado")
    elif opcionMenu == 6:
        print("No implementado")
    elif opcionMenu != 7:
        print("Opcion no válida")

    



