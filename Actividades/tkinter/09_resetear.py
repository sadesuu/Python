import tkinter as tk

def limpiar():
    e1.delete(0, tk.END)
    e2.delete(0,tk.END)
    resultado.config(text="")

ventana = tk.Tk()
ventana.title("Limpiar campos")

tk.Label(ventana, text="Numero 1").pack()
e1 = tk.Entry(ventana)
e1.pack()

tk.Label(ventana, text="Numero 2").pack()
e2 = tk.Entry(ventana)
e2.pack()

boton = tk.Button(ventana, text="Limpiar", command=limpiar)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()
    