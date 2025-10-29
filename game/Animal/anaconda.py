from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range


class Anaconda(Animal):
    def __init__(self):
        super().__init__("Anaconda", Range(2.5, 3.5), Range(0.06, 0.06), Range(0.03, 0.03), Range(1, 2), AnimalAscii.ANACONDA.value)