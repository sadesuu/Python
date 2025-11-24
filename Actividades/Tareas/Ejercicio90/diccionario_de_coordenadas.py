coord = {
    "A" : (1,2),
    "B" : (3,4),
    "C" : (5,6),
    "D" : (7,8),
    "E" : (9,10)
}

maximo = ["",0]

for i in coord.keys():
    distancia = sum(coord.get(i))
    if distancia > maximo[1]:
        maximo[0] = i
        maximo[1] = distancia
print(maximo)