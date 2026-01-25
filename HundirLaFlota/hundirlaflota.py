import random

#Constantes del juego
TABLERO_SIZE = 8
VACIO = "  "  # Agua
TOCADO = "💥"  # Barco tocado
AGUA = "💧"  # Disparo al agua

#Símbolos de barcos
SIMBOLOS_BARCOS = {
    "Crucero": "⛴️",
    "Velero": "⛵",
    "Destructor": "🛳️",
    "Lancha": "🚤"
}

#Definición de la flota: [nombre, tamaño]
FLOTA = [
    ["Crucero", 3],
    ["Velero", 2],
    ["Destructor", 2],
    ["Lancha", 1]
]


def inicializar_tablero():
    #Crea un tablero vacío#
    return [[VACIO for _ in range(TABLERO_SIZE)] for _ in range(TABLERO_SIZE)]


def mostrar_tablero(tablero, ocultar_barcos=True):
    #Muestra el tablero en la consola#
    print("\n    " + "  ".join(str(i) for i in range(TABLERO_SIZE)))
    separador = "  +" + "---+" * (TABLERO_SIZE - 2)
    print(separador)
    for i in range(TABLERO_SIZE):
        fila = f"{i} |"
        for j in range(TABLERO_SIZE):
            celda = tablero[i][j]
            
            if ocultar_barcos and celda in SIMBOLOS_BARCOS.values():
                fila += VACIO + "|"
            else:
                fila += celda + "|"
        print(fila)
        print(separador)
    print()


def puede_colocar_barco(tablero, fila, col, tamano, direccion):
    #Verifica si se puede colocar un barco en la posición
    if direccion:
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
        direccion = random.choice([True, False])
        fila = random.randint(0, TABLERO_SIZE - 1)
        col = random.randint(0, TABLERO_SIZE - 1)
        
        if puede_colocar_barco(tablero, fila, col, tamano, direccion):
            coordenadas = []
            if direccion:
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


def disparo_maquina(tablero, disparos_realizados):
    #La máquina realiza un disparo inteligente
    while True:
        fila = random.randint(0, TABLERO_SIZE - 1)
        col = random.randint(0, TABLERO_SIZE - 1)
        # Verificar si el disparo ya fue realizado
        ya_disparado = False
        for disparo in disparos_realizados:
            if disparo[0] == fila and disparo[1] == col:
                ya_disparado = True
                break
        if not ya_disparado:
            disparos_realizados.append((fila, col))
            return fila, col


def jugar_jugador_vs_jugador():
    #Modo Jugador vs Jugador
    print("\n=== JUGADOR vs JUGADOR ===\n")
    
    # Inicializar tableros para ambos jugadores
    print("Configurando Jugador 1...")
    tablero1, barcos1 = inicializar_juego()
    
    print("Configurando Jugador 2...")
    tablero2, barcos2 = inicializar_juego()
    
    turno = 1
    disparos1 = 0
    disparos2 = 0
    
    while not todos_hundidos(barcos1) and not todos_hundidos(barcos2):
        jugador_actual = 1 if turno % 2 == 1 else 2
        tablero_objetivo = tablero2 if jugador_actual == 1 else tablero1
        barcos_objetivo = barcos2 if jugador_actual == 1 else barcos1
        
        print(f"\n{'='*40}")
        print(f"TURNO {turno} - JUGADOR {jugador_actual}")
        print(f"{'='*40}")
        print("\nTablero enemigo:")
        mostrar_tablero(tablero_objetivo)
        
        try:
            entrada = input(f"Jugador {jugador_actual}, coordenadas (fila,columna): ")
            partes = entrada.split(',')
            fila = int(partes[0])
            col = int(partes[1])
            
            if fila < 0 or fila >= TABLERO_SIZE or col < 0 or col >= TABLERO_SIZE:
                print("Coordenadas fuera del tablero!")
                continue
            
            resultado = procesar_disparo(tablero_objetivo, barcos_objetivo, fila, col)
            print(f">>> {resultado}")
            
            if jugador_actual == 1:
                disparos1 += 1
            else:
                disparos2 += 1
            
            turno += 1
            input("\nPresiona Enter para continuar...")
            
        except (ValueError, IndexError):
            print("Formato incorrecto! Usa: fila,columna")
            continue
    
    # Determinar ganador
    print("\n" + "=" * 40)
    if todos_hundidos(barcos2):
        print("¡JUGADOR 1 GANA!")
        print(f"Disparos realizados: {disparos1}")
    else:
        print("¡JUGADOR 2 GANA!")
        print(f"Disparos realizados: {disparos2}")
    print("=" * 40)


def jugar_maquina_vs_jugador():
    #Modo Máquina vs Jugador
    print("\n=== MÁQUINA vs JUGADOR ===\n")
    
    # Tablero del jugador
    print("Configurando tu tablero...")
    tablero_jugador, barcos_jugador = inicializar_juego()
    
    # Tablero de la máquina
    print("Configurando tablero de la máquina...")
    tablero_maquina, barcos_maquina = inicializar_juego()
    
    disparos_maquina_realizados = []
    turno = 1
    disparos_jugador = 0
    disparos_maquina_count = 0
    
    while not todos_hundidos(barcos_jugador) and not todos_hundidos(barcos_maquina):
        es_turno_jugador = turno % 2 == 1
        
        if es_turno_jugador:
            print(f"\n{'='*40}")
            print(f"TURNO {turno} - TU TURNO")
            print(f"{'='*40}")
            print("\nTablero de la máquina:")
            mostrar_tablero(tablero_maquina)
            
            try:
                entrada = input("Tus coordenadas (fila,columna): ")
                partes = entrada.split(',')
                fila = int(partes[0])
                col = int(partes[1])
                
                if fila < 0 or fila >= TABLERO_SIZE or col < 0 or col >= TABLERO_SIZE:
                    print("Coordenadas fuera del tablero!")
                    continue
                
                resultado = procesar_disparo(tablero_maquina, barcos_maquina, fila, col)
                print(f">>> {resultado}")
                disparos_jugador += 1
                
            except (ValueError, IndexError):
                print("Formato incorrecto! Usa: fila,columna")
                continue
        else:
            print(f"\n{'='*40}")
            print(f"TURNO {turno} - TURNO DE LA MÁQUINA")
            print(f"{'='*40}")
            
            fila, col = disparo_maquina(tablero_jugador, disparos_maquina_realizados)
            print(f"La máquina dispara a: {fila},{col}")
            
            resultado = procesar_disparo(tablero_jugador, barcos_jugador, fila, col)
            print(f">>> {resultado}")
            disparos_maquina_count += 1
            
            print("\nTu tablero:")
            mostrar_tablero(tablero_jugador, ocultar_barcos=False)
        
        turno += 1
    
    # Determinar ganador
    print("\n" + "=" * 40)
    if todos_hundidos(barcos_maquina):
        print("¡HAS GANADO!")
        print(f"Disparos realizados: {disparos_jugador}")
    else:
        print("¡LA MÁQUINA GANA!")
        print(f"Disparos de la máquina: {disparos_maquina_count}")
    print("=" * 40)


def jugar_maquina_vs_maquina():
    #Modo Máquina vs Máquina
    print("\n=== MÁQUINA vs MÁQUINA ===\n")
    
    # Tableros
    print("Configurando Máquina 1...")
    tablero1, barcos1 = inicializar_juego()
    
    print("Configurando Máquina 2...")
    tablero2, barcos2 = inicializar_juego()
    
    disparos_maquina1 = []
    disparos_maquina2 = []
    turno = 1
    disparos1_count = 0
    disparos2_count = 0
    
    while not todos_hundidos(barcos1) and not todos_hundidos(barcos2):
        es_turno_maquina1 = turno % 2 == 1
        
        if es_turno_maquina1:
            print(f"\n{'='*40}")
            print(f"TURNO {turno} - MÁQUINA 1")
            print(f"{'='*40}")
            
            fila, col = disparo_maquina(tablero2, disparos_maquina1)
            print(f"Máquina 1 dispara a: {fila},{col}")
            
            resultado = procesar_disparo(tablero2, barcos2, fila, col)
            print(f">>> {resultado}")
            disparos1_count += 1
            
            print("\nTablero Máquina 2:")
            mostrar_tablero(tablero2)
        else:
            print(f"\n{'='*40}")
            print(f"TURNO {turno} - MÁQUINA 2")
            print(f"{'='*40}")
            
            fila, col = disparo_maquina(tablero1, disparos_maquina2)
            print(f"Máquina 2 dispara a: {fila},{col}")
            
            resultado = procesar_disparo(tablero1, barcos1, fila, col)
            print(f">>> {resultado}")
            disparos2_count += 1
            
            print("\nTablero Máquina 1:")
            mostrar_tablero(tablero1)
        
        turno += 1
    
    # Determinar ganador
    print("\n" + "=" * 40)
    if todos_hundidos(barcos2):
        print("¡MÁQUINA 1 GANA!")
        print(f"Disparos realizados: {disparos1_count}")
    else:
        print("¡MÁQUINA 2 GANA!")
        print(f"Disparos realizados: {disparos2_count}")
    print("=" * 40)


def jugar():
    #Función principal del juego con selección de modo
    print("=" * 40)
    print("HUNDIR LA FLOTA")
    print("=" * 40)
    print(f"\nTablero de {TABLERO_SIZE}x{TABLERO_SIZE}")
    print("Símbolos: O=Agua, X=Tocado, -=Fallo\n")
    
    print("Selecciona el modo de juego:")
    print("1. Jugador vs Jugador")
    print("2. Máquina vs Jugador")
    print("3. Máquina vs Máquina")
    
    while True:
        try:
            modo = int(input("\nElige una opción (1-3): "))
            if modo == 1:
                jugar_jugador_vs_jugador()
                break
            elif modo == 2:
                jugar_maquina_vs_jugador()
                break
            elif modo == 3:
                jugar_maquina_vs_maquina()
                break
            else:
                print("Opción inválida. Elige 1, 2 o 3.")
        except ValueError:
            print("Por favor, introduce un número válido.")

