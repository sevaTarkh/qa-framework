import requests

class APIClient:
    def __init__(self, timeout: int = 5000):
        self.base_url = "https://train.com"
        self.timeout = timeout


    def build_url(self, end_point: str):
        if not end_point.startswith('/'):
            end_point = '/' + end_point
        return self.base_url.rstrip('/') + end_point


    def get(self, end_point: str):
        url = self.build_url(end_point=end_point)
        response = requests.get(url=url)
        return response

    def post(self, payload, end_point: str):
        url = self.build_url(end_point=end_point)
        response = requests.post(url=url, json=payload)
        return response