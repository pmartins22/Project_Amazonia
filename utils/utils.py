import os
import sys


class Utils:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_input_int(min, max):
        lines_to_clear = 1
        while True:
            ipt = input("Enter choice: ")

            Utils.clear_lines_above(lines_to_clear)
            lines_to_clear = 2

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
    def get_input_str(label ,max):
        lines_to_clear = 1

        while True:
            ipt = input(label).strip()
            if not ipt:
                Utils.clear_lines_above(lines_to_clear)
                print("Input cannot be empty. Try again.")
                lines_to_clear = 2
                continue
            if not ipt.isalpha():
                Utils.clear_lines_above(lines_to_clear)
                print("Input must contain only letters. Try again.")
                lines_to_clear = 2
                continue
            if len(ipt) > max:
                Utils.clear_lines_above(lines_to_clear)
                print("Input max size is " + str(max) + ". Try again.")
                lines_to_clear = 2
                continue
            return ipt

    @staticmethod
    def clear_lines_above(amount):
        for _ in range(amount):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
        sys.stdout.flush()

