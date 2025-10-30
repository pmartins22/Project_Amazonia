# This file defines the abstract base class for all player classes in the game.
# It provides a structure for different player specializations, like Hunter or Fisher,
# and handles their serialization and deserialization.
from abc import ABC, abstractmethod


class PlayerClass(ABC):
    """
    An abstract base class for player specializations.

    This class defines the common interface for all player classes, ensuring they
    can be applied to a player to grant specific buffs and can be saved and loaded.
    """
    def __init__(self, name):
        """
        Initializes the player class.

        :param name: The name of the class (e.g., "Hunter").
        :type name: str
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        self.name = name

    @abstractmethod
    def apply_buff(self, player):
        """
        Applies the class-specific buffs to the player.

        This method must be implemented by subclasses to modify the player's
        attributes according to the class's specialization.

        :param player: The player instance to apply the buffs to.
        :type player: Player
        """
        pass

    def to_dict(self):
        """
        Serializes the player class to a dictionary.

        :return: A dictionary containing the class name.
        :rtype: dict
        """
        return {"class_name": self.name}

    @classmethod
    def from_dict(cls, data):
        """
        Creates a player class instance from a dictionary.

        This factory method reads the class name from the dictionary and returns
        an instance of the corresponding subclass.

        :param data: The dictionary containing the class data.
        :type data: dict
        :return: An instance of a PlayerClass subclass (e.g., Hunter, Fisher).
        :rtype: PlayerClass
        :raises TypeError: If data is not a dictionary.
        :raises KeyError: If 'class_name' is missing from the data.
        :raises ValueError: If the class name is unknown.
        """
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