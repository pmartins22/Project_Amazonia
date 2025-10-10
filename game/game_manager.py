from utils.day_period import DayPeriod
from utils.range import Range
from utils.utils import Utils


class GameManager:
    def __init__(self, player, time = 8.0, days_survived = 0):
        self.player = player
        self.time = time
        self.days_survived = days_survived

    def pass_time(self, time, tax_energy = True):
        self.time += time
        if self.time >= 24.0:
            self.days_survived += int(self.time // 24.0)
            self.time = self.time % 24


        if tax_energy: self.player.take_energy(time)

        hunger_tax = time * Range(0.45, 0.65).get_random()
        self.player.take_hunger(hunger_tax)

        tax_energy_hp = False
        energy_hp_tax = time * Range(0.3, 0.4).get_random()
        tax_hunger_hp = False
        hunger_hp_tax = time * Range(0.4, 0.45).get_random()

        if self.player.energy < self.player.max_energy * 0.2:
            tax_energy_hp = True
            self.player.hp -= energy_hp_tax

        if self.player.hunger < self.player.max_hunger * 0.2:
            tax_hunger_hp = True
            self.player.hp -= hunger_hp_tax

        display = Utils.format_time(time) + " have passed: "
        if tax_energy: display += "\n    * Energy lost: " + Utils.format_float(time)
        display += "\n    * Hunger tax: " + Utils.format_float(hunger_tax)
        if tax_energy_hp: display += "\n    * You're tired. HP tax: " + Utils.format_float(energy_hp_tax)
        if tax_hunger_hp: display += "\n    * You're hungry. HP tax: " + Utils.format_float(hunger_hp_tax)

        return display





    def print_game_status(self, under_bar = False):
        Utils.draw_bar(125, "-", "Game Status: ", "*")
        print()
        print("                         Time: " + self.get_time() + "       |       " +
              "Day Period: " + self.get_day_period().name + "       |       " +
              "Days Survived: " + str(self.days_survived))
        print()
        if under_bar: Utils.draw_bar(125, "-", corners="*"); print()


    def print_player_status(self, under_bar = False):
        Utils.draw_bar(125, "-", self.player.name + " Status: ", "*")
        print()
        print("               HP: " + self.player.format_hp() + " / " + str(
            int(self.player.max_hp)) + "          |          " +
              "Hunger: " + self.player.format_hunger() + " / " + str(
            int(self.player.max_hunger)) + "           |          " +
              "Energy: " + self.player.format_energy() + " / " + str(int(self.player.max_energy)))
        print()
        print("Fishing Average Delay: " + self.player.format_fish_pull_delay() + "       |       " +
              "Hunt Average Success Rate: " + self.player.format_hunt_success_rate() + "       |       " +
              "Run Average Success Rate: " + self.player.format_run_success_rate())
        print()
        if under_bar: Utils.draw_bar(125, "-", corners="*"); print()



    def print_player_inventory(self, under_bar = False):
        Utils.draw_bar(125, "-", "Player Inventory: ", "*")
        print()
        print("                                   Fish: " + str(
            self.player.fish_amount) + "                 |                 " +
              "Meat: " + str(self.player.meat_amount))
        print()
        if under_bar: Utils.draw_bar(125, "-", corners="*"); print()



    def get_time(self):
        return Utils.format_time(self.time)


    def get_day_period(self):
        if self.time >= 0 and self.time < 6:
            return DayPeriod.DAWN
        elif self.time >= 6 and self.time < 12:
            return DayPeriod.MORNING
        elif self.time >= 12 and self.time < 18:
            return DayPeriod.AFTERNOON
        elif self.time >= 18 and self.time < 24:
            return DayPeriod.NIGHT