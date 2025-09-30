import sys
from time import sleep

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

    name = Utils.get_input_str("Enter your name: ", 8)


    player = Player(name)
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
    choice = Utils.get_input_int(1, 2)

    class_name = ""

    match choice:
        case 1:
            class_name = "Fisher"
            Fisher().apply_buff(player)
        case 2:
            class_name = "Hunter"
            Hunter().apply_buff(player)

    Utils.clear_terminal()

    Utils.draw_bar(125, "*", corners = "#")
    print("#  Player Created Successfully #")
    print()
    print("Name: " + player.name)
    print("Class: " + class_name)
    print()
    Utils.draw_bar(125, "*", corners = "#")
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
    print_player_inventory(game_manager)

    Utils.draw_bar(30, "-", corners = "*")
    print("1 : Eat")
    print("2 : Sleep")
    print("3 : Fish")
    print("4 : Hunt")
    print("5 : Quit")
    Utils.draw_bar(30, "-", corners = "*")


def print_game_status(game_manager):
    Utils.draw_bar(125, "-", "Game Status: ", "*")
    print()
    print("           Time: " + game_manager.format_time() + "       |       " +
          "Day Period: " + game_manager.get_day_period().name + "       |       " +
          "Days Survived: " + str(game_manager.days_survived))
    print()

def print_player_status(game_manager):
    Utils.draw_bar(125, "-", game_manager.player.name + " Status: ", "*")
    print()
    print("           HP: " + game_manager.player.format_hp() + " / " + str(int(game_manager.player.max_hp)) + "          |          " +
          "Hunger: " + game_manager.player.format_hunger() + " / " + str(int(game_manager.player.max_hunger)) + "          |          " +
          "Energy: " + game_manager.player.format_energy() + " / " + str(int(game_manager.player.max_energy)))
    print()
    print("Fishing Average Delay: " + game_manager.player.format_fish_pull_delay() + "       |       " +
          "Hunt Success Rate: " + game_manager.player.format_hunt_success_rate() + "       |       " +
          "Run Success Rate: " + game_manager.player.format_run_success_rate())
    print()

def print_player_inventory(game_manager):
    Utils.draw_bar(125, "-", "Player Inventory: ", "*")
    print()
    print("                           Fish: " + str(game_manager.player.fish_amount) + "                 |                 " +
          "Meat: " + str(game_manager.player.meat_amount))
    print()
    Utils.draw_bar(125, "-", corners = "*")


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
    choice = Utils.get_input_int(1, 2)

    match choice:
        case 1: launch_game()
        case 2: sys.exit(0)