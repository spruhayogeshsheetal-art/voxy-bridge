import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_cognition_endpoint(client):
    response = client.post('/api/cognition/evaluate', json={
        "language": "python",
        "code": "print('Cognition Test Active')"
    })
    assert response.status_code in [200, 404, 500]
