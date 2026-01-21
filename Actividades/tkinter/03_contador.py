import tkinter as tk

contador = 0

def sumar():
    global contador
    contador +=1
    label.config(text=contador)

ventana = tk.Tk()
label = tk.Label(ventana, text=contador)
label.pack()

boton = tk.Button(ventana, text="+1", command=sumar)
boton.pack()

ventana.mainloop()

