paises = {
    "España": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "Francia": ["París", "Lyon", "Marsella", "Niza"],
    "Italia": ["Roma", "Milán", "Nápoles", "Turín"],
    "Alemania": ["Berlín", "Múnich", "Hamburgo", "Fráncfort"],
    "Estados Unidos": ["Washington D.C.", "Nueva York", "Los Ángeles", "Chicago"]
}

opcion = input("Ingrese el nombre de un país para ver sus ciudades (España, Francia, Italia, Alemania, Estados Unidos): ").lower()

for pais, ciudades in paises.items():
    if pais.lower() == opcion:
        print(f"Las ciudades principales de {pais} son:")
        for ciudad in ciudades:
            print(f"- {ciudad}")
        break

if opcion == "madrid":
    print("Madrid es la capital de España.")
else:
    print("País no encontrado en el diccionario.")
