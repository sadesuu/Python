frases = "hola que tal misael mesa".split(" ")

dic = {}


for palabra in frases:
    if palabra[0] in dic:
        dic[palabra[0]].append(palabra)
        dic[palabra[0]].sort()
    else:
        dic[palabra[0]] = [palabra]
print(dic)