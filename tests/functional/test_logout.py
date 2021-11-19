def test_invalid_logout(client):
    """
    GIVEN a Flask app
    WHEN the /logout endpoint is requested with no user in session (GET)
    THEN check response is valid
    """
    response = client.get("/api/auth/logout")
    assert response.status_code == 401
    assert (
        b"The server could not verify that you are authorized to access the URL requested."
        in response.data
    )


def test_logout(client, mongo, fake_user):
    """
    GIVEN a Flask app, a Mongo client and fake user data
    WHEN user logged in
    THEN log the user out and check the response is valid
    """
    assert mongo.db.users.find({"email": fake_user["email"]})

    response = client.post(
        "/api/auth/login",
        json={"email": fake_user["email"], "password": fake_user["password"]},
    )
    assert response.status_code == 200
    assert response.json["login"] is True

    response = client.get("/api/auth/logout")
    assert response.status_code == 200
    assert response.json["logout"] is True
