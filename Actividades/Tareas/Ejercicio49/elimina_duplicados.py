array = ["hola", "adios", "hola", "adios"]
sinCopia = []
for i in array:
    if i not in sinCopia:
        sinCopia.append(i)
print(sinCopia)