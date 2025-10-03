palabras = ["hola", "adiós", "sídasdas", "nodsad", "python", "c"]
longitud = 4
nueva_lista=[]

for palabra in palabras:
    if len(palabra) > longitud:
        nueva_lista.append(palabra)
print(nueva_lista)