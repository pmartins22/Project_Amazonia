from game.player import Player
from utils.day_period import DayPeriod
from utils.range import Range
from utils.utils import Utils


class GameManager:
    def __init__(self, player, time=8.0, days_survived=0):
        if not isinstance(player, Player):
            raise TypeError("Player must be an instance of Player class")
        if not isinstance(time, (int, float)) or time < 0 or time >= 24:
            raise ValueError("Time must be a number between 0 and 24")
        if not isinstance(days_survived, int) or days_survived < 0:
            raise ValueError("Days survived must be a non-negative integer")

        self.player = player
        self.time = time
        self.days_survived = days_survived

    def pass_time(self, time, tax_energy=True, tax_hunger=True):
        if not isinstance(time, (int, float)) or time <= 0:
            raise ValueError("Time must be a positive number")

        self.time += time
        if self.time >= 24.0:
            self.days_survived += int(self.time // 24.0)
            self.time = self.time % 24

        tax_energy_hp = False
        energy_hp_tax = 0
        if self.player.energy < self.player.max_energy * 0.2:
            tax_energy_hp = True
            energy_hp_tax = time * Range(0.3, 0.4).get_random()
            self.player.take_damage(energy_hp_tax)

        tax_hunger_hp = False
        hunger_hp_tax = 0
        if self.player.hunger < self.player.max_hunger * 0.2:
            tax_hunger_hp = True
            hunger_hp_tax = time * Range(0.4, 0.45).get_random()
            self.player.take_damage(hunger_hp_tax)

        if tax_energy:
            self.player.take_energy(time)

        hunger_tax = time * Range(0.45, 0.65).get_random()
        if tax_hunger:
            self.player.take_hunger(hunger_tax)

        display = f"{Utils.format_time(time)} have passed: "
        if tax_energy:
            display += f"\n    * Energy lost: {Utils.format_float(time)}"
        if tax_hunger:
            display += f"\n    * Hunger tax: {Utils.format_float(hunger_tax)}"
        if tax_energy_hp:
            display += f"\n    * You're tired. HP tax: {Utils.format_float(energy_hp_tax)}"
        if tax_hunger_hp:
            display += f"\n    * You're hungry. HP tax: {Utils.format_float(hunger_hp_tax)}"

        return display

    def print_game_status(self, under_bar=False):
        Utils.draw_bar(125, "-", "Game Status: ", "*")
        print()
        print(f"                         Time: {self.get_time()}       |       "
              f"Day Period: {self.get_day_period().name}       |       "
              f"Days Survived: {self.days_survived}")
        print()
        if under_bar:
            Utils.draw_bar(125, "-", corners="*")
            print()

    def print_player_status(self, under_bar=False):
        Utils.draw_bar(125, "-", f"{self.player.name} Status: ", "*")
        print()
        print(f"               HP: {self.player.format_hp()} / {int(self.player.max_hp)}          |          "
              f"Hunger: {self.player.format_hunger()} / {int(self.player.max_hunger)}           |          "
              f"Energy: {self.player.format_energy()} / {int(self.player.max_energy)}")
        print()
        print(f"Fishing Average Delay: {self.player.format_fish_pull_delay()}       |       "
              f"Hunt Average Success Rate: {self.player.format_hunt_success_rate()}       |       "
              f"Run Average Success Rate: {self.player.format_run_success_rate()}")
        print()
        if under_bar:
            Utils.draw_bar(125, "-", corners="*")
            print()

    def print_player_inventory(self, under_bar=False):
        Utils.draw_bar(125, "-", "Player Inventory: ", "*")
        print()
        print(f"                                   Fish: {self.player.fish_amount}                 |                 "
              f"Meat: {self.player.meat_amount}")
        print()
        if under_bar:
            Utils.draw_bar(125, "-", corners="*")
            print()

    def get_time(self):
        return Utils.format_time(self.time)

    def get_day_period(self):
        if 0 <= self.time < 6:
            return DayPeriod.DAWN
        elif 6 <= self.time < 12:
            return DayPeriod.MORNING
        elif 12 <= self.time < 18:
            return DayPeriod.AFTERNOON
        else:
            return DayPeriod.NIGHT

    def to_dict(self):
        return {
            "player": self.player.to_dict(),
            "time": self.time,
            "days_survived": self.days_survived,
        }

    @classmethod
    def from_dict(cls, data):
        required_keys = ["player", "time", "days_survived"]
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            raise KeyError(f"Missing required keys: {missing_keys}")

        return cls(
            player=Player.from_dict(data["player"]),
            time=data["time"],
            days_survived=data["days_survived"]
        )