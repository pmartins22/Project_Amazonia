# This file defines the abstract base class for all animals in the game.
from abc import ABC

from utils.range import Range
from utils.day_period import DayPeriod


class Animal(ABC):
    """
    An abstract base class for all animals in the game.

    This class provides a common structure for animal objects, including their
    attributes like damage, success rate taxes for hunting and running, meat drop
    amount, and ASCII art. It also includes a static method to get a random
    animal based on the time of day.
    """
    def __init__(self, name, damage, hunt_success_rate_tax, run_success_rate_tax, meat_drop, ascii_art):
        """
        Initializes a new Animal instance.

        :param name: The name of the animal.
        :type name: str
        :param damage: The range of damage the animal can inflict.
        :type damage: Range
        :param hunt_success_rate_tax: The tax applied to the player's hunt success rate.
        :type hunt_success_rate_tax: Range
        :param run_success_rate_tax: The tax applied to the player's run success rate.
        :type run_success_rate_tax: Range
        :param meat_drop: The range of meat dropped upon death.
        :type meat_drop: Range
        :param ascii_art: The ASCII art representation of the animal.
        :type ascii_art: str
        """
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
        """
        Returns a random animal instance based on the time of day.

        The probability of encountering each type of animal changes depending on
        whether it is dawn, morning, afternoon, or night.

        :param day_period: The current period of the day.
        :type day_period: DayPeriod
        :return: An instance of a randomly selected animal class.
        :rtype: Animal
        :raises TypeError: If day_period is not a DayPeriod enum.
        """
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