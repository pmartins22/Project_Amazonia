from game import game_manager


class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_average(self):
        return (self.min + self.max) / 2