import tkinter as tk


def cambiar():
    ĺabel.config(text="ON")


ventana = tk.Tk()
ventana.title("Boton que cambia")
ventana.geometry("680x900")

ĺabel = tk.Label(ventana, text="OFF")
ĺabel.pack(pady=10)

boton = tk.Button(ventana, text="Cambiar", command=cambiar)
boton.pack()

ventana.mainloop()

