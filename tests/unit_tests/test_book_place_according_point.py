import server
from tests.conftest import client

def test_book_places_with_enough_points(client):
    server.clubs = [{"name": "Test club", "points": "4"}]
    server.competitions = [{"name": "Test competition", "numberOfPlaces": "5"}]

    response = client.post('/purchasePlaces', data={
        'competition': "Test competition",
        'club': "Test club",
        'places': '4',
    })

    assert response.status_code == 200
    assert b"Great, booking complete!" in response.data
    assert int(server.competitions[0]['numberOfPlaces']) == 1

def test_book_places_without_enough_points(client):
    server.clubs = [{"name": "Test club", "points": "4"}]
    server.competitions = [{"name": "Test competition", "numberOfPlaces": "5"}]

    response = client.post('/purchasePlaces', data={
        'competition': "Test competition",
        'club': "Test club",
        'places': '5',
    })

    assert response.status_code == 200
    assert b"have enough points." in response.data
    assert int(server.competitions[0]['numberOfPlaces']) == 5
