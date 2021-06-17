from tkinter import *
from tkinter import ttk

# ventana
v = Tk()
v.title("Probando Treeview")

nameFiles = ["codigo.py", "codigo2.py", "README.txt"]
sizeFiles = ["3 Mb", "400 bytes", "200 bytes"]
modFiles = ["18:30", "2:00", "15:45"]
# Treeview object
tv = ttk.Treeview(v)
tv['columns'] = ("size", "lastmod")
# headeres
tv.heading("#0", text = "Archivo" )
tv.heading("size", text= "Tamaño")
tv.heading("lastmod", text= "Última modificación")
# inserta datos
for i in range(len(nameFiles)):
    tv.insert("", END, text = nameFiles[i], values = (sizeFiles[i], modFiles[i]))

tv.pack()
v.mainloop()
