from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
from tkinter.font import names
import Varios

# CONTROLES, VENTANAS, CANVAS, ...
# ventana
v = Tk()
v.title("Mis contactos")

# Contenedor ventana emergente
# cvEliminar = Canvas(v, width= 300, height= 300)

# contenedor Notebook
frmTab = Frame(v)
frmTab.grid(row= 5, column= 0, columnspan=8) 

# control pestaña
tabControl = ttk.Notebook(frmTab)

# pestañas
tab1 = Frame(tabControl)

# adding tab
tabControl.add(tab1, text = "Lista Contactos")

# Packin the tab control to make the tabs visible
tabControl.pack(expand= 1, fill = "both")

# TREEVIEW
tv = ttk.Treeview(tab1)
tv['columns'] = ("nombre", "movil", "correo")
tv.column("#0", width=0, stretch=NO)
tv.column("nombre")
tv.column("movil")
tv.column("correo")
# headers
tv.heading("#0", text= "")
tv.heading("nombre", text= "Nombre")
tv.heading("movil", text= "Móvil")
tv.heading("correo", text= "Correo")
tv.pack()

# IMAGENES BOTONES
# agregar
pngAdd = PhotoImage(file = "img/add.png")
pngAddR = pngAdd.subsample(12, 12)
# modificar
pngEdit = PhotoImage(file = "img/edit.png")
pngEditR = pngEdit.subsample(12, 12)
# eliminar
pngDel = PhotoImage(file = "img/delete.png")
pngDelR = pngDel.subsample(12, 12)
# guardar
pngSave = PhotoImage(file = "img/save.png")
pngSaveR = pngSave.subsample(12, 12)
# ordenar
pngSort = PhotoImage(file = "img/filter.png")
pngSortR = pngSort.subsample(12, 12)
# buscar
pngLook = PhotoImage(file = "img/look.png")
pngLookR = pngLook.subsample(12, 12)

# LABELS
Label(v, text= "Nombre", font= "Consolas 12").grid(row=1, column=0)
Label(v, text= "Apellido", font= "Consolas 12").grid(row=2, column=0)
Label(v, text= "Móvil", font= "Consolas 12").grid(row=3, column=0)
Label(v, text= "Correo", font= "Consolas 12").grid(row=4, column=0)

# ENTRY
txtName = Entry(v, width= 30, font= "Consolas 12")
txtName.grid(row=1, column=1)
txtLastName = Entry(v, width= 30, font= "Consolas 12")
txtLastName.grid(row=2, column=1)
txtMovil = Entry(v, width= 30, font= "Consolas 12")
txtMovil.grid(row=3, column=1)
txtMail = Entry(v, width= 30, font= "Consolas 12")
txtMail.grid(row=4, column=1)

# MOSTRAR CONTACTOS
# muestra contactos en treeview formato tabla
Varios.desdeArchivo("Contactos.txt", tv)
contactos = [[tv.item(item, 'values'), item] for item in tv.get_children('')]
#print(contactos)
# FUNCIONES
# Agregar
def agregar():
    apellido = txtLastName.get().upper()
    nombre = txtName.get().upper()
    movil = txtMovil.get()
    correo = txtMail.get()
    if apellido == '' and nombre == '' and movil == '' and correo == '':
        messagebox.showerror("", "No hay datos a ingresar")       
    else:
        item = tv.insert("", END, text="", values=(apellido + " " + nombre, movil, correo))
        contactos.append([tv.item(item, 'values'), item])
        print(contactos)
        
        messagebox.showinfo("Contacto Agregado", "El contacto fue agregado exitosamente")
        
def ordenar():
    # obtiene los itemas del treeview y los agrega a la lista names
    names = [(tv.set(item, 'nombre'), item) for item in tv.get_children('')]
    # ordena la lista alfabetimente
    names.sort()
    # print(names)
    # mueve los datos de acuerdo al sorting
    for index, (values, item) in enumerate(names):
        tv.move(item, '', index)
    Varios.limpiarEntry(txtName, txtLastName, txtMovil, txtMail)
    messagebox.showinfo("", "Los contactos fueron ordenados alfabéticamente")

def actualizar():
    apellido = txtLastName.get().upper()
    nombre = txtName.get().upper()
    movil = txtMovil.get()
    correo = txtMail.get()
    # item seleccionado/highlighted
    selected = tv.focus()
    temp = tv.item(selected, 'values')
    tempFullName = temp[0].split()
    if apellido != "":
        tv.set(selected, 'nombre', apellido + " " + tempFullName[1])
    if nombre != "":
        tv.set(selected, 'nombre', tempFullName[0] + " " + nombre)
    if movil != "":
        tv.set(selected, 'movil', movil)
    if correo != "":
        tv.set(selected, 'correo', correo)

    Varios.limpiarEntry(txtName, txtLastName, txtMovil, txtMail)
    messagebox.showinfo("Modificar", "Contacto modificado")

def eliminar():
    selected = tv.focus()
    temp = tv.item(selected)
    #MsgBox = messagebox.askquestion("Eliminar contacto", "Desea eliminar el siguiente contacto: {}".format(temp), icon = 'warning')
    #if MsgBox == 'Sí':    
    tv.detach(temp)
    tv.focus()
    messagebox.showinfo("Eliminar", "El contacto fue eliminado")
    #else:
        #messagebox.showinfo("", "El contacto NO fue eliminado")
# Botones
# agregar
Button(v, text="Agregar", image = pngAddR, command= agregar).grid(row=0, column=2)
# modificar
Button(v, text="Agregar", image = pngEditR, command= actualizar).grid(row=0, column=3)
# eliminar
Button(v, text="Agregar", image = pngDelR, command= eliminar).grid(row=0, column=4)
#cvEliminar.create_window(150, 150, window = bttEliminar)
# guardar
Button(v, text="Agregar", image = pngSaveR).grid(row=0, column=5)
# ordenar
Button(v, text="Agregar", image = pngSortR, command= ordenar).grid(row=0, column=6)
# buscar
Button(v, text="Agregar", image = pngLookR).grid(row=0, column=7)

v.mainloop()