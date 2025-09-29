lista = [1,2,3,4,5,6,-7,-8,-9,-10]

for i in lista: 
    if i < 0:
        lista.remove(i)
print(lista)