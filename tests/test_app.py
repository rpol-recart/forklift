import pytest
from app.create_flask import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as c:
        yield c


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data


def test_404_error(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
