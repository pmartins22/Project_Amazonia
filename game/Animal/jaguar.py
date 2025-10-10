from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range


class Jaguar(Animal):
    def __init__(self):
        super().__init__("Jaguar", Range(4.5, 5.5), Range(0.1, 0.1), Range(0.2, 0.2), Range(3, 4), AnimalAscii.JAGUAR.value)