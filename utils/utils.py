import os
import sys


class Utils:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_input_int(min, max, label = "Enter Int: ", out_of_range_msg = "Out of range, try again."):
        lines_to_clear = 1
        while True:
            ipt = input(label)

            Utils.clear_lines_above(lines_to_clear)
            lines_to_clear = 2

            try:
                ipt = int(ipt)
            except ValueError:
                print("Invalid type, try again.")
                continue

            if ipt < min or ipt > max:
                print(out_of_range_msg)
                continue

            return ipt

    @staticmethod
    def get_input_str(max, label = "Enter Text: ", invalid_enters = []):
        if not isinstance(invalid_enters, list) or not all(isinstance(i, str) for i in invalid_enters):
            raise TypeError("invalid_enters must be a list of strings")

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
            if ipt in invalid_enters:
                Utils.clear_lines_above(lines_to_clear)
                print("Input is invalid. Try again.")
                lines_to_clear = 2
                continue
            return ipt

    @staticmethod
    def clear_lines_above(amount):
        for _ in range(amount):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
        sys.stdout.flush()

    @staticmethod
    def draw_bar(size, tile, label = "", corners = ""):
        min_size = len(label) + 2 * len(corners)
        if size < min_size:
            raise ValueError(f"Size too small! Must be at least {min_size}, got {size}.")

        result = ""
        result += corners + label
        result += tile * (size - len(label) - (2*len(corners)))
        result += corners

        print(result)

    @staticmethod
    def format_time(time):
        hours = int(time)
        minutes = int((time - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"

    @staticmethod
    def format_float(value, decimals=2):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        if not isinstance(decimals, int) or decimals < 0:
            raise ValueError("Decimals must be a non-negative integer.")

        return f"{value:.{decimals}f}"




