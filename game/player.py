from utils.range import Range
from utils.utils import Utils


class Player:
    def __init__(self, name, player_class, hp = 20.0, max_hp = 20.0, hunger = 20.0, max_hunger = 20.0, energy = 16.0, max_energy = 16.0, fish_pull_delay = Range(0.2, 0.4), hunt_success_rate = Range(0.25, 0.35), run_success_rate = Range(0.35, 0.5), fish_amount = 0, meat_amount = 0):
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
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def format_hp(self):
        return "{:.2f}".format(self.hp)

    def take_energy(self, energy):
        self.energy -= energy
        if self.energy < 0:
            self.energy = 0


    def sleep(self, amount):
        self.energy += amount
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def format_energy(self):
        return "{:.2f}".format(self.energy)

    def take_hunger(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0


    def eat(self, amount):
        self.hunger += amount
        if self.hunger > self.max_hunger:
            self.hunger = self.max_hunger

    def lvl_up_fish(self, amount):
        if self.player_class.name == "Fisher":
            amount *= Range(1.01, 1.8).get_random()

        range_to_add = Range(0,0)

        prob = Range(1,2).get_random(as_int=True)

        if prob == 1 and self.fish_pull_delay.min + amount < self.fish_pull_delay.max:
            range_to_add.min += amount
        else:
            range_to_add.max += amount

        self.fish_pull_delay = self.fish_pull_delay.add(range_to_add)

    def lvl_up_hunt(self, amount):
        if self.player_class.name == "Hunter":
            amount *= Range(1.01, 1.8).get_random()

        range_to_add = Range(0,0)

        prob = Range(1,2).get_random(as_int=True)
        if prob == 1 and self.hunt_success_rate.min + amount < self.hunt_success_rate.max:
            if self.hunt_success_rate.min + amount < 1: range_to_add.min += amount
        else:
            if self.hunt_success_rate.min + amount < 1: range_to_add.max += amount

        self.hunt_success_rate = self.hunt_success_rate.add(range_to_add)

    def lvl_up_run(self, amount):
        if self.player_class.name == "Hunter":
            amount *= Range(1.01, 1.8).get_random()

        range_to_add = Range(0, 0)

        prob = Range(1, 2).get_random(as_int=True)
        if prob == 1 and self.run_success_rate.min + amount < self.run_success_rate.max:
            if self.run_success_rate.min + amount <= 1: range_to_add.min += amount
        else:
            if self.run_success_rate.max + amount <= 1: range_to_add.max += amount

        self.run_success_rate = self.run_success_rate.add(range_to_add)

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
            "player_class": self.player_class,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "hunger": self.hunger,
            "max_hunger": self.max_hunger,
            "energy": self.energy,
            "max_energy": self.max_energy,
            "fish_pull_delay": self.fish_pull_delay.to_dict() if self.fish_pull_delay else None,
            "hunt_success_rate": self.hunt_success_rate.to_dict() if self.hunt_success_rate else None,
            "run_success_rate": self.run_success_rate.to_dict() if self.run_success_rate else None,
            "fish_amount": self.fish_amount,
            "meat_amount": self.meat_amount,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            player_class=data["player_class"],
            hp=data["hp"],
            max_hp=data["max_hp"],
            hunger=data["hunger"],
            max_hunger=data["max_hunger"],
            energy=data["energy"],
            max_energy=data["max_energy"],
            fish_pull_delay=Range.from_dict(data["fish_pull_delay"]) if data["fish_pull_delay"] else None,
            hunt_success_rate=Range.from_dict(data["hunt_success_rate"]) if data["hunt_success_rate"] else None,
            run_success_rate=Range.from_dict(data["run_success_rate"]) if data["run_success_rate"] else None,
            fish_amount=data["fish_amount"],
            meat_amount=data["meat_amount"],
        )

