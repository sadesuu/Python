numero = int(input("Inserta un numero para calcular su factorial: "))
fact = 1
for numero in range(numero, 1 , -1):
    fact = fact *numero
    
print(f"El numero factorial es {fact}")

