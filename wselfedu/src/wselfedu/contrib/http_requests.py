"""Requests module."""

from urllib.parse import urljoin

import httpx
from httpx import Request

DEV_HOST_API = 'http://127.0.0.1/'
DEV_USERNAME = 'user1'
DEV_PASSWORD = '1q2s3d4r'

HOST_API = DEV_HOST_API
USERNAME = DEV_USERNAME
PASSWORD = DEV_PASSWORD
GET_TOKEN_PATH = 'auth/token/login/'


class CustomAuth(httpx.Auth):
    """Custom authentication class with httpx library."""

    _access_token = None

    def __init__(self, username: str, password: str) -> None:
        """Construct auth."""
        self.auth_data = {
            'username': username,
            'password': password,
        }

    def auth_flow(self, request: Request) -> Request:
        """Add headers to request."""
        request.headers['Authorization'] = f'Token {self.access_token}'
        yield request

    @property
    def access_token(self) -> str:
        """Access token."""
        if not self._access_token:
            self.get_access_token()
        return self._access_token

    def get_access_token(self) -> None:
        """Get access token."""
        with httpx.Client() as client:
            response = client.post(
                url=urljoin(HOST_API, GET_TOKEN_PATH),
                json=self.auth_data,
            )
        self._access_token = response.json()['auth_token']


auth = CustomAuth(USERNAME, PASSWORD)


def send_get_request(path: str, url: str | None = None) -> list[dict]:
    """Send a GET request."""
    request_url = url or urljoin(HOST_API, path)
    with httpx.Client(auth=auth) as client:
        response = client.get(url=request_url)
    return response.json()
