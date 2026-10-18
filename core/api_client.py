import requests

class APIClient:
    def __init__(self, base_url: str, timeout: int = 5):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def _build_url(self, endpoint: str):
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint
        return self.base_url + endpoint

    def get(self, endpoint: str):
        response = self.session.get(
            url=self._build_url(endpoint=endpoint),
            timeout=self.timeout
        )
        return response

    def post(self, endpoint: str, payload):
        response = self.session.post(
            url=self._build_url(endpoint=endpoint),
            json=payload,
            timeout=self.timeout
        )
        return response

    def close(self):
        self.session.close()