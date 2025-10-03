lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0

for numero in lista:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")