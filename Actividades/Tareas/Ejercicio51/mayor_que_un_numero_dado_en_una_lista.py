numeros = [3, 7, 12, 18, 25, 31, 37, 44, 50, 57, 63, 70, 77, 83, 90, 96,15,41,68,99]
numeros_mayores =[]
usuario = int(input("Introduzca un número: "))

num_max = numeros[0]
for i in numeros:
    if  i > num_max:
        num_max = i
    if i > usuario:
        numeros_mayores.append(i)

numeros_copia = numeros_mayores.copy()
ordenada = []
while numeros_copia:
    minimo = numeros_copia[0]
    for num in numeros_copia:
        if num < minimo:
            minimo = num
    ordenada.append(minimo)
    numeros_copia.remove(minimo)
print(f"Números mayores que {usuario}: {ordenada}")

        
