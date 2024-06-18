from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import get_async_session


__all__ = [
    "DBAsyncSession",
]

DBAsyncSession = Annotated[AsyncSession, Depends(get_async_session)]
