lista = [1, 2, 3, 3]
lista.sort()
lista_contada = []
contador = 0

for i in lista:
    for j in lista:
        if i == j:
            contador += 1
    lista_contada.append((i, contador))
    contador = 0
print(f"{lista_contada[0][0]}:{lista_contada[0][1]}")