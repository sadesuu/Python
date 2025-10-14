lista = [-1,-2,-3, 0, 1, 2,3]
contador = 0

for i in lista:
    if i < 0: 
        contador +=1
        print(i)
print(f"Son {contador} numeros negativos.")