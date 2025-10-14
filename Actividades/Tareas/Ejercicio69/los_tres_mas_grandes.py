numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35]
mayores = []

for i in range(3):
    aux = numeros[0]
    for j in numeros:
     if j > aux:
         aux = j
    mayores.append(aux)
    numeros.remove(aux)
print(mayores)
         