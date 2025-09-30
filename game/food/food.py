from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, name, nutritional_value):
        self.name = name
        self.nutritional_value = nutritional_value