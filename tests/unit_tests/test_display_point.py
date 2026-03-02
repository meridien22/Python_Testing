import server
from tests.conftest import client

def test_show_summary_with_points_club(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Clubs' in response.data
