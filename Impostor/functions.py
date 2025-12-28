import random

num_players = 0
name_per_player = ""
num_rounds = 0
num_impostors = 1
player_list = []

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
    global player_list, num_impostors
    impostors = random.sample(player_list, num_impostors)
    print("Impostor(es) seleccionado(s):")
    for impostor in impostors:
        print(impostor)




initial_questions()
create_players()
display_game_settings()
choose_impostor()