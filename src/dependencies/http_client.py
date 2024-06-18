from typing import Annotated

from fastapi import Depends

from src.clients import AsyncHttpClient
from src.settings import settings

__all__ = [
    "HttpClientDepends"
]


HttpClient = AsyncHttpClient(base_url=settings.MARKET_DATA_PROXY_URL.unicode_string())
HttpClientDepends = Annotated[AsyncHttpClient, Depends(lambda: HttpClient)]
