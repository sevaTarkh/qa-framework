from pydantic import BaseModel, ConfigDict



class PostModel(BaseModel):
    model_config = ConfigDict(strict=True)

    userId: int
    id: int
    title: str
    body: str