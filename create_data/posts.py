
def make_post(**overrides):
    post = {
        "userId": 1,
        "title": "Заголовок поста нашего",
        "body": "Тут супер важно"
    }
    post.update(overrides)
    return post