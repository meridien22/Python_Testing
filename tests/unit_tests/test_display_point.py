import server
from tests.conftest import client

def test_show_summary_with_points_club(client):
    """Displaying other clubs' points on the club's homepage."""
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Clubs' in response.data


def test_table_points_public(client):
    """Displaying the points of all clubs on the public page of the site."""
    response = client.get('/points')
    assert response.status_code == 200
    assert b'Clubs' in response.data