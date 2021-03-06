def test_get_posts(client):
    """
    GIVEN a Flask app
    WHEN the /posts endpoint is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/api/posts")
    assert response.status_code == 200
    assert response.json.get("data")
    assert isinstance(response.json["data"], list)
    for document in response.json["data"]:
        assert document.get("_id")
        assert isinstance(document["_id"], dict)
        assert document["_id"].get("$oid")
        assert document.get("username")
        assert isinstance(document["username"], str)
        assert document.get("haiku")
        assert isinstance(document["haiku"], str)
        assert document.get("likes")
        assert isinstance(document["likes"], int)
        assert document.get("posted_at")
        assert isinstance(document["posted_at"], dict)
        assert document["posted_at"].get("$date")
