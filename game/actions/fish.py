import time
from time import sleep

from ascii_art.food_ascii import FoodAscii
from ascii_art.landscape_ascii import LandScapeAscii
from game import game_manager
from utils.range import Range
from utils.utils import Utils
import keyboard


def start_fish(game_manager):
    while True:
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
        choice = Utils.get_input_int(1, 2, "Enter your choice: ")

        if choice == 2: return

        exp_amount = None

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
            exp_amount = Range(0.005, 0.008).get_random()

        else:
            start = time.time()
            caught = False

            print(FoodAscii.FISH.value)
            while time.time() - start < game_manager.player.fish_pull_delay.get_random():
                if keyboard.is_pressed("space"):
                    game_manager.player.fish_amount += 1
                    caught = True
                    break

            if caught:
                print()
                print("You got a fish! New amount: ", game_manager.player.fish_amount)

                exp_amount = Range(0.02, 0.03).get_random()
            else:
                Utils.clear_lines_above(5)
                print()
                print("Too late!")
                exp_amount = Range(0.005, 0.008).get_random()

        sleep(2)
        print()

        game_manager.player.lvl_up_fish(exp_amount)

        print("EXP gain: " + Utils.format_float(exp_amount, 3))
        sleep(2)
        print()

        print(game_manager.pass_time(Range(0.8, 1.5).get_random()))
        print()

        input("Press [ENTER] to continue...")



