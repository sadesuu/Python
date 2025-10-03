lista = [1,2,3,4,5,6,7,8,9]
lista.sort()
mediana = 0
if len(lista) % 2 == 0:
    mediana = (lista[len(lista)//2 - 1] + lista[len(lista)//2]) / 2
else:
    mediana = lista[len(lista)//2]
print(f"La mediana es: {mediana}")