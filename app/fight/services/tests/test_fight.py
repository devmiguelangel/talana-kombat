import pytest
from fight.services import Fight


@pytest.fixture
def fights():
    fights = [
        {
            "player1": {
                "movimientos": ["D", "DSD", "S", "DSD", "SD"],
                "golpes": ["K", "P", "", "K", "P"]
            },
            "player2": {
                "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
                "golpes": ["K", "", "K", "P", "P"]
            }
        },
        {
            "player1": {
                "movimientos": ["SDD", "DSD", "SA", "DSD"],
                "golpes": ["K", "P", "K", "P"]
            },
            "player2": {
                "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
                "golpes": ["P", "K", "K", "K", "P", "K"]
            }
        },
        {
            "player1": {
                "movimientos": ["DSD", "S"],
                "golpes": ["P", ""]
            },
            "player2": {
                "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
                "golpes": ["P", "", "P", "K", "K", "K"]
            }
        }
    ]

    return fights


@pytest.fixture
def fight1(fights):
    return Fight(fights[0])


@pytest.fixture
def fight2(fights):
    return Fight(fights[1])


@pytest.fixture
def fight3(fights):
    return Fight(fights[2])


class TestFight:
    def test_order_players(self, fight1):
        first, second = fight1.get_order_players()

        assert first.name == 'Tonyn'
        assert second.name == 'Arnaldor'

    def test_start_fight1(self, fight1):
        fight1.start()
        last_story = fight1.story[len(fight1.story) - 1]

        assert last_story.find('Arnaldor') == 0

    def test_start_fight2(self, fight2):
        fight2.start()
        last_story = fight2.story[len(fight2.story) - 1]

        assert last_story.find('Tonyn') == 0

    def test_start_fight3(self, fight3):
        fight3.start()
        last_story = fight3.story[len(fight3.story) - 1]

        assert last_story.find('Arnaldor') == 0
