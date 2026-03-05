import server
from tests.conftest import client
import html
import re

def test_registration_until_competition_is_full(client):
    """Secretaries reserve places for a competition until it is no longer
    possible because the competition is full."""

    server.clubs = [
        {
        "name": "test_club_1",
        "points": "10",
        "email": "john@simplylift.co",
        },
        {
        "name": "test_club_2",
        "points": "20",
        "email": "john@simplylift.co",
        },
    ]
    server.competitions = [{
        "name": "test_competition",
        "numberOfPlaces": "20",
        "date": "2027-03-27 10:00:00",
    }]

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition",
        'club': "test_club_1",
        'places': '5',
    })
    assert response.status_code == 200
    assert b"Great, booking complete !" in response.data

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition",
        'club': "test_club_2",
        'places': '5',
    })
    assert response.status_code == 200
    assert b"Great, booking complete !" in response.data

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition",
        'club': "test_club_1",
        'places': '11',
    })
    assert response.status_code == 200
    data_clean = html.unescape(response.data.decode())
    assert "Competition don't have enough place." in data_clean

def test_registration_until_club_have_not_enough_place(client):
    """A secretary reserves places for competitions until it is 
    no longer possible because the club no longer has enough points."""


    server.clubs = [
        {
        "name": "test_club",
        "points": "10",
        "email": "john@simplylift.co",
        },
    ]
    server.competitions = [
        {
        "name": "test_competition_1",
        "numberOfPlaces": "20",
        "date": "2027-03-27 10:00:00",
        },
        {
        "name": "test_competition_2",
        "numberOfPlaces": "40",
        "date": "2027-04-02 10:00:00",
        }
    ]

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition_1",
        'club': "test_club",
        'places': '5',
    })
    assert response.status_code == 200
    assert b"Great, booking complete !" in response.data

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition_2",
        'club': "test_club",
        'places': '5',
    })
    assert response.status_code == 200
    assert b"Great, booking complete !" in response.data

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition_1",
        'club': "test_club",
        'places': '5',
    })
    assert response.status_code == 200
    assert b"have enough points." in response.data


def test_registration_and_update_public_page(client):
    """Secretaries reserve seats and the public points display page is up to date"""

    server.clubs = [
        {
        "name": "test_club_1",
        "points": "10",
        "email": "john@simplylift.co",
        },
        {
        "name": "test_club_2",
        "points": "20",
        "email": "john@simplylift.co",
        },
    ]
    server.competitions = [{
        "name": "test_competition",
        "numberOfPlaces": "20",
        "date": "2027-03-27 10:00:00",
    }]

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition",
        'club': "test_club_1",
        'places': '5',
    })
    assert response.status_code == 200
    assert b"Great, booking complete !" in response.data

    response = client.post('/purchasePlaces', data={
        'competition': "test_competition",
        'club': "test_club_2",
        'places': '5',
    })
    assert response.status_code == 200
    assert b"Great, booking complete !" in response.data

    response = client.get('/points')
    assert response.status_code == 200

    html_nettoye = re.sub(r'\s+', ' ', response.data.decode())
    assert "<td>test_club_1</td><td>5</td>"
    assert "<td>test_club_2</td><td>15</td>"
