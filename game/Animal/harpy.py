# This file defines the Harpy class, a specific type of Animal.
from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range

class Harpy(Animal):
    """
    Represents the Harpy Eagle, a bird of prey in the game.

    The Harpy is a relatively common but still dangerous animal. It is quicker
    to run from but offers less meat compared to larger predators.
    """
    def __init__(self):
        """
        Initializes a new Harpy instance.

        Sets the specific attributes for the Harpy, including its name, damage range,
        success rate taxes for hunting and running, the amount of meat it drops,
        and its ASCII art representation.
        """
        super().__init__("Harpy", Range(1.5, 2.5), Range(0.02, 0.02), Range(0.05, 0.05), Range(1, 1), AnimalAscii.HARPY.value)