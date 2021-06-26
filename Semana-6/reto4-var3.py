class cliente:
    
    def __init__(self, nombre, edad, dinero_cuenta_bancaria, fila_interes, transaccion, cantidad_retirar, cantidad_consignar):
        self.nombre = nombre
        self.edad = edad
        self.dinero_cuenta_bancaria = dinero_cuenta_bancaria
        self.fila_interes = fila_interes
        self.transaccion = transaccion
        self.cantidad_retirar = cantidad_retirar
        self.cantidad_consignar = cantidad_consignar

# ***********************************************************************************************************************************

# FUNCIONES
def agregarCola(nombre, cola):
    cola.append(nombre)

def suma(lista):
    suma = 0
    if len(lista) > 0:
        for i in lista:
            suma += i
    return suma

def minimo(lista):
    
    if len(lista) > 0:
        min = lista[0]
        for i in lista[1:]:
            if i < min:
                min = i
    else:
        min = -1
    return min

def sede_bancaria(cola_general):

    cola_caja = []
    cola_info = []
    lst_retiros = []
    lst_consignaciones = []
    edad_retiro = []
    edad_consignacion = []
    edad_info = []

    # recorre la fila de clientes
    for cliente in cola_general:
        # asigna el cliente que va a caja a la fila de caja
        if cliente.fila_interes == "caja":
            agregarCola(cliente.nombre, cola_caja)
            # el cliente va a realizar un retiro
            if cliente.transaccion == "retirar":
                # adiciona el valor a retirar
                lst_retiros.append(cliente.cantidad_retirar)
                # adiciona edad del cliente
                edad_retiro.append(cliente.edad)
            # el cliente va realizar una consignación
            elif cliente.transaccion == "consignar":
                # adiciona el valor a consignar
                lst_consignaciones.append(cliente.cantidad_consignar)
                # adiciona edad del cliente
                edad_consignacion.append(cliente.edad)         
        # asigna el cliente a la fila de información
        elif cliente.fila_interes == "info":
            agregarCola(cliente.nombre, cola_info)
            edad_info.append(cliente.edad)

    suma_retiros = suma(lst_retiros)
    suma_consignaciones = suma(lst_consignaciones)
    edad_minima_retiro = minimo(edad_retiro)
    edad_minima_info = minimo(edad_info)
    edad_minima_consignacion = minimo(edad_consignacion)
    
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion 
    # return lst_consignaciones, lst_retiros, cola_caja, cola_info, edad_retiro, edad_consignacion, edad_info

a, b, c, d, e, f, g = sede_bancaria([cliente("Matt",21,235000,"caja","retirar",100000,0),cliente("Dan",32,658000,"caja","retirar",98000,0),cliente("Diana",29,87000,"info","ninguna",0,0)])

print("CAJA:", a)
print("INFORMACIÓN:", b)
print("SUMA RETIROS:", c)
print("SUMA CONSIGNACIONES:", d)
print("EDAD MIN RETIROS:", e)
print("EDAD MIN INFORMACIÓN:", f)
print("EDAD MIN CONSIGANCIONES:", g)










