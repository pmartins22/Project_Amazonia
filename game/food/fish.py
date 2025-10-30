# This file defines the Fish class, a specific type of Food.
from game.food.food import Food
from utils.range import Range


class Fish(Food):
    """
    Represents fish, a type of food obtained from fishing.

    Fish provides a moderate nutritional value.
    """
    def __init__(self):
        """
        Initializes a new Fish instance.

        Sets the specific nutritional value range for fish.
        """
        super().__init__("Fish", Range(0.8, 1.5))