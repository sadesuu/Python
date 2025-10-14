tablero = [["  " for _ in range(3)] for _ in range(3)]
#Funcion que imprime un tablero inicial
def imprimirTablero():
    print("   0  | 1 | 2 |")
    #Recorre la longitud del array
    for i in range(len(tablero)):
        print("---------------")
        print(i, end=" ")
        #Imprime el contenido del array en la posicion inesima y añade | al final
        for j in tablero[i]:
            print( j, end=" | ")
        print(" ")

def comprobarGanador():
    #Comprobar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != "  ":
            return f"El ganador es {fila[0]}"
    #Comprobar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != "  ":
            return f"El ganador es {tablero[0][col]}"
    #Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "  ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "  ":
        return tablero[0][2]
    return None
    
def jugadorContraJugador():
    imprimirTablero()
    turno = 0
    while True:
        if turno % 2 == 0:
            print("Turno del Jugador X")
            fila = int(input("Inserte en que fila quiere jugar: "))
            columna = int(input("nserte en que columna quiere jugar: "))
            if tablero[fila][columna] == "  ":
                tablero[fila][columna] = "X"
                turno += 1
                comprobarGanador()
            else:
                print("Casilla ocupada")
            imprimirTablero()
        elif turno % 2 == 1:
            print("Turno del Jugador 0")
            fila = int(input("Inserte en que fila quiere jugar: "))
            columna = int(input("Inserte en que columna quiere jugar: "))
            if tablero[fila][columna] == "  ":
                tablero[fila][columna] = "0"
                turno += 1
                comprobarGanador()
            else:
                print("Casilla ocupada")
            imprimirTablero()
    


print("Selecciona el modo de juego: ")
print("1. Jugador contra jugador")
print("2. Jugador contra maquina")
print("3. Maquina contra maquina")
opcion = int(input(""))

match opcion:
    case 1:
        jugadorContraJugador()
    case 2:
        print("si")
    case 3:
        print("-")
    case _:
        print("Introduzca un modo valido")