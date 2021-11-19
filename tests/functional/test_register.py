def test_empty_data_is_invalid(client):
    """
    GIVEN a Flask app
    WHEN the /register endpoint is sent empty data (POST)
    THEN check that the endpoint expects the email, username, password and password2 fields
    """
    response = client.post("/api/auth/register", json={})
    assert response.status_code == 400
    assert response.json["msg"]["email"] == ["Missing data for required field."]
    assert response.json["msg"]["username"] == ["Missing data for required field."]
    assert response.json["msg"]["password"] == ["Missing data for required field."]
    assert response.json["msg"]["password2"] == ["Missing data for required field."]


def test_email_is_valid(client):
    """
    GIVEN a Flask app
    WHEN the /register endpoing is sent an invalid email (POST)
    THEN check that the endpoint expects a valid email address and returns the correct response
    """
    response = client.post("/api/auth/register", json={"email": ""})
    assert response.status_code == 400
    assert response.json["msg"]["email"] == ["Not a valid email address."]

    response = client.post("/api/auth/register", json={"email": "invalid"})
    assert response.status_code == 400
    assert response.json["msg"]["email"] == ["Not a valid email address."]

    response = client.post("/api/auth/register", json={"email": "invalid@invalid"})
    assert response.status_code == 400
    assert response.json["msg"]["email"] == ["Not a valid email address."]


def test_username_is_valid(client):
    """
    GIVEN a Flask app
    WHEN the /register endpoint is sent an invalid username (POST)
    THEN check that the endpoint expects a valid username and returns the correct response
    """
    response = client.post("/api/auth/register", json={"username": ""})
    assert response.status_code == 400
    assert response.json["msg"]["username"] == [
        "username must be at least 4 characters"
    ]

    response = client.post("/api/auth/register", json={"username": "with spaces"})
    assert response.status_code == 400
    assert response.json["msg"] == "no spaces allowed"


def test_password_is_valid(client):
    """
    GIVEN a Flask app
    WHEN the /register endpoint is sent an invalid password (POST)
    THEN check that the endpoint expects a valid password and returns the correct response
    """
    response = client.post("/api/auth/register", json={"password": ""})
    assert response.status_code == 400
    assert response.json["msg"]["password"] == [
        "password must be at least 8 characters"
    ]

    response = client.post("/api/auth/register", json={"password": "1234"})
    assert response.status_code == 400
    assert response.json["msg"]["password"] == [
        "password must be at least 8 characters"
    ]

    response = client.post("/api/auth/register", json={"password": "1234 5678"})
    assert response.status_code == 400
    assert response.json["msg"] == "no spaces allowed"


def test_passwords_match(client, different_passwords):
    """
    GIVEN a Flask app and fake user data with different passwords
    WHEN the /register endpoint is sent non matching passwords (POST)
    THEN check that the endpoint expects matching passwords and returns the correct response
    """
    response = client.post("/api/auth/register", json=different_passwords)
    assert response.status_code == 400
    assert response.json["msg"] == "passwords do not match"


def test_register_new_user(client, mongo, new_fake_user):
    """
    GIVEN a Flask app, a Mongo client and fake user data
    WHEN the /register endpoint is sent valid data (POST)
    THEN check the response is valid and user added to database
    """
    response = client.post(
        "/api/auth/register",
        json=new_fake_user,
    )
    assert response.status_code == 201
    assert response.json["msg"] == "new user created"
    assert mongo.db.users.find_one({"email": new_fake_user["email"]})


def test_email_already_exists(client, email_exists):
    """
    GIVEN a Flask app and fake user data with an existing email
    WHEN the /register endpoint is sent valid data (POST) and email already exists
    THEN check the response is valid
    """
    response = client.post(
        "/api/auth/register",
        json=email_exists,
    )
    assert response.status_code == 409
    assert response.json["msg"] == "email already exists"
    assert response.json["errorField"] == "email"


def test_username_already_exists(client, username_exists):
    """
    GIVEN a Flask app and fake user data with an existing username
    WHEN the /register endpoint is sent valid data (POST) and username already exists
    THEN check the response is valid
    """
    response = client.post(
        "/api/auth/register",
        json=username_exists,
    )
    assert response.status_code == 409
    assert response.json["msg"] == "username already exists"
    assert response.json["errorField"] == "username"


def test_password_is_hashed(mongo, fake_user):
    """
    GIVEN a Mongo client and fake user data
    WHEN a user is registered
    THEN check the password is hashed when stored in database
    """
    added_user = mongo.db.users.find_one({"email": fake_user["email"]})
    assert fake_user["password"] != added_user["pwd_hash"]
