from api.api_client import ApiClient

def test_get_users():

    api = ApiClient()
    response = api.get("/users")

    assert response.status_code == 200
    assert len(response.json()) > 0