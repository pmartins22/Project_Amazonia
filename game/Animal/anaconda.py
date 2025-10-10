from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range


class Anaconda(Animal):
    def __init__(self):
        super().__init__("Anaconda", Range(2.5, 3.5), Range(0.1, 0.1), Range(0.2, 0.2), Range(1, 2), AnimalAscii.ANACONDA.value)