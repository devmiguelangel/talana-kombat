import pytest
from .player import Player


@pytest.fixture
def combos():
    combos = {
        "movimientos": ["D", "DSD", "S", "DSD", "SD"],
        "golpes": ["K", "P", "", "K", "P"]
    }

    return combos


@pytest.fixture
def player(combos):
    return Player('player1', combos)


class TestPlayer:
    def test_num_combos(self, player):
        assert player.num_combos() == 4

    def test_num_moves(self, player):
        assert player.num_moves() == 5

    def test_num_blows(self, player):
        assert player.num_hits() == 4

    def test_attack_damage(self, player):
        assert player.get_attack_damage('D', 'K')['damage'] == 1
        assert player.get_attack_damage('DSD', 'P')['damage'] == 3
        assert player.get_attack_damage('S', '')['damage'] == 0
        assert player.get_attack_damage('DSD', 'K')['damage'] == 2
        assert player.get_attack_damage('SD', 'P')['damage'] == 1


class TestFight:
    pass
