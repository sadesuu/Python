tablero = []

def crearTablero():
    Ancho = int(input("Ancho del tablero: "))
    Alto = int(input("Alto del tablero: "))
    for i in range(Alto):
        tablero.append([])
        for j in range(Ancho):
            tablero[i].append("  ")


def imprimirTablero():
    for i in range(len(tablero[0]) + 1):
       if i == 0:
           print("   | ", end="")
       else:
           print(f"{i} | ", end="")
    for i in range(len(tablero)):
        print(f"\n  {"-" *((len(tablero)+1)*3 + len(tablero)-1)}")
        print(f" {i+1} |", end="")
        #Imprime el contenido del array en la posicion inesima y añade | al final.
        for j in tablero[i]:
            print( j, end=" |")
            
def pedirMovimiento():
    fila = int(input("Introduce la fila: ")) - 1
    columna = int(input("Introduce la columna: ")) - 1
    if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero[0]):
        print("Movimiento fuera de los límites del tablero. Inténtalo de nuevo.")
        return pedirMovimiento()
    return fila, columna             
            
def comprobarGanador():
    #Comprobar filas.
    for fila in tablero:
        if all(casilla == fila[0] and casilla != "  " for casilla in fila):
            return f"🏆El ganador es {fila[0]}🏆"
    #Comprobar columnas.
    for col in range(len(tablero[0])):
        if all(tablero[row][col] == tablero[0][col] and tablero[0][col] != "  " for row in range(len(tablero))):
            return f"🏆El ganador es {tablero[0][col]}🏆"
    #Comprobar diagonales si el tablero es cuadrado.
    if len(tablero) == len(tablero[0]):
        if all(tablero[i][i] == tablero[0][0] and tablero[0][0] != "  " for i in range(len(tablero))):
            return f"🏆El ganador es {tablero[0][0]}🏆"
        if all(tablero[i][len(tablero)-1-i] == tablero[0][len(tablero)-1] and tablero[0][len(tablero)-1] != "  " for i in range(len(tablero))):
            return f"🏆El ganador es {tablero[0][len(tablero)-1]}🏆"
    # Comprobar empate
    for fila in tablero:
        for casilla in fila:
            if casilla == "  ":
                return   # Todavía hay casillas libres.
    return "🤝¡Empate!🤝"           
            
def jugador(simbolo):
    print(f"\nTurno del Jugador({simbolo})")
    pedirMovimiento()
    fila, columna = pedirMovimiento()
    if tablero[fila][columna] == "  ":
        tablero[fila][columna] = simbolo
        ganador = comprobarGanador()
        if ganador:
            imprimirTablero()
            print(ganador)
            return True
    else:
        print("Movimiento inválido, intenta de nuevo.")
        return jugador(simbolo)

def jugadorVSjugador():
    crearTablero()
    turno = 0
    simbolos = [" X", " O"]
    while True:
        imprimirTablero()
        if jugador(simbolos[turno]):
            break
        turno = 1 - turno  # Alterna entre 0 y 1
    
jugadorVSjugador()