lista = "hola adios hola hola que tal adios"
dic = {}

for lista in lista.split(" "):
    if lista not in dic:
        dic[lista] = 1
    else:
        dic[lista] += 1
print(dic)