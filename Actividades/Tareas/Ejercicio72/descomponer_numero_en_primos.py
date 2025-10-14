numero = int(input("Introduzca un numero entero positivo: "))

while numero < 1 or numero > 1000:
    numero = int(input("Error. Introduzca un numero entero positivo: "))
divisor = 2
print(f"Descomposicion en factores primos de {numero}: ", end="")
while numero > 1:
    if numero % divisor == 0:
        print(divisor, end=" ") 
        numero /= divisor
    else:
        divisor += 1
print()



    