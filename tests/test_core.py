def test_attempt(client):
    r = client.get("/")
    assert r.json() == {"hello": "world"}
