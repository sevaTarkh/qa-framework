import pytest
import allure

from factories.posts import make_post
from model.post_model import PostModel


@allure.epic("Блог API")
@allure.feature('Посты')
class TestPostApi:

    @allure.title('Получение поста')
    def test_get_post_200(self, posts_service):
        response = posts_service.get_post(post_id=1)
        assert response.status_code == 200
        PostModel.model_validate(response.json())

    @allure.title('Получение несуществующего поста')
    def test_get_missing_post_returns_404(self, posts_service):
        response = posts_service.get_post(post_id=99999)
        assert response.status_code == 404

    @allure.title('Получение поста по id={post_id}')
    @allure.story('Получение поста')
    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post_by_id_200(self, post_id, posts_service):
        response = posts_service.get_post(post_id=post_id)
        assert response.status_code == 200
        created_post = PostModel.model_validate(response.json())
        assert created_post.id == post_id

    @allure.title('Создание поста')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_post_201(self, posts_service):
        post_data = make_post()
        response = posts_service.create_post(payload=post_data)
        assert response.status_code == 201
        created = PostModel.model_validate(response.json())
        assert post_data['userId'] == created.userId
        assert post_data['title'] == created.title
        assert post_data['body'] == created.body
