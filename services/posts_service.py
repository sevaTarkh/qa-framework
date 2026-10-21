import allure


class PostsService:
    def __init__(self, client):
        self.client = client

    @allure.step('Получаю post с id: {post_id}')
    def get_post(self, post_id: int):
        return self.client.get(endpoint=f"posts/{post_id}")

    @allure.step('Создаю пост')
    def create_post(self, payload):
        return self.client.post(endpoint="posts", payload=payload)