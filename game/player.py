from utils.range import Range


class Player:
    def __init__(self, name, hp = 20.0, max_hp = 20.0, hunger = 20.0, max_hunger = 20.0, energy = 16.0, max_energy = 16.0, fish_pull_delay = Range(0.2, 0.9), hunt_success_rate = Range(0.25, 0.35), run_success_rate = Range(0.35, 0.5), fish_amount = 0, meat_amount = 0):
        self.name = name
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
        if self.hp <= 0:
            # Import here to avoid circular import
            from game.game import end_game
            end_game()

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def format_hp(self):
        return "{:.2f}".format(self.hp)

    def take_energy(self, energy):
        self.energy -= energy
        if self.energy <= 0:
            self.energy = 0

    def sleep(self, amount):
        self.energy += amount
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def format_energy(self):
        return "{:.2f}".format(self.energy)

    def take_hunger(self, amount):
        self.hunger -= amount
        if self.hunger <= 0:
            self.hunger = 0

    def eat(self, amount):
        self.hunger += amount
        if self.hunger > self.max_hunger:
            self.hunger = self.max_hunger

    def format_hunger(self):
        return "{:.2f}".format(self.hunger)

    def format_fish_pull_delay(self):
        return "{:.2f}".format(self.fish_pull_delay.get_average()) + "s"

    def format_hunt_success_rate(self):
        return "{:.2f}".format(self.hunt_success_rate.get_average() * 100) + "%"

    def format_run_success_rate(self):
        return "{:.2f}".format(self.run_success_rate.get_average() * 100) + "%"

