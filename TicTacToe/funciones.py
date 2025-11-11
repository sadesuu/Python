import random

fila = int(input("Máximo de filas del tablero: "))
columna = int(input("Máximo de columnas del tablero: "))

tablero = [[" " for _ in range(fila)] for _ in range(columna)]
#Funcion que imprime un tablero inicial
def imprimirTablero():
    print("  ", end="")
    for i in range(1, columna +1):
        print(i, end=" | ")
   
    #Recorre la longitud del array.
    for i in range(len(tablero)):
        print()
        print("-" * (columna *4 + 2))
        print(i+1, end=" ")
        #Imprime el contenido del array en la posicion inesima y añade | al final.
        for j in tablero[i]:
            print( j, end=" | ")


def pedirMovimiento():
    fil = int(input("Inserte en que fila quiere jugar: "))
    col = int(input("Inserte en que columna quiere jugar: "))
    if fil < 1 or fil > fila  or col < 1 or col > columna:
        print("Movimiento invalido, intenta de nuevo")
        return pedirMovimiento()
    return fil, col

def comprobarGanador():
    simbolos_consecutivos = 3  # Siempre se necesitan 3 para ganar
    
    # Comprobar filas
    for fila_idx in range(len(tablero)):
        for col_inicio in range(columna - simbolos_consecutivos + 1):
            # Verifica 3 casillas consecutivas en la fila
            if all(tablero[fila_idx][col_inicio + i] == tablero[fila_idx][col_inicio] and 
                   tablero[fila_idx][col_inicio] != " " 
                   for i in range(simbolos_consecutivos)):
                return f"🏆El ganador es {tablero[fila_idx][col_inicio]}🏆"
    
    # Comprobar columnas
    for col_idx in range(columna):
        for fila_inicio in range(fila - simbolos_consecutivos + 1):
            # Verifica 3 casillas consecutivas en la columna
            if all(tablero[fila_inicio + i][col_idx] == tablero[fila_inicio][col_idx] and 
                   tablero[fila_inicio][col_idx] != " " 
                   for i in range(simbolos_consecutivos)):

                return f"🏆El ganador es {tablero[fila_inicio][col_idx]}🏆"
    
    # Comprobar diagonales principales (\)
    for fila_inicio in range(fila - simbolos_consecutivos + 1):
        for col_inicio in range(columna - simbolos_consecutivos + 1):
            if all(tablero[fila_inicio + i][col_inicio + i] == tablero[fila_inicio][col_inicio] and 
                   tablero[fila_inicio][col_inicio] != " " 
                   for i in range(simbolos_consecutivos)):
                return f"🏆El ganador es {tablero[fila_inicio][col_inicio]}🏆"
    
    # Comprobar diagonales secundarias (/)
    for fila_inicio in range(fila - simbolos_consecutivos + 1):
        for col_inicio in range(simbolos_consecutivos - 1, columna):
            if all(tablero[fila_inicio + i][col_inicio - i] == tablero[fila_inicio][col_inicio] and 
                   tablero[fila_inicio][col_inicio] != " " 
                   for i in range(simbolos_consecutivos)):
                return f"🏆El ganador es {tablero[fila_inicio][col_inicio]}🏆"
    
    # Comprobar empate
    for fila_idx in range(fila):
        for col_idx in range(columna):
            if tablero[fila_idx][col_idx] == " ":
                return None  # Todavía hay casillas libres
    return "🤝¡Empate!🤝"
    
    
    
def jugador(simbolo):
    print()
    print(f"Turno del Jugador({simbolo})")
    fila, columna = pedirMovimiento()
    #Comprueba que la posicion introducida sea un espacio en blanco.
    if tablero[fila-1][columna-1] == " ":
        #Reemplaza en el tablero el espacio en blanco por el símbolo.
        tablero[fila-1][columna-1] = simbolo
        ganador = comprobarGanador()
        #Comprueba que si el jugador ha ganado con esa última jugada.
        if ganador:
            imprimirTablero()
            print()
            print(ganador)
            return True
        return False
    else:
        #Si no es un espacio en blanco la casilla esta ocupada.
        print("Casilla ocupada")
        return None  # Indica movimiento inválido

def maquina(simbolo):
    print()
    print(f"Turno de la Maquina({simbolo})")
    #Genera fila y columna aleatorias para el movimiento de la maquina.
    fil = random.randint(0,fila)
    column = random.randint(0,columna)
    #Comprueba que la posicion generada sea un espacio en blanco.
    if tablero[fil-1][column-1] == " ":
        #Reemplaza en el tablero el espacio en blanco por el símbolo.
        tablero[fil-1][column-1] = simbolo
        ganador = comprobarGanador()
        #Comprueba que si la maquina ha ganado con esa última jugada.
        if ganador:
            imprimirTablero()
            print()
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
        imprimirTablero()
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
            imprimirTablero()