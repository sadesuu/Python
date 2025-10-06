palabras = ["sol", "luna", "mar", "estrella", "cielo"]  
nuevas = []
inicial = input("Introduce una letra: ").lower()

for i in palabras:
    if i.startswith(inicial):
        nuevas.append(i)
print(nuevas)
    