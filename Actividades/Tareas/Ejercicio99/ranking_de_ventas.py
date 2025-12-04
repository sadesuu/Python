ventas = [("Pepe", 200), ("Juanito", 150), ("Pitingo", 50), ("Optimus_Prime", 300), ("Pitingo", 50), ("Optimus_Prime", 300), ("Juanito", 150)]

ranking_ventas = {}

for vendedor, monto in ventas:
    if vendedor in ranking_ventas:
        ranking_ventas[vendedor] += monto
    else:
        ranking_ventas[vendedor] = monto
ranking_ordenado = sorted(ranking_ventas.items(), key=lambda x: x[1], reverse=True)

print(ranking_ordenado)