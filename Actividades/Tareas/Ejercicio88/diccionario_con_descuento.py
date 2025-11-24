productos = {
    "pan" : 1.5,
    "leche" : 0.9,
    "huevos" : 2.5,
    "carne" : 5.0,
    "pescado" : 4.0
}

productos2 = {}

descuento = int(input("Introduzca el descuento: "))

for producto, precio in productos.items():
    if descuento < 100:
         productos2.update({producto : round((precio * (1 - descuento / 100)), 2)})
    else: 
         print("Descuento no valido.")
print(productos2)