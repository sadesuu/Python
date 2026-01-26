import tkinter as tk

root = tk.Tk()
root.title("Calculadora con Grid")

ventana = tk.Entry(root, justify="right")

ventana.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

tk.Button(root, text="1").grid(row=1, column=0)
tk.Button(root, text="2").grid(row=1, column=1)
tk.Button(root, text="3").grid(row=1, column=2)

tk.Button(root, text="4").grid(row=2, column=0)
tk.Button(root, text="5").grid(row=2, column=1)
tk.Button(root, text="6").grid(row=2, column=2)

tk.Button(root, text="7").grid(row=3, column=0)
tk.Button(root, text="8").grid(row=3, column=1)
tk.Button(root, text="9").grid(row=3, column=2)

tk.Button(root, text="0").grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()