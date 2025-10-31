from funciones import jugadorContraJugador, jugadorContraMaquina, maquinaContraMaquina

print("Selecciona el modo de juego: ")
print("1. Jugador contra jugador")
print("2. Jugador contra maquina")
print("3. Maquina contra maquina")
opcion = int(input(""))

match opcion:
    case 1:
        jugadorContraJugador()
    case 2:
        jugadorContraMaquina()
    case 3:
        maquinaContraMaquina()
    case _:
        print("Introduzca un modo válido")