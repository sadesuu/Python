import tkinter as tk

ventana = tk.Tk()
ventana.title("Formulario con Grid")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1, padx=10, pady=5)

edad = tk.Entry(ventana)
edad.grid(row=1, column=1, padx=10, pady=5)

tk.Button(ventana, text="Enviar").grid(row=2, columnspan=2, pady=10)

ventana.mainloop()