import tkinter as tk


def mostrar():
    label.config(text=entrada.get())

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Mostrar", command=mostrar)
boton.pack()

label = tk.Label(ventana, text="")
label.pack()

ventana.mainloop()
