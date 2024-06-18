import httpx

from typing import Optional


__all__ = [
    "AsyncHttpClient",
]


class AsyncHttpClient:
    def __init__(self, base_url):
        self.client = httpx.AsyncClient(base_url=base_url)

    async def get(self, endpoint: str, params: Optional[dict] = None, timeout: float = 3.0):
        try:
            response = await self.client.get(endpoint, params=params, timeout=timeout)
            return response.json()
        except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError):
            return None

    async def post(
            self,
            endpoint: str,
            params: Optional[dict] = None,
            data: Optional[dict] = None,
            timeout: float = 3.0
    ):
        try:
            response = await self.client.post(endpoint, params=params, json=data, timeout=timeout)
            return response.json()
        except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError):
            return None

    async def put(
            self,
            endpoint: str,
            params: Optional[dict] = None,
            data: Optional[dict] = None,
            timeout: float = 3.0
    ):
        try:
            response = await self.client.put(endpoint, params=params, json=data, timeout=timeout)
            return response.json()
        except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError):
            return None
