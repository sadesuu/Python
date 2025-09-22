nota = int(input("Que nota has sacado(0-10): "))

match nota:
    case 0,1,2:
        print("Muy deficiente")
    case 3,4:
      print("Deficiente")
    case 5: 
        print("Aprobado")
    case 6:
        print("Bien")
    case 7, 8: 
        print("Notable")
    case 9:
        print("Sobresaliente")
    case 10:
        print("Matricula de honor")
    case _:
        print("Introduzca un número valido")