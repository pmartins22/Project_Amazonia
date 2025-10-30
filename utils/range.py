# This file defines the Range class, a utility for handling numerical ranges.
# It provides methods for getting random values within the range, performing
# arithmetic operations, and serializing/deserializing the object.

import random


class Range:
    """
    Represents a numerical range with a minimum and maximum value.
    """
    def __init__(self, min, max):
        """
        Initializes a new Range instance.

        :param min: The minimum value of the range.
        :param max: The maximum value of the range.
        """
        if min > max:
            raise ValueError(f"min ({min}) must not be bigger than max ({max})")
        self.min = min
        self.max = max

    def get_average(self):
        """
        Calculates the average of the min and max values.

        :return: The average value.
        """
        return (self.min + self.max) / 2

    def get_random(self, as_int=False):
        """
        Gets a random value within the range.

        :param as_int: If True, returns a random integer; otherwise, a float.
        :return: A random number.
        :rtype: int or float
        """
        if as_int:
            return random.randint(self.min, self.max)
        return random.uniform(self.min, self.max)

    def subtract(self, other):
        """
        Subtracts another Range object from this one.

        :param other: The Range object to subtract.
        :type other: Range
        :return: A new Range object representing the result.
        :rtype: Range
        """
        return Range(self.min - other.min, self.max - other.max)

    def add(self, other):
        """
        Adds another Range object to this one.

        :param other: The Range object to add.
        :type other: Range
        :return: A new Range object representing the result.
        :rtype: Range
        """
        return Range(self.min + other.min, self.max + other.max)

    def to_dict(self):
        """
        Serializes the Range object to a dictionary.

        :return: A dictionary with 'min' and 'max' keys.
        :rtype: dict
        """
        return {"min": self.min, "max": self.max}

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Range instance from a dictionary.

        :param data: A dictionary with 'min' and 'max' keys.
        :type data: dict
        :return: A new Range instance.
        :rtype: Range
        """
        if "min" not in data or "max" not in data:
            raise KeyError("Dictionary must contain 'min' and 'max'")
        return cls(data["min"], data["max"])