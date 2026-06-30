import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_ok(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json()['status'] == 'ok'


def test_hello_default(client):
    resp = client.get('/hello')
    assert resp.status_code == 200
    assert b'Hello, mundo!' in resp.data


def test_hello_with_name(client):
    resp = client.get('/hello?name=Juan')
    assert resp.status_code == 200
    assert b'Hello, Juan!' in resp.data
