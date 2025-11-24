dic = {
    "mates" : [5,8,7,9],
    "lengua" : [1,8,5,8,]
}

for i in dic:
    media = sum(dic[i]) / len(dic[i])
    print(f"La media de {i} es: {media:.2f}")