import json
import logging
import pytest
from fastapi.testclient import TestClient
from src.app.main import app
from src.app.import_routes import import_routes
from databases import Database
from tests.test_datases import TEST_DATABASE_URL, create_engine, text, MetaData

app.logger = logging.getLogger(name="PREQUIN_TEST")
app.logger.disabled = True

# Create a test client
import_routes(app)
client = TestClient(app)

# Fixtures to create and drop the test database
@pytest.fixture(scope="module")
def create_test_database():
    test_database_url = TEST_DATABASE_URL
    engine = create_engine(test_database_url)
    metadata = MetaData()
    metadata.drop_all(engine)
    metadata.create_all(engine)
    yield test_database_url
    metadata.drop_all(engine)

# Test the /register and /token endpoints
def test_register_and_login(create_test_database):
    # Register a user
    register_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/user/register", json=register_data, headers={
        'accept': 'application/json',
        'Content-Type': 'application/json'
    })
    assert response.status_code == 200

    # Log in to get an access token
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/user/token", data=login_data)
    assert response.status_code == 200

    # Extract the access token from the response
    access_token = response.json()["access_token"]

    # Test the /generate_array endpoint with the access token
    generate_array_data = {
        "sentence": "This is a test sentence."
    }
    response = client.post("/app/generate_array", json=generate_array_data, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
