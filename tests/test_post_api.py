import pytest
from data.data import Data
class TestPostApi:

    def test_get_post(self, posts_service):
        response = posts_service.get_post(post_id=1)
        assert response.status_code == 200
        assert "title" in response.json()

    def test_get_incorrect_post(self, posts_service):
        response = posts_service.get_post(post_id=99999)
        assert response.status_code == 404

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post_by_id(self, post_id, posts_service):
        response = posts_service.get_post(post_id=post_id)
        assert response.status_code == 200
        assert response.json()['id'] == post_id

    def test_create_post(self, posts_service):
        response = posts_service.create_post(payload=Data.make_post())
        assert response.status_code == 201
        assert "id" in response.json()