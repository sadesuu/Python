import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Mi primera interfaz gráfica ")
ventana.geometry("680x900")



def saludar():
    messagebox.showinfo("Saludo", "!Hola, mundo¡")

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=20)

ventana.mainloop()