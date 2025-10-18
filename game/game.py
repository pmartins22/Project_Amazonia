import sys
from time import sleep
from unittest import case

from ascii_art.animal_ascii import AnimalAscii
from ascii_art.general_ascii import GeneralAscii
from ascii_art.landscape_ascii import LandScapeAscii
from game.actions.eat import start_eat
from game.actions.fish import start_fish
from game.actions.sleep import start_sleep
from game.actions.hunt import start_hunt
from game.data.save import print_player_list, has_save, load_game, save_game
from game.game_manager import GameManager
from game.player import Player
from game.player_class.fisher import Fisher
from game.player_class.hunter import Hunter
from utils.utils import Utils


def launch_game():
    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners="#")
    print("#  Welcome to Project Amazonia! #")
    print()
    Utils.draw_bar(30, "-", corners="*")
    print()
    print("1 : New Game")
    print("2 : Load Game")
    print("3 : Quit")
    print()
    Utils.draw_bar(30, "-", corners="*")
    print()
    Utils.draw_bar(125, "*", corners="#")
    print()

    choice = Utils.get_input_int(1, 3, "Enter your choice: ")

    game_manager = None

    match choice:
        case 1:
            player = create_player()
            game_manager = GameManager(player)
        case 2:
            game_manager = load_game_choice()
        case 3:
            Utils.clear_terminal()
            sys.exit(0)


    game_loop(game_manager)

def create_player():
    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners = "#")
    print("#  Welcome to Player Creation #")
    print()

    name = Utils.get_input_str(8, "Enter your name: ", invalid_enters=["return"])

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

    input("Press [ENTER] to continue...")

    return player

def load_game_choice():
    while True:
        Utils.clear_terminal()
        Utils.draw_bar(125, "*", corners="#")
        print("#  What game do you want to load? #")
        print()

        Utils.draw_bar(30, "-",label=" Saved Players List " , corners="*")
        print()
        print_player_list()
        print()
        Utils.draw_bar(30, "-", corners="*")
        print()

        Utils.draw_bar(125, "*", corners="#")
        print()

        name = Utils.get_input_str(8, """Enter player name ("return" to go back): """)
        print()

        if name == "return": launch_game()

        if has_save(name):
            print("Game loaded successfully!")
            sleep(2)
            return load_game(name)
        else:
            print("No game saved on this name! Try again.")
            sleep(2)






def game_loop(game_manager):
    while True:
        if game_manager.player.hp <= 0:
            end_game(game_manager)

        Utils.clear_terminal()

        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)
        print()

        Utils.draw_bar(30, "-", corners = "*")
        print()

        print("1 : Eat")
        print("2 : Sleep")
        print("3 : Fish")
        print("4 : Hunt")
        print()
        print("5 : Save Game")
        print("6 : Return to Menu")
        print()

        Utils.draw_bar(30, "-", corners = "*")
        print()

        choice = Utils.get_input_int(1, 6, "Enter your choice: ")
        print()

        match choice:
            case 1: start_eat(game_manager)
            case 2: start_sleep(game_manager)
            case 3: start_fish(game_manager)
            case 4: start_hunt(game_manager)
            case 5:
                save_game(game_manager)
                print("Game saved successfully!")
                sleep(2)
            case 6:
                print("Unsaved progress will be lost, are you sure?")
                print()
                Utils.draw_bar(20, "-", corners="*")
                print("1 : Yes")
                print("2 : No")
                Utils.draw_bar(20, "-", corners="*")
                print()

                choice = Utils.get_input_int(1, 2, "Enter your choice: ")
                match choice:
                    case 1: launch_game()
                    case 2: break





def end_game(game_manager):
    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners = "#")
    print(GeneralAscii.DEATH.value)
    print()
    print("YOU DIED!")
    print()
    Utils.draw_bar(30, "-", corners = "*")
    print("1 : Load Game")
    print("2 : Return to Menu")
    Utils.draw_bar(30, "-", corners = "*")
    print()
    Utils.draw_bar(125, "*", corners = "#")
    print()
    choice = Utils.get_input_int(1, 2, "Enter your choice: ")

    match choice:
        case 1:
            game_manager = load_game_choice()
            game_loop(game_manager)
        case 2: launch_game()