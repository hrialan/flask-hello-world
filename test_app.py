import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_helloworld(client):
    """Test the root endpoint."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'Hello World!'

def test_fake_data(client):
    """Test the fake data endpoint."""
    rv = client.get('/api/v1/fake-data')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data == {
        "name": "John Doe",
        "age": 30,
        "location": "New York"
    }


if __name__ == "__main__":
    pytest.main()