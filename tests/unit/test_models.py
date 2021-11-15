from app.models import User, load_user


def test_new_user(fake_user):
    """
    GIVEN the User class and fake user data
    WHEN a new user object is created with the fake user
    THEN check each field is defined correctly
    """
    existing_user = User(email=fake_user["email"], username=fake_user["username"])

    assert existing_user.email == fake_user["email"]
    assert existing_user.username == fake_user["username"]
    assert existing_user.get_id() == fake_user["username"]
    assert existing_user.is_authenticated


def test_user_loader(fake_user):
    """
    GIVEN the user loader and fake user data
    WHEN a username is passed into the user loader
    THEN check that the return value is correct
    """
    user = load_user(fake_user["username"])
    assert isinstance(user, User)
    assert user.email == fake_user["email"]
    assert user.username == fake_user["username"]
    assert load_user("anonymous_user") is None
