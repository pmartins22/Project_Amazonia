import os
import sys


class Utils:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_input_int(min, max, label="Enter Int: ", out_of_range_msg="Out of range, try again."):
        if min > max:
            raise ValueError(f"min ({min}) cannot be greater than max ({max})")

        lines_to_clear = 1
        while True:
            ipt = input(label)
            Utils.clear_lines_above(lines_to_clear)
            lines_to_clear = 2

            try:
                ipt = int(ipt)
                if min <= ipt <= max:
                    return ipt
                print(out_of_range_msg)
            except ValueError:
                print("Invalid type, try again.")

    @staticmethod
    def get_input_str(max, label="Enter Text: ", invalid_enters=[]):
        if not isinstance(invalid_enters, list) or not all(isinstance(i, str) for i in invalid_enters):
            raise TypeError("invalid_enters must be a list of strings")

        lines_to_clear = 1
        while True:
            ipt = input(label).strip()
            Utils.clear_lines_above(lines_to_clear)
            lines_to_clear = 2

            if not ipt:
                print("Input cannot be empty. Try again.")
            elif not ipt.isalpha():
                print("Input must contain only letters. Try again.")
            elif len(ipt) > max:
                print(f"Input max size is {max}. Try again.")
            elif ipt in invalid_enters:
                print("Input is invalid. Try again.")
            else:
                return ipt

    @staticmethod
    def clear_lines_above(amount):
        for _ in range(amount):
            sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

    @staticmethod
    def draw_bar(size, tile, label="", corners=""):
        if size <= 0:
            raise ValueError(f"Size must be positive, got {size}.")

        min_size = len(label) + 2 * len(corners)
        if size < min_size:
            raise ValueError(f"Size too small! Must be at least {min_size}, got {size}.")

        print(f"{corners}{label}{tile * (size - len(label) - 2 * len(corners))}{corners}")

    @staticmethod
    def format_time(time):
        if not isinstance(time, (int, float)):
            raise TypeError("Time must be a number.")
        if time < 0:
            raise ValueError("Time cannot be negative.")
        if time >= 24:
            raise ValueError("Time cannot be greater or equal to 24 hours.")

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