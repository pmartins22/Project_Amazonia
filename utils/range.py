import random


class Range:
    def __init__(self, min, max):
        if min > max:
            raise ValueError(f"min ({min}) must not be bigger than max ({max})")
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

    def to_dict(self):
        return {"min": self.min, "max": self.max}

    @classmethod
    def from_dict(cls, data):
        if "min" not in data or "max" not in data:
            raise KeyError("Dictionary must contain 'min' and 'max'")
        return cls(data["min"], data["max"])