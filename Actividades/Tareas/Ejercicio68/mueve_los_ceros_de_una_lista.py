numeros = [0,0, 1, 0, 3, 12, 0, 5]

for i in numeros:
    if i == 0:
        numeros.remove(i)
        numeros.append(i)
print(numeros)