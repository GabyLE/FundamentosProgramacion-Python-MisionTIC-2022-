print("Operación aritmética dos números")
print("-----------------------------------------------")

print("""Opciones:
1) Suma (+)
2) Resta (-)
3) División (/)
4) Multiplicación (*)""")

operaciones = {1: "+", 2: "-", 3: "/", 4: "*"}
# VALIDACIÓN
try:
    # ENTRADA
    num_1 = float(input("Ingrese un primer número: "))
    num_2 = float(input("Ingrese el segundo número: "))
    oper = int(input("Seleccione la operación aritmética: "))
    nOper = operaciones[oper]
    # PROCESO
    if oper == 1:
        val_f = num_1 + num_2
    elif oper == 2:
        val_f = num_1 - num_2
    elif oper == 3:
        if num_2 != 0:
            val_f = num_1 / num_2
        else:
            print("No se puede dividir por cero(0)")
    else:
        val_f = num_1 * num_2
    print("------------------------------------------------------")
    print("{} {} {} = {}".format(num_1,nOper,num_2,val_f ))

except:
    print("Datos no válidos")