import pytest


def test_api_view_fight_error(client):
    response = client.post('/api/fights')

    assert response.status_code == 400


@pytest.mark.django_db
def test_api_view_fight1(client):
    data = {
        "player1": {
            "movimientos": ["D", "DSD", "S", "DSD", "SD"],
            "golpes": ["K", "P", "", "K", "P"]
        },
        "player2": {
            "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
            "golpes": ["K", "", "K", "P", "P"]
        }
    }
    response = client.post(
        '/api/fights',
        json=data,
    )

    print('#########################')
    print(response.json())
    print('#########################')

    assert response.status_code == 200
