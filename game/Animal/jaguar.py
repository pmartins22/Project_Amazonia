# This file defines the Jaguar class, a specific type of Animal.
from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range


class Jaguar(Animal):
    """
    Represents the Jaguar, a formidable predator in the game.

    The Jaguar is a powerful animal with high damage and a significant challenge
    for players to hunt. It provides a substantial amount of meat when defeated.
    """

    def __init__(self):
        """
        Initializes a new Jaguar instance.

        Sets the specific attributes for the Jaguar, including its name, damage range,
        success rate taxes for hunting and running, the amount of meat it drops,
        and its ASCII art representation.
        """
        super().__init__("Jaguar", Range(4.5, 5.5), Range(0.1, 0.1), Range(0.2, 0.2), Range(3, 4), AnimalAscii.JAGUAR.value)