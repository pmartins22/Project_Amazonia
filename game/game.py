import sys
from time import sleep

from game.game_manager import GameManager
from game.player import Player
from player_class.fisher import Fisher
from player_class.hunter import Hunter
from utils.utils import Utils


def launch_game():
    player = create_player()
    game_manager = GameManager(player)
    game_loop(game_manager)

def create_player():
    Utils.clear_terminal()
    print("#***********************************************************************#")
    print("#  Welcome to Player Creation #")
    print()

    lines_to_clear = 1

    while True:
        name = input("Enter your name: ").strip()
        if not name:
            Utils.clear_lines_above(lines_to_clear)
            print("Name cannot be empty. Try again.")
            lines_to_clear = 2
            continue
        if not name.isalpha():
            Utils.clear_lines_above(lines_to_clear)
            print("Name must contain only letters. Try again.")
            lines_to_clear = 2
            continue
        break


    player = Player(name)
    print()
    print("Choose your class:")
    print()
    print("*------------------------*")
    print("1 : Fisher")
    print("2 : Hunter")
    print("*------------------------*")
    print()
    print("#***********************************************************************#")
    choice = Utils.get_input(1, 2)

    class_name = ""

    match choice:
        case 1:
            class_name = "Fisher"
            Fisher().apply_buff(player)
        case 2:
            class_name = "Hunter"
            Hunter().apply_buff(player)

    Utils.clear_terminal()

    print("#***********************************************************************#")
    print("#  Player Created Successfully #")
    print()
    print("Name: " + player.name)
    print("Class: " + class_name)
    print()
    print("#***********************************************************************#")
    print()

    for i in range(5, 0, -1):
        print("Game starting in " + str(i) + " seconds...")
        sleep(1)
        Utils.clear_lines_above(1)

    return player




def game_loop(game_manager):
    Utils.clear_terminal()
    print_game_status(game_manager)
    print_player_status(game_manager)

def print_game_status(game_manager):
    print("*Game Status: --------------------------------------------------------------------------*")
    print("Time: " + game_manager.format_time() + "       |       " +
          "Day Period: " + game_manager.get_day_period().name + "       |       " +
          "Days Survived: " + str(game_manager.days_survived))

def print_player_status(game_manager):
    print("*" + game_manager.player.name + " Status: ------------------------------------------------------------------------*")
    print("HP: " + game_manager.player.format_hp() + "       |       " +
          "Hunger: " + game_manager.player.format_hunger() + "       |       " +
          "Energy: " + game_manager.player.format_energy())
    print("*---------------------------------------------------------------------------------------*")


def end_game():
    Utils.clear_terminal()
    print("#***********************************************************************#")
    print("YOU DIED! CONTINUE?")
    print()
    print("*------------------------*")
    print("1 : Continue")
    print("2 : Quit")
    print("*------------------------*")
    print()
    print("#***********************************************************************#")
    print()
    choice = Utils.get_input(1, 2)

    match choice:
        case 1: launch_game()
        case 2: sys.exit(0)