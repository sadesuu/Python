numero = int(input("Ingrese un número entero mayor que 1: "))
primos = []
for num in range(2, numero):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)
print(f"Números primos hasta {numero}: {primos}")
