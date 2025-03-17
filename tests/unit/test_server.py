import pytest
from flask import Flask
from flask.testing import FlaskClient
from ...services.server import create_app

@pytest.fixture
def client() -> FlaskClient:
    with create_app().test_client() as client:
        yield client

def test_home_with_stub(mocker, client):
    fake_data = {"symbol": "MSFT", "price": 100.0, "name": "Fake Company"}
    mocker.patch("yfinanceapi.services.server.get_ticker", return_value=fake_data)
    response = client.get('/ticker/MSFT')
    assert response.status_code == 200
    data = response.get_json()
    assert data == fake_data

def test_home_with_stub_no_data(mocker, client):
    fake_data = {}
    mocker.patch("yfinanceapi.services.server.get_ticker", return_value=fake_data)
    response = client.get('/ticker/INVALID')
    assert response.status_code == 200
    data = response.get_json()
    assert data == fake_data
