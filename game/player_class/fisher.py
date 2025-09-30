from game.player_class.player_class import PlayerClass

class Fisher(PlayerClass):
    def apply_buff(self, player):
        player.fish_pull_delay.min += 0.2
        player.fish_pull_delay.max += 0.2

