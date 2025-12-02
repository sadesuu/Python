#Pide un texto largo. Crea un diccionario donde:

    #Las claves sean cada palabra distinta y el valor el número de veces que aparece. 
    #Los valores sean otro diccionario con: {"apariciones": x, "longitud": y}
    #Muestra las 5 palabras más frecuentes.


frase  = "Lorem ipsum dolor sit amet consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum"

dic = {

}



dic2 = {}
frases = frase.split(" ")
for palabra in frases:
    if palabra in dic:
        dic[palabra] += 1
    else:
        dic[palabra] = 1

print(dic)



for palabra in frases:
    if len(palabra) in dic2:
        dic2[len(palabra)] += 1
    else:
        dic2[len(palabra)] = 1
print(dic2)



ordenado = sorted(dic.items())

for valor in list(ordenado.reverse())[-5:]:
    print(valor)