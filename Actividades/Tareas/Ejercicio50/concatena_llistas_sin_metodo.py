lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_conc = []
j = 5
for i in range(1,len(lista1)):
    lista_conc.append(i)
    j = j-i
    lista_conc.append(j)
    
print(lista_conc)

