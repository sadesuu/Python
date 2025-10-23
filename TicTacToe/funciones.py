import random

tablero = [["  " for _ in range(3)] for _ in range(3)]
#Funcion que imprime un tablero inicial
def imprimirTablero():
    print("   1  | 2 | 3 |")
    #Recorre la longitud del array.
    for i in range(len(tablero)):
        print("---------------")
        print(i+1, end=" ")
        #Imprime el contenido del array en la posicion inesima y añade | al final.
        for j in tablero[i]:
            print( j, end=" | ")
        print(" ")


def pedirMovimiento():
    fila = int(input("Inserte en que fila quiere jugar(1, 2, 3): "))
    columna = int(input("Inserte en que columna quiere jugar(1, 2, 3): "))
    if fila < 1 or fila > 3 or columna < 1 or columna > 3:
        print("Movimiento invalido, intenta de nuevo")
        return pedirMovimiento()
    return fila, columna

def comprobarGanador():
    #Comprobar filas.
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != "  ":
            return f"🏆El ganador es {fila[0]}🏆"
    #Comprobar columnas.
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != "  ":
            return f"🏆El ganador es {tablero[0][col]}🏆"
    #Comprobar diagonales.
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "  ":
        return f"🏆El ganador es {tablero[0][0]}🏆"
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "  ":
        return f"🏆El ganador es {tablero[0][2]}🏆"
    # Comprobar empate
    for fila in tablero:
        for casilla in fila:
            if casilla == "  ":
                return   # Todavía hay casillas libres.
    return "🤝¡Empate!🤝"
    
    
    
def jugador(simbolo):
    print(f"Turno del Jugador({simbolo})")
    fila, columna = pedirMovimiento()
    #Comprueba que la posicion introducida sea un espacio en blanco.
    if tablero[fila-1][columna-1] == "  ":
        #Reemplaza en el tablero el espacio en blanco por el símbolo.
        tablero[fila-1][columna-1] = simbolo
        ganador = comprobarGanador()
        #Comprueba que si el jugador ha ganado con esa última jugada.
        if ganador:
            imprimirTablero()
            print(ganador)
            return True
        return False
    else:
        #Si no es un espacio en blanco la casilla esta ocupada.
        print("Casilla ocupada")
        return None  # Indica movimiento inválido

def maquina(simbolo):
    print(f"Turno de la Maquina({simbolo})")
    #Genera fila y columna aleatorias para el movimiento de la maquina.
    fila = random.randint(0,2)
    columna = random.randint(0,2)
    #Comprueba que la posicion generada sea un espacio en blanco.
    if tablero[fila][columna] == "  ":
        #Reemplaza en el tablero el espacio en blanco por el símbolo.
        tablero[fila][columna] = simbolo
        ganador = comprobarGanador()
        #Comprueba que si la maquina ha ganado con esa última jugada.
        if ganador:
            imprimirTablero()
            print(ganador)
            return True
        return False
    else:
        #Si no es un espacio en blanco la casilla esta ocupada.
        print("Movimiento invalido, intenta de nuevo")
        return None  # Indica movimiento inválido

def jugadorContraJugador():
    #Imprime el tablero en blanco.
    imprimirTablero()
    turno = 0
    while True:
        #Comprueba el resto de turno, si es 0 es el turno del Jugador X y si es 1 es el turno del Jugador O.
        if turno % 2 == 0:
            resultado = jugador("X")
            if resultado == True:
                break
            elif resultado == False:
                turno += 1
        elif turno % 2 == 1:
            resultado = jugador("O")
            if resultado == True:
                break
            elif resultado == False:
                turno += 1
        imprimirTablero()
    

def jugadorContraMaquina():
    #Imprime el tablero en blanco.
    imprimirTablero()
    turno = 0
    while True:
        #Comprueba el resto de turno, si es 0 es el turno del Jugador y si es 1 es el turno de la Maquina.
        if turno % 2 == 0:
            resultado = jugador("X")
            if resultado == True:
                break
            elif resultado == False:
                turno += 1
        #Turno de la Maquina.
        if turno % 2 == 1:
            resultado = maquina("O")
            if resultado == True:
                break
            elif resultado == False:
                turno += 1
        
def maquinaContraMaquina():
        #Imprime el tablero en blanco.
        imprimirTablero()
        turno = 0
        while True:
            #Comprueba el resto de turno, si es 0 es el turno de la Maquina X y si es 1 es el turno de la Maquina O.
            if turno % 2 == 0:
                resultado = maquina("X")
                if resultado == True:
                    break
                elif resultado == False:
                    turno +=1
            #Turno de la Maquina O.
            if turno % 2 == 1:
                resultado = maquina("O")
                if resultado == True:
                    break
                elif resultado == False:
                    turno +=1
        