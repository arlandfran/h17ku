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
