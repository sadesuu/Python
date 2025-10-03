lista = [1,1,1,2,2,3,3,3,3,4,5,5,5,6]
lista.sort()
lista_contada = []
contador = 0

for i in lista:
    for j in lista:
        if i == j:
            contador += 1
    lista_contada.append((i, contador))
    contador = 0
    
if len(lista_contada) > 0:
    moda = lista_contada[0]
    for i in lista_contada:
        if i[1] > moda[1]:
            moda = i
    print(f"La moda es {moda[0]} con un total de: {moda[1]}")