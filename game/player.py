# This file defines the Player class, which encapsulates all data and behaviors
# related to the player character. This includes stats (HP, hunger, energy),
# skills, inventory, and methods for modifying these attributes.

from game.player_class.player_class import PlayerClass
from utils.range import Range
from utils.utils import Utils


class Player:
    """
    Represents the player character in the game.

    This class holds all player-specific data, including their name, class, stats
    (health, hunger, energy), skills (fishing, hunting, running), and inventory.
    It provides methods to manage these attributes, such as taking damage, eating,
    sleeping, and leveling up skills. It also handles its own serialization and
    deserialization.
    """
    def __init__(self, name, player_class, hp=20.0, max_hp=20.0, hunger=20.0, max_hunger=20.0, energy=16.0,
                 max_energy=16.0, fish_pull_delay=Range(0.3, 0.4), hunt_success_rate=Range(0.3, 0.4),
                 run_success_rate=Range(0.35, 0.5), fish_amount=0, meat_amount=0):
        """
        Initializes a new Player instance.

        :param name: The player's name.
        :param player_class: The player's chosen specialization (e.g., Hunter, Fisher).
        :param hp: Current health points.
        :param max_hp: Maximum health points.
        :param hunger: Current hunger level.
        :param max_hunger: Maximum hunger level.
        :param energy: Current energy level.
        :param max_energy: Maximum energy level.
        :param fish_pull_delay: The time window for catching a fish.
        :param hunt_success_rate: The base success rate for hunting.
        :param run_success_rate: The base success rate for running from animals.
        :param fish_amount: The amount of fish in the inventory.
        :param meat_amount: The amount of meat in the inventory.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")

        if not isinstance(player_class, PlayerClass):
            raise ValueError("player_class must be a PlayerClass")

        if not isinstance(hp, (int, float)) or hp < 0:
            raise ValueError(f"hp must be a non-negative number, got {hp}")
        if not isinstance(max_hp, (int, float)) or max_hp <= 0:
            raise ValueError(f"max_hp must be a positive number, got {max_hp}")
        if hp > max_hp:
            raise ValueError(f"hp ({hp}) cannot be greater than max_hp ({max_hp})")

        if not isinstance(hunger, (int, float)) or hunger < 0:
            raise ValueError(f"hunger must be a non-negative number, got {hunger}")
        if not isinstance(max_hunger, (int, float)) or max_hunger <= 0:
            raise ValueError(f"max_hunger must be a positive number, got {max_hunger}")
        if hunger > max_hunger:
            raise ValueError(f"hunger ({hunger}) cannot be greater than max_hunger ({max_hunger})")

        if not isinstance(energy, (int, float)) or energy < 0:
            raise ValueError(f"energy must be a non-negative number, got {energy}")
        if not isinstance(max_energy, (int, float)) or max_energy <= 0:
            raise ValueError(f"max_energy must be a positive number, got {max_energy}")
        if energy > max_energy:
            raise ValueError(f"energy ({energy}) cannot be greater than max_energy ({max_energy})")

        if not isinstance(fish_pull_delay, Range):
            raise TypeError("fish_pull_delay must be a Range object")
        if not isinstance(hunt_success_rate, Range):
            raise TypeError("hunt_success_rate must be a Range object")
        if not isinstance(run_success_rate, Range):
            raise TypeError("run_success_rate must be a Range object")

        if not isinstance(fish_amount, int) or fish_amount < 0:
            raise ValueError(f"fish_amount must be a non-negative integer, got {fish_amount}")
        if not isinstance(meat_amount, int) or meat_amount < 0:
            raise ValueError(f"meat_amount must be a non-negative integer, got {meat_amount}")

        self.name = name
        self.player_class = player_class
        self.hp = hp
        self.max_hp = max_hp
        self.hunger = hunger
        self.max_hunger = max_hunger
        self.energy = energy
        self.max_energy = max_energy
        self.fish_pull_delay = fish_pull_delay
        self.hunt_success_rate = hunt_success_rate
        self.run_success_rate = run_success_rate
        self.fish_amount = fish_amount
        self.meat_amount = meat_amount

    def take_damage(self, damage):
        """
        Reduces the player's health by a given amount.

        HP cannot go below zero.

        :param damage: The amount of damage to inflict.
        :type damage: float
        """
        if not isinstance(damage, (int, float)) or damage < 0:
            raise ValueError("Damage must be a non-negative number")
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        """
        Increases the player's health by a given amount.

        HP cannot exceed max_hp.

        :param amount: The amount of health to restore.
        :type amount: float
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Heal amount must be a non-negative number")
        self.hp = min(self.max_hp, self.hp + amount)

    def format_hp(self):
        """
        Returns the player's current HP as a formatted string.
        """
        return Utils.format_float(self.hp)

    def take_energy(self, energy):
        """
        Reduces the player's energy by a given amount.

        Energy cannot go below zero.

        :param energy: The amount of energy to consume.
        :type energy: float
        """
        if not isinstance(energy, (int, float)) or energy < 0:
            raise ValueError("Energy must be a non-negative number")
        self.energy = max(0, self.energy - energy)

    def sleep(self, amount):
        """
        Increases the player's energy by a given amount.

        Energy cannot exceed max_energy.

        :param amount: The amount of energy to restore.
        :type amount: float
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Sleep amount must be a non-negative number")
        self.energy = min(self.max_energy, self.energy + amount)

    def format_energy(self):
        """
        Returns the player's current energy as a formatted string.
        """
        return Utils.format_float(self.energy)

    def take_hunger(self, amount):
        """
        Reduces the player's hunger by a given amount.

        Hunger cannot go below zero.

        :param amount: The amount of hunger to inflict.
        :type amount: float
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Hunger amount must be a non-negative number")
        self.hunger = max(0, self.hunger - amount)

    def eat(self, amount):
        """
        Increases the player's hunger by a given amount.

        Hunger cannot exceed max_hunger.

        :param amount: The amount of hunger to restore.
        :type amount: float
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Eat amount must be a non-negative number")
        self.hunger = min(self.max_hunger, self.hunger + amount)

    def lvl_up_fish(self, amount):
        """
        Increases the player's fishing skill.

        The skill gain is multiplied if the player has the 'Fisher' class.
        The amount is added to either the min or max of the fish_pull_delay range.

        :param amount: The base amount to increase the skill by.
        :type amount: float
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number")

        if self.player_class.name == "Fisher":
            amount *= Range(1.01, 1.8).get_random()

        prob = Range(1, 2).get_random(as_int=True)

        if prob == 1 and self.fish_pull_delay.min + amount < self.fish_pull_delay.max:
            self.fish_pull_delay.min += amount
        else:
            self.fish_pull_delay.max += amount

    def lvl_up_hunt(self, amount):
        """
        Increases the player's hunting skill.

        The skill gain is multiplied if the player has the 'Hunter' class.
        The amount is added to either the min or max of the hunt_success_rate range.

        :param amount: The base amount to increase the skill by.
        :type amount: float
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number")

        if self.player_class.name == "Hunter":
            amount *= Range(1.01, 1.8).get_random()

        prob = Range(1, 2).get_random(as_int=True)

        if prob == 1 and self.hunt_success_rate.min + amount < self.hunt_success_rate.max:
            if self.hunt_success_rate.min + amount < 1:
                self.hunt_success_rate.min += amount
        else:
            if self.hunt_success_rate.max + amount < 1:
                self.hunt_success_rate.max += amount

    def lvl_up_run(self, amount):
        """
        Increases the player's running skill.

        The skill gain is multiplied if the player has the 'Hunter' class.
        The amount is added to either the min or max of the run_success_rate range.

        :param amount: The base amount to increase the skill by.
        :type amount: float
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number")

        if self.player_class.name == "Hunter":
            amount *= Range(1.01, 1.8).get_random()

        prob = Range(1, 2).get_random(as_int=True)

        if prob == 1 and self.run_success_rate.min + amount < self.run_success_rate.max:
            if self.run_success_rate.min + amount <= 1:
                self.run_success_rate.min += amount
        else:
            if self.run_success_rate.max + amount <= 1:
                self.run_success_rate.max += amount

    def format_hunger(self):
        """
        Returns the player's current hunger as a formatted string.
        """
        return Utils.format_float(self.hunger)

    def format_fish_pull_delay(self):
        """
        Returns the player's average fish pull delay as a formatted string.
        """
        return Utils.format_float(self.fish_pull_delay.get_average()) + "s"

    def format_hunt_success_rate(self):
        """
        Returns the player's average hunt success rate as a formatted string.
        """
        return Utils.format_float(self.hunt_success_rate.get_average() * 100) + "%"

    def format_run_success_rate(self):
        """
        Returns the player's average run success rate as a formatted string.
        """
        return Utils.format_float(self.run_success_rate.get_average() * 100) + "%"

    def to_dict(self):
        """
        Serializes the Player object to a dictionary.

        :return: A dictionary representation of the player's state.
        :rtype: dict
        """
        return {
            "name": self.name,
            "player_class": self.player_class.to_dict(),
            "hp": self.hp,
            "max_hp": self.max_hp,
            "hunger": self.hunger,
            "max_hunger": self.max_hunger,
            "energy": self.energy,
            "max_energy": self.max_energy,
            "fish_pull_delay": self.fish_pull_delay.to_dict(),
            "hunt_success_rate": self.hunt_success_rate.to_dict(),
            "run_success_rate": self.run_success_rate.to_dict(),
            "fish_amount": self.fish_amount,
            "meat_amount": self.meat_amount,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Player instance from a dictionary.

        :param data: The dictionary containing the player's state.
        :type data: dict
        :return: A new Player instance.
        :rtype: Player
        :raises KeyError: If required keys are missing from the data.
        """
        required_keys = ["name", "player_class", "hp", "max_hp", "hunger", "max_hunger",
                         "energy", "max_energy", "fish_pull_delay", "hunt_success_rate",
                         "run_success_rate", "fish_amount", "meat_amount"]

        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            raise KeyError(f"Missing required keys: {missing_keys}")

        return cls(
            name=data["name"],
            player_class=PlayerClass.from_dict(data["player_class"]),
            hp=data["hp"],
            max_hp=data["max_hp"],
            hunger=data["hunger"],
            max_hunger=data["max_hunger"],
            energy=data["energy"],
            max_energy=data["max_energy"],
            fish_pull_delay=Range.from_dict(data["fish_pull_delay"]),
            hunt_success_rate=Range.from_dict(data["hunt_success_rate"]),
            run_success_rate=Range.from_dict(data["run_success_rate"]),
            fish_amount=data["fish_amount"],
            meat_amount=data["meat_amount"],
        )