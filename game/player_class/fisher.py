from game.player_class.player_class import PlayerClass
from utils.range import Range


class Fisher(PlayerClass):
    def __init__(self):
        super().__init__("Fisher")

    def apply_buff(self, player):
        player.fish_pull_delay = player.fish_pull_delay.add(Range(0.2, 0.2))

