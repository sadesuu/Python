numero = int(input("Inserta el valor"))
medida = input("En que medida esta el valor(km, hm, dam, m,dm,cm,mm)")


match medida:
    case "km":
        print("Es igual a", numero * 1000, "m")
    case "hm":
        print("Es igual a", numero * 100, "m")
    case "dam":
        print("Es igual a", numero * 10, "m")
    case "m":
        print("Es igual a", numero, "m")
    case "dm":
        print("Es igual a", numero / 10, "m")
    case "cm":
        print("Es igual a", numero / 100, "m")
    case "mm":
        print("Es igual a", numero / 1000, "m")
    case _:
        print("Medida no valida")