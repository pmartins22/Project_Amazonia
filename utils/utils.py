# This file provides a collection of static utility methods used across the
# application. These helpers handle common tasks such as terminal manipulation,
# user input validation, UI drawing, and data formatting.

import os
import sys


class Utils:
    """
    A collection of static utility methods for common tasks.
    """
    @staticmethod
    def clear_terminal():
        """
        Clears the console screen.

        Works on both Windows ('cls') and Unix-based systems ('clear').
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_input_int(min, max, label="Enter Int: ", out_of_range_msg="Out of range, try again."):
        """
        Prompts the user for an integer input within a specified range.

        Continuously prompts until a valid integer is entered.

        :param min: The minimum acceptable value (inclusive).
        :param max: The maximum acceptable value (inclusive).
        :param label: The message to display to the user.
        :param out_of_range_msg: The message to display if the input is out of range.
        :return: The validated integer input from the user.
        :rtype: int
        """
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
        """
        Prompts the user for a non-empty, alphabetic string input.

        Continuously prompts until a valid string is entered.

        :param max: The maximum allowed length of the string.
        :param label: The message to display to the user.
        :param invalid_enters: A list of strings that are not allowed as input.
        :return: The validated string input from the user.
        :rtype: str
        """
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
        """
        Clears a specified number of lines above the current cursor position.

        Uses ANSI escape codes to move the cursor up and clear the line.

        :param amount: The number of lines to clear.
        :type amount: int
        """
        for _ in range(amount):
            sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

    @staticmethod
    def draw_bar(size, tile, label="", corners=""):
        """
        Prints a decorative bar to the console.

        :param size: The total width of the bar.
        :param tile: The character used to fill the bar.
        :param label: An optional label to display within the bar.
        :param corners: Optional characters to use for the ends of the bar.
        """
        if size <= 0:
            raise ValueError(f"Size must be positive, got {size}.")

        min_size = len(label) + 2 * len(corners)
        if size < min_size:
            raise ValueError(f"Size too small! Must be at least {min_size}, got {size}.")

        print(f"{corners}{label}{tile * (size - len(label) - 2 * len(corners))}{corners}")

    @staticmethod
    def format_time(time):
        """
        Formats a float representing hours into a HH:MM string.

        :param time: The time in hours (e.g., 8.5 for 08:30).
        :type time: float
        :return: The formatted time string.
        :rtype: str
        """
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
        """
        Formats a float or int to a string with a specific number of decimal places.

        :param value: The number to format.
        :param decimals: The number of decimal places to include.
        :return: The formatted number as a string.
        :rtype: str
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        if not isinstance(decimals, int) or decimals < 0:
            raise ValueError("Decimals must be a non-negative integer.")

        return f"{value:.{decimals}f}"