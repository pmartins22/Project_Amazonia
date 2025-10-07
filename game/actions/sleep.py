from time import sleep

from ascii_art.general_ascii import GeneralAscii
from utils.utils import Utils

def start_sleep(game_manager):
    while True:
        Utils.clear_terminal()

        print(GeneralAscii.SLEEP.value)
        print()
        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)

        Utils.draw_bar(30, "-", corners="*")
        print("Do you want to sleep now ?")
        print()
        print("1 : Yes")
        print("2 : Not yet !")
        Utils.draw_bar(30, "-", corners="*")
        print()
        choice = Utils.get_input_int(1, 2, "Enter your choice: ")

        if choice == 2: break

        hours = Utils.get_input_int(1, 48, "How many hours do you want to sleep: ")

        estimated_hunger_loss = hours * 0.55
        min_hunger_threshold = game_manager.player.max_hunger * 0.1

        if game_manager.player.hunger - estimated_hunger_loss < min_hunger_threshold:
            print("You are to much hunger for sleep this time! Eat first.")
            sleep(2)
            start_sleep(game_manager)

        print("You are sleeping...")
        sleep(2)

        game_manager.player.sleep(hours)

        print(game_manager.pass_time(hours, tax_energy=False))
        sleep(3)
