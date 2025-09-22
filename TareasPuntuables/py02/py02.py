dia = int(input("Introduce el dia de nacimiento: "))
mes = input("Introduca el mes de nacimiento: ").lower


# Aries: 21 de marzo – 20 de abril
# Tauro: 21 de abril – 20 de mayo
# Géminis: 21 de mayo – 21 de junio
# Cáncer: 22 de junio – 22 de julio
# Leo: 23 de julio – 23 de agosto
# Virgo: 24 de agosto – 22 de septiembre
# Libra: 23 de septiembre – 23 de octubre
# Escorpio: 24 de octubre – 22 de noviembre
# Sagitario: 23 de noviembre – 21 de diciembre
# Capricornio: 22 de diciembre – 20 de enero
# Acuario: 21 de enero – 19 de febrero
# Piscis: 20 de febrero – 20 de marzo

match(mes):
    case "enero":
        if dia < 20:
            print("Capricornio")
        else:
            print("Acuario")
    case "febrero":
        if dia < 19:
            print("Acuario")
        else:
            print("Piscis")
    case "marzo":
        if dia < 20:
            print("Piscis")
        else:
            print("Aries")     
    case "abril":
        if dia < 20:
            print("Aries")
        else:
            print("Tauro")
    case "mayo":
        if dia < 20:
            print("Tauro")
        else:
            print("Géminis")
    case "junio":
        if dia <20:
            print("Géminis")
        else:
            print("Cáncer")
    case "julio":
        if dia < 20:
            print("Cáncer")
        else:
            print("Leo")
    case "agosto":
        if dia < 20:
            print("Leo")
        else:
            print("Virgo")
    case "septiembre":
        if dia < 20:
            print("Virgo")
        else: 
            print("Libra")
    case "octubre":
        if dia <20:
            print("Libra")
        else:
            print("Escorpio")
    case "noviembre":
        if dia < 20:
            print("Escorpio")
        else: 
            print("Sagitario")
    case "diciembre":
        if dia <=21:
            print("Sagitario")
        else:
            print("Capricornio") 