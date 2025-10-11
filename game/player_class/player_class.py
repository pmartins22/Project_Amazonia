from abc import ABC, abstractmethod

class PlayerClass(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_buff(self, player):
        # This method must be implemented by subclasses
        pass

    def to_dict(self):
        return {"class_name": self.name}

    @classmethod
    def from_dict(cls, data):
        class_name = data.get("class_name")
        if class_name == "Hunter":
            from game.player_class.hunter import Hunter
            return Hunter()
        elif class_name == "Fisher":
            from game.player_class.fisher import Fisher
            return Fisher()
        else:
            raise ValueError(f"Unknown class: {class_name}")