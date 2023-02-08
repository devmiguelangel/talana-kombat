import pytest


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


def test_api_view_fight_error(client):
    response = client.post('/api/fights')

    assert response.status_code == 400


# @pytest.mark.django_db
def test_api_view_fight1(client, fights):
    data = fights[0]

    response = client.post(
        '/api/fights',
        data,
        content_type='application/json',
    )

    assert response.status_code == 200

    data = response.json()
    assert data[len(data) - 1].find('Arnaldor') == 0
    assert data[len(data) - 1].find('Tonyn') != 0


def test_api_view_fight2(client, fights):
    data = fights[1]

    response = client.post('/api/fights', data, content_type='application/json')

    assert response.status_code == 200

    data = response.json()
    assert data[len(data) - 1].find('Tonyn') == 0
    assert data[len(data) - 1].find('Arnaldor') != 0


def test_api_view_fight3(client, fights):
    data = fights[2]

    response = client.post('/api/fights', data, content_type='application/json')

    assert response.status_code == 200

    data = response.json()
    assert data[len(data) - 1].find('Arnaldor') == 0
    assert data[len(data) - 1].find('Tonyn') != 0
