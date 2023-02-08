# Helpers
from fight.helpers import default_players


class Player:
    def __init__(self, player_number, data):
        self.name = default_players[player_number]['name']
        self.default_combos = default_players[player_number]['default_combos']
        self.moves = data['movimientos']
        self.hits = data['golpes']
        self.life = 6

    def num_combos(self):
        """ It returns the number of combos in the current move set """

        num = 0

        for i, m in enumerate(self.moves):
            if len(m) > 0 and len(self.hits[i]) > 0:
                num += 1

        return num

    def num_moves(self):
        """ It returns the number of moves """

        num = 0

        for m in self.moves:
            if len(m) > 0:
                num += 1

        return num

    def num_hits(self):
        """ It returns the number of hits """

        num = 0

        for b in self.hits:
            if len(b) > 0:
                num += 1

        return num

    def get_attack_damage(self, move, hit):
        message = ''
        damage = 0

        # Creating a string with the current move and hit combination
        current_hit = '{move}+{hit}'.format(move=move, hit=hit)

        for combo in self.default_combos:
            # Creating a string with the default move and hit combination
            combo_hit = '{move}+{hit}'.format(move=combo['move'], hit=combo['hit'])
            # Looking for the index of the current hit in the default combos
            index = current_hit.find(combo_hit)

            # Checking if the current move and hit combination is in the default combos
            if index == 0:
                message = '{0} lanza {1}'.format(self.name, combo['attack_message'])
                damage = combo['power']
                break
            elif index >= 1:
                message = '{0} se mueve y lanza {1}'.format(self.name, combo['attack_message'])
                damage = combo['power']
                break
            elif len(move) > 0:
                message = '{0} se mueve'.format(self.name)
                damage = 0

        return {'message': message, 'damage': damage}
