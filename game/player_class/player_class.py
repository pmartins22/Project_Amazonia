from abc import ABC, abstractmethod


class PlayerClass(ABC):
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        self.name = name

    @abstractmethod
    def apply_buff(self, player):
        # This method must be implemented by subclasses
        pass

    def to_dict(self):
        return {"class_name": self.name}

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        class_name = data.get("class_name")
        if not class_name:
            raise KeyError("Missing 'class_name' key in data")

        if class_name == "Hunter":
            from game.player_class.hunter import Hunter
            return Hunter()
        elif class_name == "Fisher":
            from game.player_class.fisher import Fisher
            return Fisher()
        else:
            raise ValueError(f"Unknown class: {class_name}")