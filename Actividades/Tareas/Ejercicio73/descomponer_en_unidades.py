numero = input("Introduzca un numero: ")



for i in range(len(numero)):
    if numero[i] == numero[0]:
        print(f"{numero[i]} centesimas")
    elif numero[i] == numero[1]:
        print(f"{numero[i]} decimas")
    elif numero[i] == numero[2]:
        print(f"{numero[i]} unidades")
