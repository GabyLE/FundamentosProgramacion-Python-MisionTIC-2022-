from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
from Nodo import Nodo
from Lista import Lista

# ventana
v = Tk()
v.title("Mis contactos")

# contenedor Notebook
frmTab = Frame(v)
frmTab.grid(row= 1, column= 0, columnspan=5) 

# control pestaña
tabControl = ttk.Notebook(frmTab)

# pestañas
tab1 = Frame(tabControl)

# adding tab
tabControl.add(tab1, text = "Lista Contactos")

# Packin the tab control to make the tabs visible
tabControl.pack(expand= 1, fill = "both")

# Treeview
tv = ttk.Treeview(tab1)
tv['columns'] = ("movil", "correo")
# headers
tv.heading("#0", text= "Nombre")
tv.heading("movil", text= "Móvil")
tv.heading("correo", text= "Correo")
tv.pack()

# imagenes botones
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

# objeto lista ligada
contactos = Lista()
contactos.desdeArchivo("Contactos.txt")
contactos.listarGUI(tv)

# Botones
# agregar
Button(v, text="Agregar", image = pngAddR).grid(row=0, column=0)
# modificar
Button(v, text="Agregar", image = pngEditR).grid(row=0, column=1)
# eliminar
Button(v, text="Agregar", image = pngDelR).grid(row=0, column=2)
# guardar
Button(v, text="Agregar", image = pngSaveR).grid(row=0, column=3)
# ordenar
Button(v, text="Agregar", image = pngSortR).grid(row=0, column=4)

v.mainloop()