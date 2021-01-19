
def test_app_online(client):
    response = client.get("/")
    assert response.location == "http://localhost/todo/"
    