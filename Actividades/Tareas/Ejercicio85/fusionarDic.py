dic1  = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5
}

dic2 = {
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10
}

dic3= {

}

for i in dic1:
    for j in dic2:
        suma = i + j
        dic3.update({suma : suma})

print(dic3)