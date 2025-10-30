# This file defines the Meat class, a specific type of Food.

from game.food.food import Food
from utils.range import Range


class Meat(Food):
    """
    Represents meat, a type of food obtained from hunting.

    Meat provides a high nutritional value compared to other food sources.
    """

    def __init__(self):
        """
        Initializes a new Meat instance.

        Sets the specific nutritional value range for meat.
        """
        super().__init__("Meat", Range(1.8, 2.5))