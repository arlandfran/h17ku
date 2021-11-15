import os
from dotenv import load_dotenv

load_dotenv()


def test_app_config(config):
    """
    GIVEN a Flask app config
    WHEN a Flask app is created
    THEN check that the app is configured correctly for testing
    """
    assert config["TESTING"] is True
    assert config["WTF_CSRF_ENABLED"] is False
    assert config["MONGO_URI"] == os.getenv("MONGO_TEST_URI")


def test_home_page(client):
    """
    GIVEN a Flask app
    WHEN '/' is requested (GET)
    THEN check that the response is valid and h14ku, csrf-token are present
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"h14ku" in response.data
    assert b"csrf-token" in response.data


def test_csrf_error_handler(csrf_client):
    """
    GIVEN a Flask app that is CSRF protected
    WHEN an endpoint is requested or sent data (GET, POST)
    THEN check that response is valid
    """
    response = csrf_client.get("/register")
    assert response.status_code == 200

    response = csrf_client.post("/api/auth/register")
    assert response.status_code == 400
    assert response.json["msg"] == "The CSRF token is missing."

    response = csrf_client.get("/login")
    assert response.status_code == 200

    response = csrf_client.post("/api/auth/login")
    assert response.status_code == 400
    assert response.json["msg"] == "The CSRF token is missing."
