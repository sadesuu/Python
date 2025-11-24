alumnos = {
    "hugo" : 10,
    "figue" : 9,
    "wassim" : 5
}

notaInicial = alumnos.get("hugo")
for i in alumnos:
    if alumnos[i] > notaInicial:
        notaInicial = i
print(notaInicial)