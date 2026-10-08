import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "Flask Backend Running",
    }
