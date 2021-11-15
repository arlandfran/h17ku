def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check that email, username & id are defined correctly and is authenticated
    """
    assert new_user.email == "test@test.com"
    assert new_user.username == "test_user"
    assert new_user.get_id() == "test_user"
    assert new_user.is_authenticated


def test_user_loader(user_loader, new_fake_user, fake_user, user_class):
    """
    GIVEN a user loader, fake user data and the user class
    WHEN a username is passed into the user loader
    THEN check that the return value is correct
    """
    user = user_loader(new_fake_user["username"])
    assert user is None

    user = user_loader(fake_user["username"])
    assert isinstance(user, user_class)
