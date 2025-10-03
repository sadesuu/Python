lista = [1,2,3,4,5,6,7,8,9]
lista_del_reves = []

while lista:
    lista_del_reves.append(lista[-1])
    lista.pop()
print(lista_del_reves)