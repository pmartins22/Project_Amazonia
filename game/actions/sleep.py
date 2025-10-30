# This file contains the logic for the sleep action in the game.
from time import sleep

from ascii_art.general_ascii import GeneralAscii
from game.game_manager import GameManager
from utils.range import Range
from utils.utils import Utils


def start_sleep(game_manager):
    """
    Manages the sleeping action for the player.

    This function allows the player to sleep for a specified number of hours to recover
    health and energy. It handles:
    - The player's choice to sleep.
    - Input for the duration of sleep.
    - Checking if the player is too hungry to sleep.
    - Calculating the amount of health and energy restored.
    - Updating the player's stats and advancing game time accordingly.

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

        print(GeneralAscii.SLEEP.value)
        print()

        Utils.draw_bar(30, "-", corners="*")
        print("Do you want to sleep now ?")
        print()
        print("1 : Yes")
        print("2 : Not yet !")
        Utils.draw_bar(30, "-", corners="*")
        print()

        choice = Utils.get_input_int(1, 2, "Enter your choice: ")

        if choice == 2:
            return

        hours = Utils.get_input_int(1, 48, "How many hours do you want to sleep: ")

        estimated_hunger_loss = hours * 0.55
        min_hunger_threshold = game_manager.player.max_hunger * 0.1

        if game_manager.player.hunger - estimated_hunger_loss < min_hunger_threshold:
            print("You are too hungry to sleep now! Eat first.")
            sleep(2)
            return

        print("You are sleeping...")
        sleep(2)
        print()

        print("You have woken up!")
        sleep(2)
        print()

        heal_amount = hours * Range(0.45, 0.65).get_random()

        print(f"energy gain: {hours}")
        print(f"HP gain: {Utils.format_float(heal_amount)}")
        sleep(2)
        print()

        game_manager.player.sleep(hours)
        game_manager.player.heal(heal_amount)
        print(game_manager.pass_time(hours, tax_energy=False))
        print()

        input("Press [ENTER] to continue...")
    except (ValueError, TypeError, AttributeError) as e:
        print(f"Error during sleep action: {str(e)}")
        sleep(2)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sleep(2)