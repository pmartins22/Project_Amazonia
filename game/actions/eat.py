from time import sleep

from game.food.fish import Fish
from game.food.food import Food
from game.food.meat import Meat
from utils.range import Range
from utils.utils import Utils


def start_eat(game_manager):
    Utils.clear_terminal()

    game_manager.print_game_status()
    game_manager.print_player_status()
    game_manager.print_player_inventory(under_bar=True)

    Utils.draw_bar(30, "-", corners="*")
    print("What do you want to eat ?")
    print()
    print("1 : Meat")
    print("2 : Fish")
    Utils.draw_bar(30, "-", corners="*")
    print()
    choice = Utils.get_input_int(1, 2, "Enter your choice: ")

    food = None
    food_amount = 0
    label = ""

    match choice:
        case 1:
            food = Meat()
            food_amount = game_manager.player.meat_amount
            label = "meat"
        case 2:
            food = Fish()
            food_amount = game_manager.player.fish_amount
            label = "fish"

    if food_amount <= 0:
        print(f"You don't have any {label}.")
        sleep(2)
        start_eat(game_manager)

    amount = Utils.get_input_int(1, food_amount, "Enter amount: ",
                                 out_of_range_msg=f"You don't have that much food (you have {food_amount}).")

    print("The player is eating...")
    sleep(2)

    game_manager.player.eat(amount * food.nutritional_value)
    print("I'm full")
    sleep(0.8)
    print("Nutritional gain: " + str(amount * food.nutritional_value))
    sleep(0.8)
    print(game_manager.pass_time(amount * Range(0.25, 0.35).get_random()))
    sleep(3)
