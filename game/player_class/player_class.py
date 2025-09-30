from abc import ABC, abstractmethod

class PlayerClass(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_buff(self, player):
        # This method must be implemented by subclasses
        pass

