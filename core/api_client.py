import requests

class APIClient:
    def __init__(self, base_url: str, timeout: int = 5):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def _build_url(self, end_point: str):
        if not end_point.startswith('/'):
            end_point = '/' + end_point
        return self.base_url + end_point

    def get(self, end_point: str):
        response = self.session.get(
            url=self._build_url(end_point=end_point),
            timeout=self.timeout
        )
        return response

    def post(self, end_point: str, payload):
        response = self.session.post(
            url=self._build_url(end_point=end_point),
            json=payload,
            timeout=self.timeout
        )
        return response

    def close(self):
        self.session.close()