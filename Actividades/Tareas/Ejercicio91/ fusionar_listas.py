nombres = [" Ana", "Luis", "Carlos"]
telefonos = [123456789,987654321,456123789]

dic = {}

for i in nombres:
    for j in telefonos:
        dic.update({i:j})
print(dic)  