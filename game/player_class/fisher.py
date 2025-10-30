# This file defines the Fisher class, a specific player specialization.
from game.player_class.player_class import PlayerClass
from utils.range import Range


class Fisher(PlayerClass):
    """
    Represents the Fisher specialization.

    Players with this class are more adept at fishing, gaining a buff that
    increases the time window for successfully catching a fish.
    """

    def __init__(self):
        """
        Initializes the Fisher class.
        """
        super().__init__("Fisher")

    def apply_buff(self, player):
        """
        Applies the Fisher-specific buffs to the player.

        Increases the player's fish pull delay, making it easier to catch fish.

        :param player: The player instance to apply the buffs to.
        :type player: Player
        """
        player.fish_pull_delay = player.fish_pull_delay.add(Range(0.2, 0.2))
