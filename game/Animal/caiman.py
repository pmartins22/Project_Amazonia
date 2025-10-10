from ascii_art.animal_ascii import AnimalAscii
from game.Animal.animal import Animal
from utils.range import Range


class Caiman(Animal):
    def __init__(self):
        super().__init__("Caiman", Range(3.5, 4.5), Range(0.1, 0.1), Range(0.2, 0.2), Range(2, 3), AnimalAscii.CAIMAN.value)