from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, damage, hunt_success_rate_tax, run_success_rate_tax, meat_drop):
        self.name = name
        self.damage = damage
        self.hunt_success_rate = hunt_success_rate_tax
        self.run_success_rate = run_success_rate_tax
        self.meat_drop = meat_drop
