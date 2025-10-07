from time import sleep

from utils.utils import Utils
from game.Animal.animal import Animal

def start_hunt(game_manager):
    Utils.clear_terminal()

    game_manager.print_game_status()
    game_manager.print_player_status()
    game_manager.print_player_inventory(under_bar=True)

    Utils.draw_bar(30, "-", corners="*")
    print("You are now in the forest do you want to hunt ?")
    print()
    print("1 : Yes")
    print("2 : No I'm so scared !")
    Utils.draw_bar(30, "-", corners="*")
    print()
    choice = Utils.get_input_int(1, 2, "Enter your choice: ")

    match choice:
        case 1:
            animal = Animal.get_random(game_manager.get_day_period())

            Utils.clear_terminal()
            game_manager.print_game_status()
            game_manager.print_player_status()
            game_manager.print_player_inventory(under_bar=True)

            Utils.draw_bar(30, "-", corners="*")
            print(f"A wild {animal.name} appears!")
            print()
            print("What do you want to do ?")
            print()
            print("1 : Fight")
            print("2 : Run away")
            Utils.draw_bar(30, "-", corners="*")
            print()
            action = Utils.get_input_int(1, 2, "Enter your choice: ")

            match action:
                case 1:

                    print("You fight the animal!")
                    sleep(2)
                case 2:

                    print("You run away!")
                    sleep(2)
                    return
        case 2:
            return