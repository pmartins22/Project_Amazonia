# This file contains the logic for the fish action in the game.
import time
from time import sleep

from ascii_art.food_ascii import FoodAscii
from ascii_art.landscape_ascii import LandScapeAscii
from game.game_manager import GameManager
from utils.range import Range
from utils.utils import Utils
import keyboard


def start_fish(game_manager):
    """
    Manages the fishing minigame for the player.

    This function initiates a reaction-based minigame where the player must press a key
    at the right moment to catch a fish. It handles:
    - The player's choice to start fishing.
    - A random delay before the fish appears to test the player's reaction.
    - Checking for early or late key presses.
    - Awarding fish and experience points upon a successful catch.
    - Applying a penalty for failure.
    - Advancing the game time after the action.

    :param game_manager: The main game manager object that holds the game state.
    :type game_manager: GameManager
    :raises TypeError: If game_manager is not an instance of GameManager.
    """
    if not isinstance(game_manager, GameManager):
        raise TypeError("game_manager must be an instance of GameManager")

    try:
        Utils.clear_terminal()

        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)
        print()

        print(LandScapeAscii.LAKE.value)
        print()

        Utils.draw_bar(30, "-", corners="*")
        print("Do you want to fish now ?")
        print()
        print("1 : Yes")
        print("2 : Not yet !")
        Utils.draw_bar(30, "-", corners="*")
        print()

        choice = Utils.get_input_int(1, 2, "Enter your choice: ")

        if choice == 2:
            return

        print("Get ready to fish! Press [SPACE] when the fish shows up.")
        time.sleep(2)
        print()

        failed = False
        duration = Range(3, 15).get_random()
        start = time.time()

        while time.time() - start < duration:
            if keyboard.is_pressed("space"):
                failed = True
                break

        if failed:
            print()
            print("Too early!")
            exp_amount = Range(0.002, 0.005).get_random()
        else:
            start = time.time()
            caught = False
            fish_to_add = 1

            print(FoodAscii.FISH.value)

            while time.time() - start < game_manager.player.fish_pull_delay.get_random():
                if keyboard.is_pressed("space"):
                    if game_manager.player.player_class.name == "Fisher":
                        prob = Range(0, 1).get_random()
                        if prob < 0.075:
                            fish_to_add = 2

                    game_manager.player.fish_amount += fish_to_add
                    caught = True
                    break

            if caught:
                print()
                print(f"You got {fish_to_add} fish! New amount: {game_manager.player.fish_amount}")
                exp_amount = Range(0.008, 0.012).get_random()
            else:
                Utils.clear_lines_above(5)
                print()
                print("Too late!")
                exp_amount = Range(0.002, 0.005).get_random()

        sleep(2)
        print()

        game_manager.player.lvl_up_fish(exp_amount)

        print(f"EXP gain: {Utils.format_float(exp_amount, 3)}")
        sleep(2)
        print()

        print(game_manager.pass_time(Range(0.8, 1.5).get_random()))
        print()

        input("Press [ENTER] to continue...")
    except KeyboardInterrupt:
        print("\nFishing interrupted.")
        sleep(1)
    except (ValueError, TypeError, AttributeError) as e:
        print(f"Error during fishing action: {str(e)}")
        sleep(2)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sleep(2)