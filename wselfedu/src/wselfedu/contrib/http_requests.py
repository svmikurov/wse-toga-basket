"""Requests module."""

from urllib.parse import urljoin

import httpx

DEV_HOST_API = 'http://127.0.0.1/'
DEV_USERNAME = 'user1'
DEV_PASSWORD = '1q2s3d4r'

HOST_API = DEV_HOST_API
USERNAME = DEV_USERNAME
PASSWORD = DEV_PASSWORD
GET_TOKEN_PATH = 'auth/token/login/'

auth = httpx.BasicAuth(USERNAME, PASSWORD)


def send_get_request(path: str, url: str | None = None) -> list[dict]:
    """Send a GET request."""
    request_url = url or urljoin(HOST_API, path)
    with httpx.Client(auth=auth) as client:
        response = client.get(url=request_url)
    return response.json()
