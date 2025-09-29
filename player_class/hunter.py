from player_class.player_class import PlayerClass


class Hunter(PlayerClass):
    def apply_buff(self, player):
        player.hunt_success_rate.min += 0.1
        player.hunt_success_rate.max += 0.1

        player.run_success_rate.min += 0.1
        player.run_success_rate.max += 0.1