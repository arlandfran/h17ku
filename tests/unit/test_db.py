def test_if_correct_db(mongo):
    """
    GIVEN a Mongo client
    WHEN testing
    THEN check the client is connected to the test database
    """
    assert mongo.db.name == "test"


def test_user_collection_is_empty(mongo):
    """
    GIVEN a Mongo client
    WHEN testing registration
    THEN that check the user collection is empty for testing
    """
    users = list(mongo.db.users.find({}))
    assert len(users) == 0


def test_fake_user_exists(mongo, fake_user):
    """
    GIVEN a Mongo client and fake user data
    WHEN testing login
    THEN check if fake user exists in test database
    """
    assert mongo.db.users.find({"email": fake_user["email"]})
