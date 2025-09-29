lista = ["manzana" , "platano" , "fresa",["leon", "gato", "perro"]]

for i in range(len(lista)-1):
    print(lista[i], end= " ")
print("\n")
for j in range(len(lista[3])):
    print(lista[-1][j], end=" ")
    
    