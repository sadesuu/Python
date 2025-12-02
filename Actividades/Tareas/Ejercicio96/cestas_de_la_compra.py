catalogo = {"pan":1.2, "leche":1.5, "huevos":2.3, "arroz":1.1}
cestas = {
    "cesta1": {"pan":2, "leche":1, "huevos":12},
    "cesta2": {"arroz":1, "leche":2},
    "cesta3": {"pan":1, "huevos":6, "arroz":2}
}

cesta_cara = ""
for cesta, productos in cestas.items():
    total = 0
    for producto, cantidad in productos.items():
        if producto in catalogo:
            total += catalogo[producto] * cantidad

    print(f"El total de la {cesta} es: {total:.2f} euros")

    if cesta_cara == "" or total > cesta_cara[1]:
        cesta_cara = (cesta, total)
print(f"La cesta más cara es {cesta_cara[0]} con un total de {cesta_cara[1]:.2f} euros")