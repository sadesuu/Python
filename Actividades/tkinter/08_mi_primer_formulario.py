import tkinter as tk

def guardar():
    texto = entrada1.get() + " | " + entrada2.get()
    label.config(text= texto)

ventana = tk.Tk()

ventana.geometry("680x900")

nombre = tk.Label(text="Nombre")
nombre.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

edad = tk.Label(text="Edad")
edad.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Guardar", command=guardar)
boton.pack()

label = tk.Label(ventana, text="")
label.pack()

ventana.mainloop()

    
