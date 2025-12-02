dic = {
    "Wassim": {"nota1": 7.5, "nota2": 8.0, "nota3": 6.5},
    "Juan": {"nota1": 5.0, "nota2": 6.0, "nota3": 7.0},
    "Emily": {"nota1": 9.0, "nota2": 8.5, "nota3": 9.5},
    "Raúl": {"nota1": 4.0, "nota2": 3.5, "nota3": 3.0}
}


for alumno in dic:
    notas = dic[alumno]
    media = sum(notas.values()) / len(notas)
    dic[alumno]["media"] = round(media, 2)
    print(f"La media de {alumno} es: {media:.2f}")


mejor_media = ["", 0]
for alumno in dic:
    if dic[alumno]["media"] > mejor_media[1]:
        mejor_media[0] = alumno
        mejor_media[1] = dic[alumno]["media"]
print(f"El alumno con mejor media es {mejor_media[0]}")


peor_media = ["", 10]
for alumno in dic:
    if dic[alumno]["media"] < peor_media[1]:
        peor_media[0] = alumno
        peor_media[1] = dic[alumno]["media"]
print(f"El alumno con peor media es {peor_media[0]}")