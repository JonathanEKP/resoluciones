from cProfile import label
from cgitb import text
from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")


root = Tk()
opcion = StringVar()
opcion.set(None)


Radiobutton(root, text="Hola", variable=opcion, 
            value='Hola', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Hello", variable=opcion, 
            value='Hello', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Programar", variable=opcion,   
            value='Programar', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Java", variable=opcion,   
            value='Java', command=seleccionar).pack(anchor=W)


monitor = Label(root)
monitor.pack()
Button(root, text="Limpiar", command=reset).pack()

root.mainloop()