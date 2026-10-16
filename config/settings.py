from configparser import ConfigParser


class Settings:

    def __init__(self):
        self.config = {
            "dev": {"base_url": "https://dev.example.com", "timeout": 5},
            "stage": {"base_url": "https://stage.example.com", "timeout": 10}
        }


    def get_config(self, env: str):
        try:
            return self.config[env]
        except:
            raise ValueError(f"Такого окружения нет, вот доступные {self.config.keys()}")