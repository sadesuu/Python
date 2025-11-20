

stock = {
    "Nombre" : "Leche",
    "Precio": 10,
    "Cantidad" : 5
}

nuevoPrecio = int(input("Introduzca el nuevo precio: "))
stock.update({"Precio": nuevoPrecio})
print(stock)