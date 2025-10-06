import sys
from time import sleep
from unittest import case

from ascii_art.animal_ascii import AnimalAscii
from ascii_art.landscape_ascii import LandScapeAscii
from game.actions.eat import start_eat
from game.actions.sleep import start_sleep
from game.actions.hunt import start_hunt
from game.game_manager import GameManager
from game.player import Player
from game.player_class.fisher import Fisher
from game.player_class.hunter import Hunter
from utils.utils import Utils


def launch_game():
    player = create_player()
    game_manager = GameManager(player)
    game_loop(game_manager)

def create_player():
    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners = "#")
    print("#  Welcome to Player Creation #")
    print()

    name = Utils.get_input_str(8, "Enter your name: ")

    print()
    print("Choose your class:")
    print()
    Utils.draw_bar(30, "-", corners = "*")
    print("1 : Fisher")
    print("2 : Hunter")
    Utils.draw_bar(30, "-", corners = "*")
    print()
    Utils.draw_bar(125, "*", corners = "#")
    print()
    choice = Utils.get_input_int(1, 2, "Enter your choice: ")

    player_class = None

    match choice:
        case 1:
            player_class = Fisher()
        case 2:
            player_class = Hunter()

    player = Player(name, player_class)
    player.player_class.apply_buff(player)



    Utils.clear_terminal()

    Utils.draw_bar(125, "*", corners = "#")
    print("#  Player Created Successfully #")
    print()
    print("Name: " + player.name)
    print("Class: " + player.player_class.name)
    print()
    Utils.draw_bar(125, "*", corners = "#")
    print()

    for i in range(5, 0, -1):
        print("Game starting in " + str(i) + " seconds...")
        sleep(1)
        Utils.clear_lines_above(1)

    return player




def game_loop(game_manager):
    while True:
        Utils.clear_terminal()

        print(LandScapeAscii.FOREST.value)
        print()
        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)

        Utils.draw_bar(30, "-", corners = "*")
        print()
        print("1 : Eat")
        print("2 : Sleep")
        print("3 : Fish")
        print("4 : Hunt")
        print("5 : Quit")
        print()
        Utils.draw_bar(30, "-", corners = "*")
        print()
        choice = Utils.get_input_int(1, 5, "Enter your choice: ")

        Utils.clear_terminal()

        match choice:
            case 1: start_eat(game_manager)
            case 2: start_sleep(game_manager)
            case 3: pass
            case 4: start_hunt(game_manager)
            case 5: Utils.clear_terminal(); sys.exit(0)





def end_game():
    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners = "#")
    print("YOU DIED! CONTINUE?")
    print()
    Utils.draw_bar(30, "-", corners = "*")
    print("1 : Continue")
    print("2 : Quit")
    Utils.draw_bar(30, "-", corners = "*")
    print()
    Utils.draw_bar(125, "*", corners = "#")
    print()
    choice = Utils.get_input_int(1, 2, "Enter your choice: ")

    match choice:
        case 1: launch_game()
        case 2: sys.exit(0)