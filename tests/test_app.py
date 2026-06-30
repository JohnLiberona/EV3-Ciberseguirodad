import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app_fixed import app


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


def test_hello_escapes_script_tag(client):
    """Verifica que el XSS reflejado quede mitigado."""
    resp = client.get('/hello?name=<script>alert(1)</script>')
    assert resp.status_code == 200
    assert b'<script>' not in resp.data
    assert b'&lt;script&gt;' in resp.data
