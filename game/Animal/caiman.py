# This file defines the Caiman class, a specific type of Animal.
from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range


class Caiman(Animal):
    """
    Represents the Caiman, a crocodilian reptile in the game.

    The Caiman is a strong animal, often found near water. It poses a
    significant threat and rewards the player with a good amount of meat.
    """

    def __init__(self):
        """
        Initializes a new Caiman instance.

        Sets the specific attributes for the Caiman, including its name, damage range,
        success rate taxes for hunting and running, the amount of meat it drops,
        and its ASCII art representation.
        """
        super().__init__("Caiman", Range(3.5, 4.5), Range(0.075, 0.075), Range(0.02, 0.02), Range(2, 3), AnimalAscii.CAIMAN.value)