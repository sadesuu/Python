productos = {
    "manzanas": 50,
    "naranjas": 75,
    "platanos": 100,
    "peras": 60
}

flag = True

while flag: 
    usuario = input("Desea continuar(s/n): ").lower()
    if usuario == "n":
        flag = False
    else: 
        for i in productos:
             print(f"{i} : {productos[i]}")
        product = input(" Ingrese el producto que desea consultar: ").lower()
        updateStock = (input("Que operacion desea realizar (+ o -): "))
        cantidad = int(input("Ingrese la cantidad: "))
        if updateStock == "+":

            productos.update({product : (productos[product] + cantidad)})
            for i in productos:
             print(f"{i} : {productos[i]}")
        elif productos[product] >= cantidad: 
                productos.update({product : (productos[product] - cantidad)})
                for i in productos:
                    print(f"{i} : {productos[i]}")
        else:
            print("Operación no válida")