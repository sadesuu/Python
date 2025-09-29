companeros, ordenada = ["misa", "figue", "wassim", "hugo", "alex"], []

while companeros:
    letra_min = companeros[0]
    for letra in companeros:
        if letra < letra_min:
            letra_min = letra
    ordenada.append(letra_min)
    companeros.remove(letra_min)
print(ordenada)