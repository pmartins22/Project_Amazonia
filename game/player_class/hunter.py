# This file defines the Hunter class, a specific player specialization.
from game.player_class.player_class import PlayerClass
from utils.range import Range


class Hunter(PlayerClass):
    """
    Represents the Hunter specialization.

    Players with this class gain buffs to their hunting and running success rates,
    making them more effective at tracking and escaping animals.
    """

    def __init__(self):
        """
        Initializes the Hunter class.
        """
        super().__init__("Hunter")

    def apply_buff(self, player):
        """
        Applies the Hunter-specific buffs to the player.

        Increases the player's hunt and run success rates.

        :param player: The player instance to apply the buffs to.
        :type player: Player
        """
        player.hunt_success_rate = player.hunt_success_rate.add(Range(0.1, 0.1))
        player.run_success_rate = player.run_success_rate.add(Range(0.1, 0.1))