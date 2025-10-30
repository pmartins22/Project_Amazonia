# This file serves as the main entry point and controller for the game flow.
# It handles the main menu, player creation, game loading, the primary game loop,
# and the end-game screen. It orchestrates calls to different modules based on
# player actions and game state changes.

import sys
from time import sleep

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
    """
    Displays the main menu and directs the game flow.

    This function is the initial entry point of the game. It presents the player
    with options to start a new game, load a saved game, or quit. Based on the
    player's choice, it either initiates player creation, loads a game, or exits.
    """
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

    if choice == 1:
        player = create_player()
        game_manager = GameManager(player)
    elif choice == 2:
        game_manager = load_game_choice()
    else:
        Utils.clear_terminal()
        sys.exit(0)

    game_loop(game_manager)


def create_player():
    """
    Manages the player creation process.

    Guides the player through entering a name and choosing a class (Fisher or Hunter).
    It creates a new Player instance, applies the class-specific buffs, and displays
    a confirmation screen before returning the new player object.

    :return: The newly created Player instance.
    :rtype: Player
    """
    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners="#")
    print("#  Welcome to Player Creation #")
    print()

    name = Utils.get_input_str(8, "Enter your name: ", invalid_enters=["return"])

    print()
    print("Choose your class:")
    print()
    Utils.draw_bar(30, "-", corners="*")
    print("1 : Fisher")
    print("2 : Hunter")
    Utils.draw_bar(30, "-", corners="*")
    print()
    Utils.draw_bar(125, "*", corners="#")
    print()

    choice = Utils.get_input_int(1, 2, "Enter your choice: ")

    player_class = Fisher() if choice == 1 else Hunter()
    player = Player(name, player_class)
    player.player_class.apply_buff(player)

    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners="#")
    print("#  Player Created Successfully #")
    print()
    print(f"Name: {player.name}")
    print(f"Class: {player.player_class.name}")
    print()
    Utils.draw_bar(125, "*", corners="#")
    print()

    input("Press [ENTER] to continue...")

    return player


def load_game_choice():
    """
    Manages the game loading process.

    Displays a list of saved player profiles and prompts the user to enter a name
    to load. It handles user input, validates if a save exists, and loads the
    corresponding game state. It also allows the user to return to the main menu.

    :return: A GameManager instance loaded from the selected save file.
    :rtype: GameManager
    """
    while True:
        Utils.clear_terminal()
        Utils.draw_bar(125, "*", corners="#")
        print("#  What game do you want to load? #")
        print()

        Utils.draw_bar(30, "-", label=" Saved Players List ", corners="*")
        print()
        print_player_list()
        print()
        Utils.draw_bar(30, "-", corners="*")
        print()

        Utils.draw_bar(125, "*", corners="#")
        print()

        name = Utils.get_input_str(8, """Enter player name ("return" to go back): """)
        print()

        if name == "return":
            launch_game()

        if has_save(name):
            print("Game loaded successfully!")
            sleep(2)
            return load_game(name)
        else:
            print("No game saved on this name! Try again.")
            sleep(2)


def game_loop(game_manager):
    """
    The main loop of the game.

    This function runs continuously, presenting the player with a menu of actions
    (Eat, Sleep, Fish, Hunt, Save, etc.). It captures the player's choice and
    calls the appropriate function to handle the action. It also checks for the
    player's death to trigger the end-game sequence.

    :param game_manager: The main game manager object that holds the game state.
    :type game_manager: GameManager
    """
    while True:
        if game_manager.player.hp <= 0:
            end_game(game_manager)

        Utils.clear_terminal()

        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)
        print()

        Utils.draw_bar(30, "-", corners="*")
        print()

        print("1 : Eat")
        print("2 : Sleep")
        print("3 : Fish")
        print("4 : Hunt")
        print()
        print("5 : Save Game")
        print("6 : Return to Menu")
        print()

        Utils.draw_bar(30, "-", corners="*")
        print()

        choice = Utils.get_input_int(1, 6, "Enter your choice: ")
        print()

        if choice == 1:
            start_eat(game_manager)
        elif choice == 2:
            start_sleep(game_manager)
        elif choice == 3:
            start_fish(game_manager)
        elif choice == 4:
            start_hunt(game_manager)
        elif choice == 5:
            if has_save(game_manager.player.name):
                print("Previous save on this name will be overwritten, are you sure?")
                print()
                Utils.draw_bar(20, "-", corners="*")
                print("1 : Yes")
                print("2 : No")
                Utils.draw_bar(20, "-", corners="*")
                print()

                confirm = Utils.get_input_int(1, 2, "Enter your choice: ")
                if confirm == 2:
                    continue

            save_game(game_manager)
            print("Game saved successfully!")
            sleep(2)
        else:
            print("Unsaved progress will be lost, are you sure?")
            print()
            Utils.draw_bar(20, "-", corners="*")
            print("1 : Yes")
            print("2 : No")
            Utils.draw_bar(20, "-", corners="*")
            print()

            confirm = Utils.get_input_int(1, 2, "Enter your choice: ")
            if confirm == 1:
                launch_game()


def end_game(game_manager):
    """
    Handles the end-game sequence when the player dies.

    Displays a "You Died" screen and offers the player the choice to load a
    previous game or return to the main menu.

    :param game_manager: The game manager object at the time of player death.
    :type game_manager: GameManager
    """
    Utils.clear_terminal()
    Utils.draw_bar(125, "*", corners="#")
    print(GeneralAscii.DEATH.value)
    print()
    print("YOU DIED!")
    print()
    Utils.draw_bar(30, "-", corners="*")
    print("1 : Load Game")
    print("2 : Return to Menu")
    Utils.draw_bar(30, "-", corners="*")
    print()
    Utils.draw_bar(125, "*", corners="#")
    print()

    choice = Utils.get_input_int(1, 2, "Enter your choice: ")

    if choice == 1:
        game_manager = load_game_choice()
        game_loop(game_manager)
    else:
        launch_game()