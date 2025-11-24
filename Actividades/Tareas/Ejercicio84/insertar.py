productos = {}
producto = ""
while producto != "fin":
    producto = input("Introduzca el producto: ")
    precio = int(input("Introduzca el precio"))
    productos.update({producto:precio})
    sumaTotal += precio
print(f"Precio total: {sumaTotal}")
