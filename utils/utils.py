import os
import sys


class Utils:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_input(min, max):
        lines_to_clear = 1

        while True:
            ipt = input("Enter choice: ")

            Utils.clear_lines_above(2)

            try:
                ipt = int(ipt)
            except ValueError:
                print("Invalid type, try again.")
                continue

            if ipt < min or ipt > max:
                print("Out of range, try again.")
                continue

            return ipt

    @staticmethod
    def clear_lines_above(amount):
        for _ in range(amount):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
        sys.stdout.flush()

