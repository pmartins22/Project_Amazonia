from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range

class Harpy(Animal):
    def __init__(self):
        super().__init__("Harpy", Range(1.5, 2.5), Range(0.02, 0.02), Range(0.05, 0.05), Range(1, 1), AnimalAscii.HARPY.value)