import random

num_players = 0
name_per_player = ""
num_rounds = 0
num_impostors = 1
player_list = []
impostor = ""
final_word = ""

dict_words = {
    "": ["gato", "perro", "casa", "árbol", "coche", "libro", "ciudad", "mar", "montaña", "río", "sol", "luna", "estrella", "flor", "bosque", "playa", "nieve", "fuego", "agua", "viento"],
}

dict_hints = {
    "gato": "Animal doméstico que maúlla",
    "perro": "Animal doméstico que ladra",
    "casa": "Lugar donde vives",
    "árbol": "Planta grande con tronco y hojas",
    "coche": "Vehículo con ruedas que usas para viajar",
    "libro": "Objeto con páginas que lees",
    "ciudad": "Lugar grande donde vive mucha gente",
    "mar": "Gran masa de agua salada",
    "montaña": "Elevación natural del terreno",
    "río": "Corriente de agua que fluye",
    "sol": "Estrella que ilumina nuestro planeta",
    "luna": "Cuerpo celeste que orbita la Tierra",
    "estrella": "Cuerpo celeste que brilla en el cielo nocturno",
    "flor": "Parte colorida de una planta",
    "bosque": "Gran área cubierta de árboles",
    "playa": "Zona de arena junto al mar",
    "nieve": "Agua congelada que cae del cielo en invierno",
    "fuego": "Reacción química que produce calor y luz",
    "agua": "Líquido transparente esencial para la vida",
    "viento": "Movimiento del aire"
}

dict_answers = {
}

votes = {
}
def initial_questions():
    global num_players, num_rounds,num_impostors
    num_players = int(input("Introduzca el número de jugadores: "))
    num_rounds = int(input("Introduzca el número de rondas: "))
    num_impostors = int(input("Introduzca el número de impostores: "))

def create_players():
    global player_list, num_players
    for i in range(num_players):
        name_per_player = input("Introduzca el nombre para cada jugador: ").lower()
        player_list.append(name_per_player)

def display_players():
    for player in player_list:
        print(f"Jugador: {player}")

def display_game_settings():
    print(f"Número de jugadores: {num_players}")
    print(f"Número de rondas: {num_rounds}")
    print("Jugadores:")
    display_players()

def choose_impostor():
    global player_list, num_impostors, impostor
    if num_impostors >= len(player_list):
        print("No puede haber igual o más impostores que jugadores.")
    else:
        impostors = random.sample(player_list, num_impostors)

    print("Impostor(es) seleccionado(s):")
    for impost in impostors:
        impostor = impost
        print(impost)


def show_word():
    global dict_words, player_list, impostor, final_word, dict_hints
    word = random.choice(dict_words[""])
    for player in player_list:
        print("\n" * 15)
        if player == impostor:
            for player_hint, hint in dict_hints.items():
                if player_hint == word:
                    print(f"Pista para el impostor: {hint}")
                    break
            print(f"{player}, eres el impostor. No tienes palabra asignada.")
        else:
            print(f"{player}, tu palabra es: {word}")
        input("Pulsa enter para pasar a la siguiente persona...")
    final_word = word
        
def rounds():
    global num_rounds, player_list, dict_answers
    for player in player_list:
        if player not in dict_answers:
            dict_answers[player] = []
    
    for round_number in range(1, num_rounds + 1):
        print(f"\n--- Ronda {round_number} ---")
        for player in player_list:
            print(f"\nTurno de {player}:")
            answer = input("Elija una palabra para describir la palabra secreta: ")
            dict_answers[player].append(answer)
def voting():
    global player_list, votes

    print("\nRespuestas recopiladas:")
    for player, answers in dict_answers.items():
        print(f"{player}: {', '.join(answers)}")

    print("\n--- Votación para descubrir al impostor ---")
    for player in player_list:
    
        flag = True
        while flag:
            vote = input(f"{player}, ¿a quién acusas de ser el impostor? ").lower()
            if vote not in player_list:
                print("Jugador no válido. Inténtalo de nuevo.")
            else:
                if vote != player:
                    if vote in votes:
                        votes[vote] += 1
                    else:
                        votes[vote] = 1
                    flag = False
                else:
                    print("No puedes votarte a ti mismo.")


def display_votes():
    global votes
    print("\nResultados de la votación:")
    for player, count in votes.items():
        print(f"{player}: {count} votos")

def reveal_impostor():
    global impostor
    print(f"\nEl impostor era: {impostor}")

def reveal_word():
    global final_word
    print(f"\nLa palabra secreta era: {final_word}")

def get_voted():
    global votes
    max_votes = -1
    voted_player = ""
    for player, count in votes.items():
        if count > max_votes:
            max_votes = count
            voted_player = player
    return voted_player      

def check_tie():
    global votes
    vote_counts = list(votes.values())
    if vote_counts.count(max(vote_counts)) > 1:
        return True
    return False    

def check_winner():
    global impostor
    voted_player = get_voted()
    if voted_player == impostor:
        print("Los jugadores han ganado! Han descubierto al impostor.")
    else:
        print("El impostor ha ganado! No han descubierto al impostor.")

def game():
    initial_questions()
    create_players()
    choose_impostor()
    display_game_settings()
    show_word()
    rounds()
    voting()
    display_votes()
    check_tie()
    if check_tie():
        print("\nHa habido un empate en la votación. No hay ganador esta ronda.")
    voted_player = get_voted()
    print(f"\nEl jugador con más votos es: {voted_player}")
    check_winner()
    reveal_impostor()
    reveal_word()


def main():
    game()