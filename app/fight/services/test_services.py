import pytest
from .player import Player


@pytest.fixture
def player():
    combos = {
        "movimientos": ["D", "DSD", "S", "DSD", "SD"],
        "golpes": ["K", "P", "", "K", "P"]
    }

    return Player(combos)


class TestPlayer:
    def test_num_combos(self, player):
        assert player.num_combos() == 4

    def test_num_moves(self, player):
        assert player.num_moves() == 5

    def test_num_blows(self, player):
        assert player.num_blows() == 4


class TestFight:
    pass
