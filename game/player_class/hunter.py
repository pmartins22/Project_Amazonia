from game.player_class.player_class import PlayerClass
from utils.range import Range


class Hunter(PlayerClass):
    def __init__(self):
        super().__init__("Hunter")

    def apply_buff(self, player):
        player.hunt_success_rate = player.hunt_success_rate.add(Range(0.1, 0.1))
        player.run_success_rate = player.run_success_rate.add(Range(0.1, 0.1))