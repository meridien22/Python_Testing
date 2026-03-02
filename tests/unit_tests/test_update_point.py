import server
from tests.conftest import client

def test_update_point(client):
    server.clubs = [{"name": "Test club", "points": "4"}]
    server.competitions = [{"name": "Test competition", "numberOfPlaces": "5"}]

    response = client.post('/purchasePlaces', data={
        'competition': "Test competition",
        'club': "Test club",
        'places': '3',
    })

    assert response.status_code == 200
    assert int(server.clubs[0]['points']) == 1