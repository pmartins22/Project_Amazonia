# This file defines the abstract base class for all food items in the game.
# It provides a common structure for different types of food, like Meat and Fish.

from abc import ABC

from utils.range import Range


class Food(ABC):
    """
    An abstract base class for all food items.

    This class defines the common attributes for food, such as its name and
    nutritional value.
    """

    def __init__(self, name, nutritional_value):
        """
        Initializes a new food item.

        :param name: The name of the food (e.g., "Meat").
        :type name: str
        :param nutritional_value: The range of nutritional value the food provides.
        :type nutritional_value: Range
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(nutritional_value, Range):
            raise TypeError("nutritional_value must be a Range object")

        self.name = name
        self.nutritional_value = nutritional_value