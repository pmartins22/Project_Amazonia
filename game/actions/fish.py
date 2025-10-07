import time
from time import sleep

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

        Utils.draw_bar(30, "-", corners="*")
        print("Do you want to fish now ?")
        print()
        print("1 : Yes")
        print("2 : Not yet !")
        Utils.draw_bar(30, "-", corners="*")
        choice = Utils.get_input_int(1, 2, "Enter your choice: ")

        if choice == 2: return

        print("Get ready to fish! Press [SPACE] when the bar turns GREEN.")
        time.sleep(3)
        print()

        failed = False
        duration = Range(3, 15).get_random()
        start = time.time()

        while time.time() - start < duration:
            print("\r[===== RED =====]", end="", flush=True)
            if keyboard.is_pressed("space"):
                failed = True
                break

        if failed:
            print()
            print("Too early!")
        else:
            start = time.time()
            caught = False
            while time.time() - start < game_manager.player.fish_pull_delay.get_random():
                print("\r[===== GREEN =====]", end="", flush=True)
                if keyboard.is_pressed("space"):
                    game_manager.player.fish_amount += 1
                    caught = True
                    break

            if caught:
                print()
                print("You got a fish! New amount: ", game_manager.player.fish_amount)
            else:
                print("\r[===== RED =====]", flush=True)
                print()
                print("Too late!")

        print()
        sleep(0.8)
        print(game_manager.pass_time(Range(0.80, 1.5).get_random()))
        sleep(6)



