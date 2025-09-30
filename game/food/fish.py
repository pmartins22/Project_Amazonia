from game.food.food import Food
from utils.range import Range


class Fish(Food):
    def __init__(self):
        super().__init__("Fish", Range(0.8, 1.2))