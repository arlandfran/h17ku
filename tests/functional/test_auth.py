def test_if_correct_db(mongo):
    """
    GIVEN a Mongo client
    WHEN testing authentication
    THEN check the client is connected to the test database
    """
    assert mongo.db.name == "test"


def test_user_collection_is_empty(mongo):
    """
    GIVEN a Mongo client
    WHEN testing authentication
    THEN empty user collection
    """
    mongo.db.users.delete_many({})
    users = list(mongo.db.users.find({}))
    assert len(users) == 0


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


def test_register_new_user(client, mongo, new_fake_user):
    """
    GIVEN a Flask app, Mongo client and fake user data
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


def test_password_is_hashed(mongo, new_fake_user):
    """
    GIVEN a Mongo client and fake user data
    WHEN a new user is registered
    THEN check the password is hashed when stored in database
    """
    added_user = mongo.db.users.find_one({"email": new_fake_user["email"]})
    assert new_fake_user["password"] != added_user["pwd_hash"]
