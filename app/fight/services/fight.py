from .player import Player
# Helpers
from fight.helpers import default_players


class Fight:
    def __init__(self, data):
        self.data = data

    def start(self):
        player1 = Player(self.data.get('player1'))
        player2 = Player(self.data.get('player2'))

        if (player1.num_combos < player2.num_combos) or (player1.num_moves < player2.num_moves) or (player1.num_blows < player2.num_blows):
            first = player1
            second = player2
        elif (player2.num_combos < player1.num_combos) or (player2.num_moves < player1.num_moves) or (player2.num_blows < player1.num_blows):
            first = player2
            second = player1
        else:
            first = player1
            second = player2

        first
