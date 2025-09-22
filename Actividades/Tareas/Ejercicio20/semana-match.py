opcion = input("Di un dia de la semana: ").lower()

match opcion:
    case "sabado" | "domingo":
        print("No es laborable")
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print("Es laborable")
    case _:
        print("No es un día válido")
