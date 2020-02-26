from tkinter import *
root = Tk()
root.title("Agenda")
root.geometry('200x150')
root.resizable(width=False, height=False)

header = Label(root, text="Agenda",font=("Arial Bold", 20))
header.grid(column=1, row=0)
# Nombre del contacto
lblnombre = Label(root, text="Nombre: ")
lblnombre.grid(column=0, row=1)
nombre = Entry(root)
nombre.grid(column=1, row=1)
# Nro del contacto
lblnro = Label(root, text="Numero: ")
lblnro.grid(column=0, row=2)
nro = Entry(root)
nro.grid(column=1, row=2)
# Boton guardar en base de datos
btn = Button(root, text="Guardar contacto")
btn.grid(column=1, row=3)
# entry.pack()
root.mainloop()