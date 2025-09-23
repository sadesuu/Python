colores = ["rojo", "verde", "azul", "amarillo"]
pregunta = input("Que color quieres borrar(rojo, verdde, azul, amarillo): ").lower()
colores.remove(pregunta)
print(colores)