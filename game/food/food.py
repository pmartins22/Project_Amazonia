from abc import ABC, abstractmethod

from utils.range import Range


class Food(ABC):
    def __init__(self, name, nutritional_value):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(nutritional_value, Range):
            raise TypeError("nutritional_value must be a Range object")

        self.name = name
        self.nutritional_value = nutritional_value