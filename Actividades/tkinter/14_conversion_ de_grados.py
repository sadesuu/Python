import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Conversor de Grados")


def convertir():
    try:
        c = float(celsius.get())
        f = c * 9 / 5 + 32
        resultado.config(text=f"Fahrenheit: {f:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

celsius_label = tk.Label(root, text="Grados Celsius:")
celsius_label.pack()

celsius = tk.Entry(root)
celsius.pack()

convertir_button = tk.Button(root, text="Convertir", command=convertir)
convertir_button.pack()

resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()