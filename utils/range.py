import random


class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_average(self):
        return (self.min + self.max) / 2

    def get_random(self, as_int=False):
        if as_int:
            return random.randint(self.min, self.max)
        return random.uniform(self.min, self.max)

    def subtract(self, other):
        return Range(self.min - other.min, self.max - other.max)

    def add(self, other):
        return Range(self.min + other.min, self.max + other.max)