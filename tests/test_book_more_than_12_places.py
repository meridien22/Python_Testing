import server
from tests.conftest import client
import html

def test_book_less_than_12_places(client):
    server.clubs = [{"name": "Test club", "points": "25"}]
    server.competitions = [{"name": "Test competition", "numberOfPlaces": "25"}]

    response = client.post('/purchasePlaces', data={
        'competition': "Test competition",
        'club': "Test club",
        'places': '10',
    })

    assert response.status_code == 200
    assert b"Great, booking complete!" in response.data
    assert int(server.competitions[0]['numberOfPlaces']) == 15

def test_book_more_than_12_places(client):
    server.clubs = [{"name": "Test club", "points": "25"}]
    server.competitions = [{"name": "Test competition", "numberOfPlaces": "25"}]

    response = client.post('/purchasePlaces', data={
        'competition': "Test competition",
        'club': "Test club",
        'places': '13',
    })

    assert response.status_code == 200
    data_clean = html.unescape(response.data.decode())
    assert "You can't book more than 12 places." in data_clean
    assert int(server.competitions[0]['numberOfPlaces']) == 25
