numero = int(input("Ingrese un número entero mayor que 1: "))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")