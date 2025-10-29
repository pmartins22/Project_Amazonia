from abc import ABC, abstractmethod

from utils.range import Range
from utils.day_period import DayPeriod


class Animal(ABC):
    def __init__(self, name, damage, hunt_success_rate_tax, run_success_rate_tax, meat_drop, ascii_art):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(damage, Range):
            raise TypeError("damage must be a Range object")
        if not isinstance(hunt_success_rate_tax, Range):
            raise TypeError("hunt_success_rate_tax must be a Range object")
        if not isinstance(run_success_rate_tax, Range):
            raise TypeError("run_success_rate_tax must be a Range object")
        if not isinstance(meat_drop, Range):
            raise TypeError("meat_drop must be a Range object")
        if not isinstance(ascii_art, str):
            raise TypeError("ascii_art must be a string")

        self.name = name
        self.damage = damage
        self.hunt_success_rate_tax = hunt_success_rate_tax
        self.run_success_rate_tax = run_success_rate_tax
        self.meat_drop = meat_drop
        self.ascii_art = ascii_art

    @staticmethod
    def get_random(day_period: DayPeriod):
        if not isinstance(day_period, DayPeriod):
            raise TypeError("day_period must be a DayPeriod enum")

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

        cumulative = 0
        animals = [Jaguar, Caiman, Anaconda, Harpy]

        for i, animal_prob in enumerate(current_probs):
            cumulative += animal_prob
            if prob <= cumulative:
                return animals[i]()

        return Harpy()