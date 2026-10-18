import pytest


class TestPostApi:


    def test_get_user(self, api_client):
        response = api_client.get(end_point="/posts/1")
        assert response.status_code == 200
        assert "title" in response.json()

    def test_get_incorrect_user(self, api_client):
        response = api_client.get(end_point="/posts/99999")
        assert response.status_code == 404

    @pytest.mark.parametrize("user_id", [1, 50, 100])
    def test_get_users_by_id(self, user_id, api_client):
        response = api_client.get(end_point=f"/posts/{user_id}")
        assert response.status_code == 200

