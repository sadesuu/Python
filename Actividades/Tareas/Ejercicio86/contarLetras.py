dic = {

}
texto = input("Introduce un texto: ")
contador = 1
for letra in texto: 
    if dic.__contains__(letra):

        dic.update({letra : contador + 1})
    else: 
        dic.update({letra : contador})
print(dic)