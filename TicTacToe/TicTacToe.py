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
    
def jugadorContraJugador():
    #Imprime el tablero en blanco.
    imprimirTablero()
    turno = 0
    while True:
        #Comprueba el resto de turno, si es 0 es el turno del Jugador X y si es 1 es el turno del Jugador O.
        if turno % 2 == 0:
            print("Turno del Jugador X")
            
            fila = int(input("Inserte en que fila quiere jugar(1, 2, 3): "))
            columna = int(input("Inserte en que columna quiere jugar(1, 2, 3): "))
            #Comprueba que la posicion introducida sea un espacio en blanco.
            if tablero[fila-1][columna-1] == "  ":
                #Reemplaza en el tablero el espacio en blanco por X.
                tablero[fila-1][columna-1] = "X"
                #Suma 1 al turno para cambiar el resto a 1.
                turno += 1
                ganador = comprobarGanador()
                #Comprueba que si el jugador a ganado con esa última jugada.
                if ganador:
                    imprimirTablero()
                    print(ganador)
                    break
            else:
                #Si no es un espacio en blanco la casilla esta ocupada.
                print("Casilla ocupada")
            imprimirTablero()
            #Turno de O
        elif turno % 2 == 1:
            print("Turno del Jugador O")
            #Recoge la fila y columna en la que el jugador quiere marcar.
            fila = int(input("Inserte en que fila quiere jugar(1, 2, 3): "))
            columna = int(input("Inserte en que columna quiere jugar(1, 2, 3): "))
            #Comprueba que la posicion introducida sea un espacio en blanco.
            if tablero[fila-1][columna-1] == "  ":
                #Reemplaza en el tablero el espacio en blanco por O.
                tablero[fila-1][columna-1] = "O"
                #Suma 1 al turno para cambiar el resto a 1.
                turno += 1
                ganador = comprobarGanador()
                #Comprueba que si el jugador a ganado con esa última jugada.
                if ganador:
                    imprimirTablero()
                    print(ganador)
                    break
            else:
                #Si no es un espacio en blanco la casilla esta ocupada.
                print("Casilla ocupada")
            imprimirTablero()
    

def jugadorContraMaquina():
    #Imprime el tablero en blanco.
    imprimirTablero()
    turno = 0
    while True:
        #Comprueba el resto de turno, si es 0 es el turno del Jugador y si es 1 es el turno de la Maquina.
        if turno % 2 == 0:
            print("Turno del Jugador(X)")
            #Recoge la fila y columna en la que el jugador quiere marcar.
            fila = int(input("Inserte en que fila quiere jugar(1, 2, 3): "))
            columna = int(input("Inserte en que columna quiere jugar(1, 2, 3): "))
            #Comprueba que la posicion introducida sea un espacio en blanco.
            if tablero[fila-1][columna-1] == "  ":
                #Reemplaza en el tablero el espacio en blanco por X.
                tablero[fila-1][columna-1] = "X"
                #Suma 1 al turno para cambiar el resto a 1.
                turno += 1
                ganador = comprobarGanador()
                #Comprueba que si el jugador a ganado con esa última jugada.
                if ganador:
                    imprimirTablero()
                    print(ganador)
                    break
            else:
                #Si no es un espacio en blanco la casilla esta ocupada.
                print("Movimiento invalido, intenta de nuevo")
        imprimirTablero()
        #Turno de la Maquina.
        if turno % 2 == 1:
            print("Turno de la Maquina(O)")
            #Genera fila y columna aleatorias para el movimiento de la maquina.
            fila = random.randint(0,2)
            columna = random.randint(0,2)
            #Comprueba que la posicion generada sea un espacio en blanco.
            if tablero[fila][columna] == "  ":
                #Reemplaza en el tablero el espacio en blanco por O.
                tablero[fila][columna] = "O"
                #Suma 1 al turno para cambiar el resto a 0.
                turno +=1
                ganador = comprobarGanador()
                #Comprueba que si la maquina a ganado con esa última jugada.
                if ganador:
                    imprimirTablero()
                    print(ganador)
                    break
            else:
                #Si no es un espacio en blanco la casilla esta ocupada.
                print("Movimiento invalido, intenta de nuevo")
        imprimirTablero()
        
def maquinaContraMaquina():
        #Imprime el tablero en blanco.
        imprimirTablero()
        turno = 0
        while True:
            #Comprueba el resto de turno, si es 0 es el turno de la Maquina X y si es 1 es el turno de la Maquina O.
            if turno % 2 == 0:
                print("Turno de la Maquina(X)")
                #Genera fila y columna aleatorias para el movimiento de la maquina X.
                fila = random.randint(0,2)
                columna = random.randint(0,2)
                #Comprueba que la posicion generada sea un espacio en blanco.
                if tablero[fila][columna] == "  ":
                    #Reemplaza en el tablero el espacio en blanco por X.
                    tablero[fila][columna] = "X"
                    #Suma 1 al turno para cambiar el resto a 1.
                    turno +=1
                    ganador = comprobarGanador()
                    #Comprueba que si la maquina X a ganado con esa última jugada.
                    if ganador:
                        imprimirTablero()
                        print(ganador)
                        break
                else:
                    #Si no es un espacio en blanco la casilla esta ocupada.
                    print("Movimiento invalido, intenta de nuevo")
            imprimirTablero()
            #Turno de la Maquina O.
            if turno % 2 == 1:
                print("Turno de la Maquina(O)")
                #Genera fila y columna aleatorias para el movimiento de la maquina O.
                fila = random.randint(0,2)
                columna = random.randint(0,2)
                #Comprueba que la posicion generada sea un espacio en blanco.
                if tablero[fila][columna] == "  ":
                    #Reemplaza en el tablero el espacio en blanco por O.
                    tablero[fila][columna] = "O"
                    #Suma 1 al turno para cambiar el resto a 0.
                    turno +=1
                    ganador = comprobarGanador()
                    #Comprueba que si la maquina O a ganado con esa última jugada.
                    if ganador:
                        imprimirTablero()
                        print(ganador)
                        break
                else:
                    #Si no es un espacio en blanco la casilla esta ocupada.
                    print("Movimiento invalido, intenta de nuevo")
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
        jugadorContraMaquina()
    case 3:
        maquinaContraMaquina()
    case _:
        print("Introduzca un modo valido")