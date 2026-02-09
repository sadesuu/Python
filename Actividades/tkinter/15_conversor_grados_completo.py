import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Conversor de Grados")
root.geometry("300x250")

def celsius_a_fahrenheit():
    try:
        c = float(celsius.get())
        f = c * 9 / 5 + 32
        resultado.config(text=f"Fahrenheit: {f:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

def fahrenheit_a_celsius():
    try:
        f = float(fahrenheit.get())
        c = (f - 32) * 5 / 9
        resultado.config(text=f"Celsius: {c:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido en Fahrenheit")

celsius_label = tk.Label(root, text="Grados Celsius:")
celsius_label.pack()
celsius = tk.Entry(root)
celsius.pack()
convertir_c_f_button = tk.Button(root, text="Convertir a Fahrenheit", command=celsius_a_fahrenheit)
convertir_c_f_button.pack()

fahrenheit_label = tk.Label(root, text="Grados Fahrenheit:")
fahrenheit_label.pack() 
fahrenheit = tk.Entry(root)
fahrenheit.pack()

convertir_f_c_button = tk.Button(root, text="Convertir a Celsius", command=fahrenheit_a_celsius)
convertir_f_c_button.pack()
resultado = tk.Label(root, text="")
resultado.pack()
root.mainloop()