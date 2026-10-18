class PostsService:
    def __init__(self, client):
        self.client = client

    def get_post(self, endpoint):
        return self.client.get(endpoint=endpoint)