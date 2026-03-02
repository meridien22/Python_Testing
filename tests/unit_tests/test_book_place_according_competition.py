import server
from tests.conftest import client
import html

def test_book_places_with_enough_place_competition(client):
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

def test_book_places_without_enough_place_competition(client):
    server.clubs = [{"name": "Test club", "points": "4"}]
    server.competitions = [{"name": "Test competition", "numberOfPlaces": "5"}]

    response = client.post('/purchasePlaces', data={
        'competition': "Test competition",
        'club': "Test club",
        'places': '6',
    })

    assert response.status_code == 200
    data_clean = html.unescape(response.data.decode())
    assert "Competition don't have enough place." in data_clean
    assert int(server.competitions[0]['numberOfPlaces']) == 5