import requests
import logging
import time

logger = logging.getLogger('core.api_client')

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
        url = self._build_url(endpoint=endpoint)
        logger.info(f"Метод: get, URL: {url}")
        start_time = time.time()
        response = self.session.get(
            url=url,
            timeout=self.timeout
        )
        end_time = time.time() - start_time
        logger.info(f"Статус ответа: {response.status_code}, время {end_time:.2f}s")
        return response

    def post(self, endpoint: str, payload):
        url = self._build_url(endpoint=endpoint)
        logger.info(f"Метод: post, URL: {url}")
        start_time = time.time()
        response = self.session.post(
            url=url,
            json=payload,
            timeout=self.timeout
        )
        end_time = time.time() - start_time
        logger.info(f"Статус ответа: {response.status_code}, время {end_time:.2f}s")
        return response

    def close(self):
        self.session.close()