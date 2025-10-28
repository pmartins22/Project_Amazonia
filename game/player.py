from game.player_class.player_class import PlayerClass
from utils.range import Range
from utils.utils import Utils


class Player:
    def __init__(self, name, player_class, hp=20.0, max_hp=20.0, hunger=20.0, max_hunger=20.0, energy=16.0,
                 max_energy=16.0, fish_pull_delay=Range(0.3, 0.4), hunt_success_rate=Range(0.3, 0.4),
                 run_success_rate=Range(0.35, 0.5), fish_amount=0, meat_amount=0):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if hp > max_hp or hp < 0:
            raise ValueError(f"HP ({hp}) must be between 0 and max_hp ({max_hp})")
        if hunger > max_hunger or hunger < 0:
            raise ValueError(f"Hunger ({hunger}) must be between 0 and max_hunger ({max_hunger})")
        if energy > max_energy or energy < 0:
            raise ValueError(f"Energy ({energy}) must be between 0 and max_energy ({max_energy})")

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
        if not isinstance(damage, (int, float)) or damage < 0:
            raise ValueError("Damage must be a non-negative number")
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Heal amount must be a non-negative number")
        self.hp = min(self.max_hp, self.hp + amount)

    def format_hp(self):
        return Utils.format_float(self.hp)

    def take_energy(self, energy):
        if not isinstance(energy, (int, float)) or energy < 0:
            raise ValueError("Energy must be a non-negative number")
        self.energy = max(0, self.energy - energy)

    def sleep(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Sleep amount must be a non-negative number")
        self.energy = min(self.max_energy, self.energy + amount)

    def format_energy(self):
        return Utils.format_float(self.energy)

    def take_hunger(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Hunger amount must be a non-negative number")
        self.hunger = max(0, self.hunger - amount)

    def eat(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Eat amount must be a non-negative number")
        self.hunger = min(self.max_hunger, self.hunger + amount)

    def lvl_up_fish(self, amount):
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
        return Utils.format_float(self.hunger)

    def format_fish_pull_delay(self):
        return Utils.format_float(self.fish_pull_delay.get_average()) + "s"

    def format_hunt_success_rate(self):
        return Utils.format_float(self.hunt_success_rate.get_average() * 100) + "%"

    def format_run_success_rate(self):
        return Utils.format_float(self.run_success_rate.get_average() * 100) + "%"

    def to_dict(self):
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