class PostsService:
    def __init__(self, client):
        self.client = client

    def get_post(self, post_id: int):
        return self.client.get(endpoint=f"posts/{post_id}")

    def create_post(self, payload):
        return self.client.post(endpoint="posts", payload=payload)