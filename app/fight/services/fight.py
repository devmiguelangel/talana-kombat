from .player import Player


class Fight:
    def __init__(self, data):
        self.data = data
        self.story = []

    @property
    def story(self):
        return self._story

    @story.setter
    def story(self, value):
        self._story = value

    def get_order_players(self):
        # Creating two players, player1 and player2, and assigning them the data from the json file
        player1 = Player('player1', self.data.get('player1'))
        player2 = Player('player2', self.data.get('player2'))

        if (player1.num_combos() < player2.num_combos()) or (player1.num_moves() < player2.num_moves()) or (player1.num_hits() < player2.num_hits()):
            return [player1, player2]
        elif (player2.num_combos() < player1.num_combos()) or (player2.num_moves() < player1.num_moves()) or (player2.num_hits() < player1.num_hits()):
            return [player2, player1]

        return [player1, player2]

    def start(self):
        first, second = self.get_order_players()

        # Finding the maximum number of moves between the two players
        n = max(len(first.moves), len(second.moves))

        for i in range(n):
            # Checking if the first player has moves left, if so, it will get the attack damage and message, and
            # append it to the story.
            if i < len(first.moves):
                attack1 = first.get_attack_damage(first.moves[i], first.hits[i])
                message, damage = attack1
                self.story.append(message)

                if damage > 0:
                    second.push_damage(damage)

                if second.life <= 0:
                    self.story.append(
                        '{0} Gana la pelea y aun le queda {1} de energía'.format(first.name, first.life)
                    )

                    break

            # Checking if the second player has moves left, if so, it will get the attack damage and message, and
            # append it to the story.
            if i < len(second.moves):
                attack2 = second.get_attack_damage(second.moves[i], second.hits[i])
                message, damage = attack2
                self.story.append(message)

                if damage > 0:
                    first.push_damage(damage)

                if first.life <= 0:
                    self.story.append(
                        '{0} Gana la pelea y aun le queda {1} de energía'.format(second.name, second.life)
                    )

                    break
