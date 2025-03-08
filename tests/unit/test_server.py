import pytest
from flask import Flask
from flask.testing import FlaskClient
from ...services.server import create_app

@pytest.fixture
def client() -> FlaskClient:
    with create_app().test_client() as client:
        yield client

def test_home(client):
    response = client.get('/ticker/AAPL')
    assert response.status_code == 200
    data = response.get_json()
    print(data)
    assert 'symbol' in data
    assert data['symbol'] == 'AAPL'
