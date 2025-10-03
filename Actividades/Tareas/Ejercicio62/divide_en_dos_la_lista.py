lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista1 = []
lista2 = []
limite = int(input("Introduce el número límite para dividir la lista: "))

for numero in lista_numeros:
    if numero <= limite:
        lista1.append(numero)
    else:
        lista2.append(numero)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")