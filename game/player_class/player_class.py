from abc import ABC, abstractmethod

class PlayerClass(ABC):

    @abstractmethod
    def apply_buff(self, player):
        # This method must be implemented by subclasses
        pass

