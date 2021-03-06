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

    response = client.post(
        "/api/auth/login",
        json={"email": "wrong@email.com", "password": "wrongpassword"},
    )
    assert response.status_code == 404
    assert response.json["msg"] == "email not found"
    assert response.json["login"] is False


def test_password_is_valid(client, fake_user):
    """
    GIVEN a Flask app and fake user data
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

    response = client.post(
        "/api/auth/login",
        json={"email": fake_user["email"], "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json["msg"] == "incorrect password"
    assert response.json["login"] is False


def test_user_login(client, fake_user):
    """
    GIVEN a Flask app and fake user data
    WHEN the /login endpoint is sent a valid data (POST)
    THEN check that the response is valid and user is logged in
    """
    response = client.post(
        "/api/auth/login",
        json={"email": fake_user["email"], "password": fake_user["password"]},
    )
    assert response.status_code == 200
    assert response.json["login"] is True


def test_user_is_logged_in(client, fake_user):
    """
    GIVEN a Flask app and fake user data
    WHEN user login is successful
    THEN check that the user is in Flask session
    """
    response = client.post(
        "/api/auth/login",
        json={"email": fake_user["email"], "password": fake_user["password"]},
    )
    assert response.status_code == 200
    assert response.json["login"] is True

    response = client.get("/api/auth/session")
    assert response.status_code == 200
    assert response.json["login"] is True
    assert response.json["id"] == fake_user["username"]


def test_user_not_logged_in(client):
    """
    GIVEN a Flask app
    WHEN there is no user logged in
    THEN check that there is no user in Flask session
    """
    response = client.get("/api/auth/session")
    assert response.status_code == 404
    assert response.json["login"] is False
