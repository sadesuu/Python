import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Conversor de Grados")
root.geometry("300x250")


#De grados Celsius a Fahrenheit y viceversa en la misma ventana, utilizando grid(). Añadir un botón limpiar que borre los entry y cambiar el color del resultado a azul (temperaturas menores a 20 grados Celsius) si hace frío o rojo si hace calor (temperaturas mayores a 20 grados Celsius.
def celsius_a_fahrenheit():
    try:
        c = float(celsius.get())
        f = c * 9 / 5 + 32
        resultado.config(text=f"Fahrenheit: {f:.2f}")
        if c > -20:
            resultado.config(fg="blue")
        else:
            resultado.config(fg="red")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

def fahrenheit_a_celsius():
    try:
        f = float(fahrenheit.get())
        c = (f - 32) * 5 / 9
        resultado.config(text=f"Celsius: {c:.2f}")
        if c > -20:
            resultado.config(fg="blue")
        else:
            resultado.config(fg="red")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

def limpiar():
    celsius.delete(0, tk.END)
    resultado.config(text="", fg="black")

celsius_label = tk.Label(root, text="Grados Celsius:")
celsius_label.grid(row=0, column=0, padx=10, pady=10)
celsius = tk.Entry(root)
celsius.grid(row=0, column=1, padx=10, pady=10)

fahrenheit_label = tk.Label(root, text="Grados Fahrenheit:")
fahrenheit_label.grid(row=1, column=0, padx=10, pady=10)
fahrenheit = tk.Entry(root)
fahrenheit.grid(row=1, column=1, padx=10, pady=10)

convertir_c_a_f = tk.Button(root, text="C a F", command=celsius_a_fahrenheit)
convertir_c_a_f.grid(row=2, column=0, padx=10, pady=10)
convertir_f_a_c = tk.Button(root, text="F a C", command=fahrenheit_a_celsius)
convertir_f_a_c.grid(row=2, column=1, padx=10, pady=10)

limpiar_button = tk.Button(root, text="Limpiar", command=limpiar)   
limpiar_button.grid(row=3, column=0, columnspan=2, pady=10)

resultado = tk.Label(root, text="")
resultado.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()