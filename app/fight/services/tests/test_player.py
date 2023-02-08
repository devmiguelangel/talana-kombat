import pytest
from fight.services import Player


@pytest.fixture
def combos():
    combos = [
        {
            "movimientos": ["D", "DSD", "S", "DSD", "SD"],
            "golpes": ["K", "P", "", "K", "P"]
        },
        {
            "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
            "golpes": ["K", "", "K", "P", "P"]
        }
    ]

    return combos


@pytest.fixture
def player1(combos):
    return Player('player1', combos[0])


@pytest.fixture
def player2(combos):
    return Player('player2', combos[1])


class TestPlayer:
    def test_num_combos(self, player1, player2):
        assert player1.num_combos() == 4
        assert player2.num_combos() == 4

    def test_num_moves(self, player1, player2):
        assert player1.num_moves() == 5
        assert player2.num_moves() == 5

    def test_num_blows(self, player1, player2):
        assert player1.num_hits() == 4
        assert player2.num_hits() == 4

    def test_attack_damage_player1(self, player1):
        assert player1.get_attack_damage('D', 'K')[1] == 1
        assert player1.get_attack_damage('DSD', 'P')[1] == 3
        assert player1.get_attack_damage('S', '')[1] == 0
        assert player1.get_attack_damage('DSD', 'K')[1] == 2
        assert player1.get_attack_damage('SD', 'P')[1] == 1

    def test_attack_damage_player2(self, player2):
        assert player2.get_attack_damage('SA', 'K')[1] == 3
        assert player2.get_attack_damage('SA', '')[1] == 0
        assert player2.get_attack_damage('SA', 'K')[1] == 3
        assert player2.get_attack_damage('ASA', 'P')[1] == 2
        assert player2.get_attack_damage('SA', 'P')[1] == 1

    def test_push_damage(self, player1):
        player1.push_damage(1)
        assert player1.life == 5

        player1.push_damage(2)
        assert player1.life == 3

        player1.push_damage(3)
        assert player1.life == 0
