numeros = [5, 2, 9, 1, 5, 6]
ordenada = []

numeros_copia = numeros.copy()
while numeros_copia:
    minimo = numeros_copia[0]
    for num in numeros_copia:
        if num < minimo:
            minimo = num
    ordenada.append(minimo)
    numeros_copia.remove(minimo)
print(ordenada)

numeros_copia = numeros.copy()
ordenada2 = []
while numeros_copia:
    maximos = numeros_copia[0]
    for num in numeros_copia:
        if num > maximos:
            maximos = num
    ordenada2.append(maximos)
    numeros_copia.remove(maximos)
print(ordenada2)
