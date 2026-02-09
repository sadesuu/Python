import tkinter as tk

def mostrar_tabla():
    numero = int(entry_numero.get())
    resultado = ""
    for i in range(1, 11):
        resultado += f"{numero} x {i} = {numero * i}\n"
    label_resultado.config(text=resultado)
root = tk.Tk()
root.title("Tabla de Multiplicar")
root.geometry("680x600")
label_instruccion = tk.Label(root, text="Ingrese un número:")
label_instruccion.pack(pady=10)
entry_numero = tk.Entry(root)
entry_numero.pack(pady=5)
button_mostrar = tk.Button(root, text="Mostrar Tabla", command=mostrar_tabla)
button_mostrar.pack(pady=10)
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)
root.mainloop()