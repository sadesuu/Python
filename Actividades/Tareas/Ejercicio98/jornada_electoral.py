
delegados = {}

flag = True
flag2 = True
while flag:

    nombres = input("Introducá los nombres de los candidatos: ")
    delegados.update({nombres : 0})

    continuar = input("Desea contuniar(s/n): ")
    if continuar == "n":
        flag = False
    else: 
        flag = True


while flag2:
    for i in delegados:
        print(f"-{i}")
    voto = input("Elige que delegado quieres: ")

    if delegados.__contains__(voto):
        delegados[voto] +=1
    if voto == "fin":
        flag2 = False
print(delegados)

