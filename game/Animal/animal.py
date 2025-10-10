from abc import ABC, abstractmethod

from utils.range import Range
from utils.day_period import DayPeriod


class Animal(ABC):
    def __init__(self, name, damage, hunt_success_rate_tax, run_success_rate_tax, meat_drop, ascii_art):
        self.name = name
        self.damage = damage
        self.hunt_success_rate_tax = hunt_success_rate_tax
        self.run_success_rate_tax = run_success_rate_tax
        self.meat_drop = meat_drop
        self.ascii_art = ascii_art

    @staticmethod
    def get_random(day_period: DayPeriod):

        from game.Animal.jaguar import Jaguar
        from game.Animal.caiman import Caiman
        from game.Animal.anaconda import Anaconda
        from game.Animal.harpy import Harpy

        probabilities = {
            DayPeriod.DAWN: [0.25, 0.10, 0.15, 0.50],
            DayPeriod.MORNING: [0.05, 0.25, 0.10, 0.60],
            DayPeriod.AFTERNOON: [0.10, 0.30, 0.10, 0.50],
            DayPeriod.NIGHT: [0.20, 0.05, 0.35, 0.40]
        }

        current_probs = probabilities[day_period]

        prob = Range(0, 1.0).get_random()

        if prob <= current_probs[0]:
            return Jaguar()
        if prob <= current_probs[0] + current_probs[1]:
            return Caiman()
        if prob <= current_probs[0] + current_probs[1] + current_probs[2]:
            return Anaconda()
        return Harpy()

