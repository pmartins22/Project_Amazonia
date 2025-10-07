from time import sleep

from game.food.fish import Fish
from game.food.food import Food
from game.food.meat import Meat
from utils.range import Range
from utils.utils import Utils


def start_eat(game_manager):
    while True:
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

        if choice == 3: break

        food = None
        food_amount = 0


        match choice:
            case 1:
                food = Meat()
                food_amount = game_manager.player.meat_amount

            case 2:
                food = Fish()
                food_amount = game_manager.player.fish_amount


        if food_amount <= 0:
            print(f"You don't have any {food.name}.")
            sleep(2)
            continue

        amount = Utils.get_input_int(1, food_amount, "Enter amount: ", out_of_range_msg=f"You don't have that much food (you have {food_amount}).")

        print("The player is eating...")
        sleep(2)

        nutrition = food.nutritional_value.get_random()

        if food.name == "Meat": game_manager.player.meat_amount -= amount
        if food.name == "Fish": game_manager.player.fish_amount -= amount

        sleep(0.8)
        print()
        print("Nutritional gain: " + Utils.format_float(amount * nutrition))
        sleep(0.8)
        print()
        print(game_manager.pass_time(amount * Range(0.25, 0.35).get_random()))
        game_manager.player.eat(amount * nutrition)
        sleep(6)
