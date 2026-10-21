import logging
import time

import requests

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url: str, timeout: int = 5):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def _build_url(self, endpoint: str):
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint
        return self.base_url + endpoint

    def _request(self, method, endpoint, **kwargs):
        url = self._build_url(endpoint=endpoint)
        logger.info("Метод: %s, URL: %s", method, url)
        start_time = time.perf_counter()

        response = self.session.request(method, url, timeout=self.timeout, **kwargs)

        elapsed = time.perf_counter() - start_time
        logger.info("Статус ответа: %s, время %.2f", response.status_code, elapsed)
        return response

    def get(self, endpoint: str):
        return self._request(method="GET", endpoint=endpoint)

    def post(self, endpoint: str, payload):
        return self._request(method="POST", endpoint=endpoint, json=payload)

    def close(self):
        self.session.close()