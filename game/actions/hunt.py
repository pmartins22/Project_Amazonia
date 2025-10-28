from time import sleep

from ascii_art.landscape_ascii import LandScapeAscii
from game.Animal.animal import Animal
from game.game_manager import GameManager
from utils.range import Range
from utils.utils import Utils


def start_hunt(game_manager):
    if not isinstance(game_manager, GameManager):
        raise TypeError("game_manager must be an instance of GameManager")

    try:
        Utils.clear_terminal()

        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)

        print(LandScapeAscii.FOREST.value)
        print()

        Utils.draw_bar(30, "-", corners="*")
        print("You are now in the forest do you want to hunt ?")
        print()
        print("1 : Yes")
        print("2 : No I'm so scared !")
        Utils.draw_bar(30, "-", corners="*")
        print()

        choice = Utils.get_input_int(1, 2, "Enter your choice: ")

        if choice == 2:
            return

        Utils.clear_terminal()
        animal = Animal.get_random(game_manager.get_day_period())

        game_manager.print_game_status()
        game_manager.print_player_status()
        game_manager.print_player_inventory(under_bar=True)

        print(animal.ascii_art)
        print()

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

        if action == 1:
            print(f"You are fighting the {animal.name}...")
            sleep(2)
            print()

            success_rate = game_manager.player.hunt_success_rate.subtract(animal.hunt_success_rate_tax).get_random()
            print(f"The Success probability is {Utils.format_float(success_rate * 100, 0)}%")
            sleep(2)
            print()

            prob = Range(0, 1.0).get_random()

            if prob <= success_rate:
                print("You killed the animal!")
                sleep(2)
                print()

                meat_drop = animal.meat_drop.get_random(as_int=True)
                game_manager.player.meat_amount += meat_drop

                print(f"You got: {meat_drop} meat!")
                sleep(2)
                print()

                exp_amount = Range(0.008, 0.012).get_random()
                game_manager.player.lvl_up_hunt(exp_amount)

                print(f"EXP gain: {Utils.format_float(exp_amount, 3)}")
                sleep(2)
                print()

                print(game_manager.pass_time(Range(2, 2.7).get_random()))
            else:
                print("You lost!")
                sleep(2)
                print()

                damage = animal.damage.get_random()
                game_manager.player.take_damage(damage)

                print(f"HP lost: {Utils.format_float(damage)} HP")
                sleep(2)
                print()

                exp_amount = Range(0.002, 0.005).get_random()
                game_manager.player.lvl_up_hunt(exp_amount)

                print(f"EXP gain: {Utils.format_float(exp_amount, 3)}")
                sleep(2)
                print()

                print(game_manager.pass_time(Range(2, 2.7).get_random()))
        else:
            print(f"You are running from the {animal.name}...")
            sleep(2)
            print()

            success_rate = game_manager.player.run_success_rate.subtract(animal.run_success_rate_tax).get_random()
            print(f"The Success probability is {Utils.format_float(success_rate * 100, 0)}%")
            sleep(2)
            print()

            prob = Range(0, 1.0).get_random()

            if prob <= success_rate:
                print("You escaped successfully !")
                sleep(2)
                print()

                exp_amount = Range(0.008, 0.012).get_random()
                game_manager.player.lvl_up_run(exp_amount)

                print(f"EXP gain: {Utils.format_float(exp_amount, 3)}")
                sleep(2)
                print()

                print(game_manager.pass_time(Range(1.5, 2.0).get_random()))
            else:
                print("You couldn't escape!")
                sleep(2)
                print()

                damage = animal.damage.get_random() * 0.5
                game_manager.player.take_damage(damage)

                print(f"HP lost: {Utils.format_float(damage)} HP")
                sleep(2)
                print()

                exp_amount = Range(0.002, 0.005).get_random()
                game_manager.player.lvl_up_run(exp_amount)

                print(f"EXP gain: {Utils.format_float(exp_amount, 3)}")
                sleep(2)
                print()

                print(game_manager.pass_time(Range(2, 2.7).get_random()))

        print()
        input("Press [ENTER] to continue...")
    except (ValueError, TypeError, AttributeError) as e:
        print(f"Error during hunt action: {str(e)}")
        sleep(2)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sleep(2)