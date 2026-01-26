import tkinter as tk

root = tk.Tk()
root.title("Calculadora básica")
root.geometry("300x250")
def sumar():
    num1 = float(e1.get())
    num2 = float(e2.get())
    resultado = num1 + num2
    resultado_label.config(text=f"Resultado: {resultado}")

def restar():
    num1 = int(e1.get())
    num2 = int(e2.get())

    resultado = num1 - num2
    resultado_label.config(text=f"Resultado: {resultado}")


def dividir():
    num1 = int(e1.get())
    num2 = int(e2.get())

    resultado = num1 / num2
    resultado_label.config(text=f"Resultado: {resultado}")

def multiplicar():
    num1 = int(e1.get())
    num2 = int(e2.get())

    resultado = num1 * num2
    resultado_label.config(text=f"Resultado: {resultado}") 

tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)

e2 = tk.Entry(root)
e2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Sumar", command= sumar).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Restar", command= restar).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Dividir", command= dividir).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Multiplicar", command= multiplicar).grid(row=5, column=0, padx=10, pady=10)

resultado_label = tk.Label(root, text="Resultado: ")
resultado_label.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()