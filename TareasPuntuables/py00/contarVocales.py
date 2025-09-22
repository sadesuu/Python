palabra = input("Introduce una palabra: ")
vocales = 'aeiouAEIOU'
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"Número de vocales: {contador}")