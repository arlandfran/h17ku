from tests import test_user


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


def test_register_new_user(client, mongo):
    """
    GIVEN a Flask app and Mongo client
    WHEN the /register endpoint is sent data (POST)
    THEN check the response is valid & user added to database
    """
    response = client.post(
        "/api/auth/register",
        json=test_user["valid"],
    )
    assert response.status_code == 201
    assert response.json["msg"] == "new user created"
    assert mongo.db.users.find_one({"email": test_user["valid"]["email"]})


def test_email_already_exists(client):
    """
    GIVEN a Flask app
    WHEN the /register endpoint is sent data (POST) & email already exists
    THEN check the response is valid
    """
    response = client.post(
        "/api/auth/register",
        json=test_user["invalid_email"],
    )
    assert response.status_code == 409
    assert response.json["msg"] == "email already exists"
    assert response.json["errorField"] == "email"


def test_username_already_exists(client):
    """
    GIVEN a Flask app
    WHEN the /register endpoint is sent data (POST) & username already exists
    THEN check the response is valid
    """
    response = client.post(
        "/api/auth/register",
        json=test_user["invalid_username"],
    )
    assert response.status_code == 409
    assert response.json["msg"] == "username already exists"
    assert response.json["errorField"] == "username"


def test_password_is_hashed(mongo):
    """ "
    GIVEN a Mongo client
    WHEN a new user is registered
    THEN check the password is hashed when stored in database
    """
    added_user = mongo.db.users.find_one({"email": test_user["valid"]["email"]})
    assert test_user["valid"]["password"] != added_user["pwd_hash"]
