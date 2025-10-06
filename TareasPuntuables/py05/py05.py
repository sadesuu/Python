palabras = ["sol", "luna", "mar", "estrella", "cielo"]  
filtrado = []
for i in palabras:
    for j in i[0]:
        if j == 's':
            filtrado.append(i)
print(filtrado)