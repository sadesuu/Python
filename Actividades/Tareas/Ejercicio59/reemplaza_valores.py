lista = [1, 2, 3, 3, 4]
lista.sort()
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
for i in range(len(lista)):
    if lista[i] == num1:
        lista[i] = num2
print(lista)
