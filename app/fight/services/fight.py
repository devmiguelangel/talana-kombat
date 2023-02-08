from .player import Player


class Fight:
    def __init__(self, data):
        self.data = data

    def start(self):
        player1 = Player('player1', self.data.get('player1'))
        player2 = Player('player2', self.data.get('player2'))

        if (player1.num_combos() < player2.num_combos()) or (player1.num_moves() < player2.num_moves()) or (player1.num_hits() < player2.num_hits()):
            first = player1
            second = player2
        elif (player2.num_combos() < player1.num_combos()) or (player2.num_moves() < player1.num_moves()) or (player2.num_hits() < player1.num_hits()):
            first = player2
            second = player1
        else:
            first = player1
            second = player2

        n = max(len(first.moves), len(second.moves))

        for i in range(n):
            attack = first.get_attack_damage(first.moves[i], first.hits[i])
            message, damage = attack.values()
