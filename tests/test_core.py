def test_attempt(client):
    r = client.get("/")
    assert r.json() == {"hello": "world!"}
    # r = client.get("/flurb")
    # assert r.json() == {"hello": "world"}
