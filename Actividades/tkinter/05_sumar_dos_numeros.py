import tkinter as tk

def sumar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())

    suma = num1 + num2
    label.config(text= suma)

ventana = tk.Tk()

ventana.geometry("680x900")
entrada1 = tk.Entry(ventana)
entrada1.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack()

label = tk.Label(ventana, text="0")
label.pack()

ventana.mainloop()

    
