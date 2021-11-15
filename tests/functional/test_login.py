def test_if_correct_db(mongo):
    """
    GIVEN a Mongo client
    WHEN testing
    THEN check the client is connected to the test database
    """
    assert mongo.db.name == "test"


def test_fake_user_exists(mongo, fake_user):
    """
    GIVEN a Mongo client and fake user data
    WHEN testing login
    THEN check if fake user exists in test database
    """
    assert mongo.db.users.find({"email": fake_user["email"]})


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
