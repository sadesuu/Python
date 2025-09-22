jug1 = input("Piedra🪨, Papel🧻, Tijeras✂️: ").lower()
jug2 = input("Piedra🪨, Papel🧻, Tijeras✂️: ").lower()

match (jug1,jug2):
    
    case("piedra", "piedra") | ("tijera", "tijera") | ("papel", "papel"):
        print("Empate")
    
    case ("piedra", "tijeras") | ("tijeras", "papel") | ("papel", "piedra"):
        print("Jugador 1 gana")
        
    case ("tijeras", "piedra") | ("papel", "tijeras") | ("piedra", "papel"):
        print("Jugador 2 gana")

    case _:
        print("Introduzca una opción valida")