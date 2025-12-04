aficiones = {
    "Guillermo": ["cine", "fútbol", "música"],
    "Sebas": ["ajedrez", "cine"],
    "Misael": ["música", "lectura"],
    "Hugo" : ["jugar videojuegos", "voleibol"]
}

aficiones_reverse = {}
for nombre, lista_aficiones in aficiones.items():
    for aficion in lista_aficiones:
        if aficion not in aficiones_reverse:
            aficiones_reverse[aficion] = [nombre]
        else:
            aficiones_reverse[aficion].append(nombre)


print(aficiones_reverse)