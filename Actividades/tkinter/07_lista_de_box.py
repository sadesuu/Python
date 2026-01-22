import tkinter as tk



def seleccionar(event):
    label.config(text=listbox.get(listbox.curselection()))


ventana = tk.Tk()
ventana.geometry("680x900")
listbox =tk.Listbox(ventana)

for ciudad in ["Madrid", "Sevilla", "Valencia", "Bilbao"]:
    listbox.insert(tk.END, ciudad)
listbox.pack()
listbox.bind("<<ListboxSelect>>", seleccionar)

label = tk.Label(ventana, text="")
label.pack()

ventana.mainloop()