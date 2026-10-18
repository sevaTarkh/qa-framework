class Settings:

    def __init__(self):
        self.config = {
            "dev": {"base_url": "https://dev.example.com", "timeout": 5},
            "stage": {"base_url": "https://stage.example.com", "timeout": 10},
            "demo": {"base_url": "https://jsonplaceholder.typicode.com", "timeout": 10}
        }

    def get_config(self, env: str):
        if env not in self.config:
            raise ValueError(f"Такого окружения нет, вот доступные {list(self.config)}")
        return self.config[env]

if __name__ == "__main__":
    Settings().get_config("dev123")