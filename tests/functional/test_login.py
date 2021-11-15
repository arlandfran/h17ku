def test_login_data_is_valid(client):
    """
    GIVEN a Flask app
    WHEN the /login endpoint is sent empty data (POST)
    THEN check the expects the email and password fields
    """
    response = client.post("/api/auth/login", json={})
    assert response == 400
    assert response.json["msg"]["email"] == ["Missing data for required field."]
    assert response.json["msg"]["password"] == ["Missing data for required field."]


def test_email_is_valid(client):
    """
    GIVEN a Flask app
    WHEN the /login endpoing is sent an invalid email (POST)
    THEN check that the endpoint expects a valid email address and returns the correct response
    """
    response = client.post("/api/auth/login", json={"email": ""})
    assert response.status_code == 400
    assert response.json["msg"]["email"] == ["Not a valid email address."]

    response = client.post("/api/auth/login", json={"email": "invalid"})
    assert response.status_code == 400
    assert response.json["msg"]["email"] == ["Not a valid email address."]

    response = client.post("/api/auth/login", json={"email": "invalid@invalid"})
    assert response.status_code == 400
    assert response.json["msg"]["email"] == ["Not a valid email address."]


def test_password_is_valid(client):
    """
    GIVEN a Flask app
    WHEN the /login endpoint is sent an invalid password (POST)
    THEN check that the endpoint expects a valid password and returns the correct response
    """
    response = client.post("/api/auth/login", json={"password": ""})
    assert response.status_code == 400
    assert response.json["msg"]["password"] == [
        "password must be at least 8 characters"
    ]

    response = client.post("/api/auth/login", json={"password": "1234"})
    assert response.status_code == 400
    assert response.json["msg"]["password"] == [
        "password must be at least 8 characters"
    ]

    response = client.post("/api/auth/login", json={"password": "1234 5678"})
    assert response.status_code == 400
    assert response.json["msg"] == "no spaces allowed"
