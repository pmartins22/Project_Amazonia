from game.food.food import Food
from utils.range import Range


class Meat(Food):
    def __init__(self):
        super().__init__("Meat", Range(1.8, 2.2))