class Player:
    def __init__(self, combos):
        self.life = 6
        self.moves = combos['movimientos']
        self.blows = combos['golpes']

    def num_combos(self):
        num = 0

        for i, m in enumerate(self.moves):
            if len(m) > 0 and len(self.blows[i]) > 0:
                num += 1

        return num

    def num_moves(self):
        num = 0

        for m in self.moves:
            if len(m) > 0:
                num += 1

        return num

    def num_blows(self):
        num = 0

        for b in self.blows:
            if len(b) > 0:
                num += 1

        return num
