# This file defines the Anaconda class, a specific type of Animal.
from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range


class Anaconda(Animal):
    """
    Represents the Anaconda, a giant snake in the game.

    The Anaconda is a dangerous predator with moderate damage and provides a
    decent amount of meat when hunted successfully.
    """

    def __init__(self):
        """
        Initializes a new Anaconda instance.

        Sets the specific attributes for the Anaconda, including its name, damage range,
        success rate taxes for hunting and running, the amount of meat it drops,
        and its ASCII art representation.
        """
        super().__init__("Anaconda", Range(2.5, 3.5), Range(0.06, 0.06), Range(0.03, 0.03), Range(1, 2), AnimalAscii.ANACONDA.value)