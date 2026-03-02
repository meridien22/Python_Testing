import server
from tests.conftest import client

def test_book_not_past_competition(client):
    server.competitions = [{
        "name": "Test competition",
        "numberOfPlaces": "5",
        "date": "2026-10-22 13:30:00",
    }]
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Book Places' in response.data

def test_book_past_competition(client):
    server.competitions = [{
        "name": "Test competition",
        "numberOfPlaces": "5",
        "date": "2020-10-22 13:30:00",
    }]
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Book Places' not in response.data