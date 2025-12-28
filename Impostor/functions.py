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

dict_answers = {
}
def initial_questions():
    global num_players, num_rounds,num_impostors
    num_players = int(input("Introduzca el número de jugadores: "))
    num_rounds = int(input("Introduzca el número de rondas: "))
    num_impostors = int(input("Introduzca el número de impostores: "))

def create_players():
    global player_list, num_players
    for i in range(num_players):
        name_per_player = input("Introduzca el nombre para cada jugador: ")
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
    global dict_words, player_list, impostor, final_word
    word = random.choice(dict_words[""])
    for player in player_list:
        print("\n" * 10)
        if player == impostor:
            print(f"{player}, tu palabra es: ???")
        else:
            print(f"{player}, tu palabra es: {word}")
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
        print("\nRespuestas de los jugadores:")
        for player, answers in dict_answers.items():
            print(f"{player}: {answers}")

#Ejecución de los comandos
initial_questions()
create_players()
display_game_settings()
choose_impostor()
show_word()
rounds()