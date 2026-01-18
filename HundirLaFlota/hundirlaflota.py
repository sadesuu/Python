import random

#Constantes del juego
TABLERO_SIZE = 5
VACIO = "O"  # Agua
TOCADO = "X"  # Barco tocado
AGUA = "-"  # Disparo al agua

#Símbolos de barcos
SIMBOLOS_BARCOS = {
    "Crucero": "C",
    "Submarino": "S",
    "Destructor": "D",
    "Lancha": "L"
}

#Definición de la flota: [nombre, tamaño]
FLOTA = [
    ["Crucero", 3],
    ["Submarino", 2],
    ["Destructor", 2],
    ["Lancha", 1]
]


def inicializar_tablero():
    #Crea un tablero vacío#
    return [[VACIO for _ in range(TABLERO_SIZE)] for _ in range(TABLERO_SIZE)]


def mostrar_tablero(tablero, ocultar_barcos=True, barcos=None):
    #Muestra el tablero en la consola#
    print("\n  " + " ".join(str(i) for i in range(TABLERO_SIZE)))
    for i in range(TABLERO_SIZE):
        fila = f"{i} "
        for j in range(TABLERO_SIZE):
            celda = tablero[i][j]
            
            # Si no ocultamos barcos y tenemos info de barcos, mostrar letra original
            if not ocultar_barcos and barcos and celda == TOCADO:
                # Buscar si esta posición pertenece a algún barco
                for nombre, info in barcos.items():
                    if (i, j) in info['coordenadas']:
                        fila += info['simbolo'] + " "
                        break
                else:
                    fila += celda + " "
            elif ocultar_barcos and celda in SIMBOLOS_BARCOS.values():
                fila += VACIO + " "
            else:
                fila += celda + " "
        print(fila)
    print()


def puede_colocar_barco(tablero, fila, col, tamano, horizontal):
    #Verifica si se puede colocar un barco en la posición
    if horizontal:
        if col + tamano > TABLERO_SIZE:
            return False
        for j in range(col, col + tamano):
            if tablero[fila][j] != VACIO:
                return False
    else:
        if fila + tamano > TABLERO_SIZE:
            return False
        for i in range(fila, fila + tamano):
            if tablero[i][col] != VACIO:
                return False
    return True


def colocar_barco(tablero, tamano, emoji_barco):
    #Coloca un barco aleatoriamente en el tablero
    while True:
        horizontal = random.choice([True, False])
        fila = random.randint(0, TABLERO_SIZE - 1)
        col = random.randint(0, TABLERO_SIZE - 1)
        
        if puede_colocar_barco(tablero, fila, col, tamano, horizontal):
            coordenadas = []
            if horizontal:
                for j in range(col, col + tamano):
                    tablero[fila][j] = emoji_barco
                    coordenadas.append((fila, j))
            else:
                for i in range(fila, fila + tamano):
                    tablero[i][col] = emoji_barco
                    coordenadas.append((i, col))
            return coordenadas


def inicializar_juego():
    #Inicializa el tablero y coloca los barcos
    tablero = inicializar_tablero()
    barcos = {}
    
    print("Colocando barcos...")
    for nombre, tamano in FLOTA:
        simbolo = SIMBOLOS_BARCOS[nombre]
        coordenadas = colocar_barco(tablero, tamano, simbolo)
        barcos[nombre] = {
            'tamano': tamano,
            'coordenadas': coordenadas,
            'impactos': 0,
            'simbolo': simbolo
        }
    
    return tablero, barcos


def procesar_disparo(tablero, barcos, fila, col):
    #Procesa un disparo y devuelve el resultado
    celda = tablero[fila][col]
    
    if celda == AGUA or celda == TOCADO:
        return "Ya has disparado aquí"
    
    if celda == VACIO:
        tablero[fila][col] = AGUA
        return "Agua!"
    
    if celda in SIMBOLOS_BARCOS.values():
        tablero[fila][col] = TOCADO
        
        # Buscar el barco impactado
        for nombre, info in barcos.items():
            if (fila, col) in info['coordenadas']:
                info['impactos'] += 1
                if info['impactos'] == info['tamano']:
                    return f"Hundido! ({nombre})"
                else:
                    return "Tocado!"
    
    return "Error"


def todos_hundidos(barcos):
    #Verifica si todos los barcos están hundidos
    for info in barcos.values():
        if info['impactos'] < info['tamano']:
            return False
    return True


def jugar():
    #Función principal del juego
    print("=" * 30)
    print("HUNDIR LA FLOTA")
    print("=" * 30)
    print(f"\nTablero de {TABLERO_SIZE}x{TABLERO_SIZE}")
    print("Simbolos: O=Agua, X=Tocado, -=Fallo")
    print("Introduce coordenadas como: fila,columna (ej: 2,3)\n")
    
    tablero, barcos = inicializar_juego()
    disparos = 0
    
    while not todos_hundidos(barcos):
        print(f"\n--- Disparo #{disparos + 1} ---")
        mostrar_tablero(tablero)
        
        #Pedir coordenadas
        try:
            entrada = input("Coordenadas (fila,columna): ")
            fila, col = map(int, entrada.split(','))
            
            if fila < 0 or fila >= TABLERO_SIZE or col < 0 or col >= TABLERO_SIZE:
                print("Coordenadas fuera del tablero!")
                continue
            
            # Procesar disparo
            resultado = procesar_disparo(tablero, barcos, fila, col)
            print(f">>> {resultado}")
            disparos += 1
            
        except (ValueError, IndexError):
            print("Formato incorrecto! Usa: fila,columna")
            continue
    
    #Juego terminado
    print("\n" + "=" * 30)
    print("VICTORIA!")
    print("=" * 30)
    print(f"Todos los barcos hundidos en {disparos} disparos")
    print("\nTablero final:")
    mostrar_tablero(tablero, ocultar_barcos=False, barcos=barcos)


if __name__ == "__main__":
    jugar()
