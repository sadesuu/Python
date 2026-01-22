import tkinter as tk

def cambiar():
    label.config(fg=color.get())

ventana = tk.Tk()

color = tk.StringVar(value="black")

for c in ["red", "green", "blue"]:
    tk.Radiobutton(ventana, text=c,value=c,variable=color, command=cambiar).pack()


label = tk.Label(ventana, text="Los alumnos de 2DAM \n son unos profesionales, \n")
label.pack(pady=10)

ventana.mainloop()