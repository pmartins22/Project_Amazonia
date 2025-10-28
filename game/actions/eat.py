from time import sleep

from ascii_art.food_ascii import FoodAscii
from game.food.fish import Fish
from game.food.meat import Meat
from game.game_manager import GameManager
from utils.range import Range
from utils.utils import Utils


def start_eat(game_manager):
    if not isinstance(game_manager, GameManager):
        raise TypeError("game_manager must be an instance of GameManager")

    try:
        Utils.clear_terminal()

        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)

        Utils.draw_bar(30, "-", corners="*")
        print("What do you want to eat ?")
        print()
        print("1 : Meat")
        print("2 : Fish")
        print("3 : Not yet !")
        Utils.draw_bar(30, "-", corners="*")
        print()

        choice = Utils.get_input_int(1, 3, "Enter your choice: ")

        if choice == 3:
            return

        if choice == 1:
            food = Meat()
            food_amount = game_manager.player.meat_amount
            ascii_art = FoodAscii.MEAT.value
        else:
            food = Fish()
            food_amount = game_manager.player.fish_amount
            ascii_art = FoodAscii.FISH.value

        if food_amount <= 0:
            print(f"You don't have any {food.name}.")
            sleep(2)
            return

        print(ascii_art)
        print()

        amount = Utils.get_input_int(1, food_amount, "Enter amount: ",
                                     out_of_range_msg=f"You don't have that much food (you have {food_amount}).")

        print("You are eating...")
        sleep(2)
        print()

        print("You finished eating!")
        sleep(2)
        print()

        nutrition = food.nutritional_value.get_random()
        heal_amount = nutrition * amount * Range(0.85, 0.95).get_random()

        if food.name == "Meat":
            game_manager.player.meat_amount -= amount
        elif food.name == "Fish":
            game_manager.player.fish_amount -= amount

        print(f"Nutritional gain: {Utils.format_float(amount * nutrition)}")
        print(f"HP gain: {Utils.format_float(heal_amount)}")
        sleep(2)
        print()

        game_manager.player.eat(amount * nutrition)
        game_manager.player.heal(heal_amount)
        print(game_manager.pass_time(amount * Range(0.25, 0.35).get_random(), tax_hunger=False))
        print()

        input("Press [ENTER] to continue...")
    except (ValueError, TypeError, AttributeError) as e:
        print(f"Error during eat action: {str(e)}")
        sleep(2)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sleep(2)