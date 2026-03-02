import server
from tests.conftest import client

def test_connection_inscription(client):
    """A secretary logs onto the platform and reserves places for a tournament"""

    server.clubs = [{
        "name": "Test club",
        "points": "4",
        "email": "john@simplylift.co",
    }]
    server.competitions = [{
        "name": "Test competition",
        "numberOfPlaces": "5",
        "date": "2027-03-27 10:00:00",
    }]

    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome' in response.data

    response = client.post('/purchasePlaces', data={
        'competition': "Test competition",
        'club': "Test club",
        'places': '4',
    })

    assert response.status_code == 200
    assert b"Great, booking complete !" in response.data
