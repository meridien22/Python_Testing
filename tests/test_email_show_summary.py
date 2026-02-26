from tests.conftest import client

def test_show_summary_with_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_show_summary_with_unknow_email(client):
    response = client.post('/showSummary', data={'email': 'toto@simplylift.co'})
    assert response.status_code == 200
    assert b"Cet email ne correspond" in response.data

def test_show_summary_with_no_email(client):
    response = client.post('/showSummary', data={'email': ''})
    assert response.status_code == 200
    assert b"Cet email ne correspond" in response.data