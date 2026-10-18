import pytest

class TestPostApi:

    def test_get_post(self, post_service):
        response = post_service.get_post(endpoint="/posts/1")
        assert response.status_code == 200 and "title" in response.json()

    def test_get_incorrect_post(self, post_service):
        response = post_service.get_post(endpoint="/posts/99999")
        assert response.status_code == 404

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post_by_id(self, post_id, post_service):
        response = post_service.get_post(endpoint=f"/posts/{post_id}")
        assert response.status_code == 200
        assert  response.json()['id'] == post_id

