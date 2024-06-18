import jwt

from typing import Type, Optional

from starlette.requests import Request

from pydantic import BaseModel

from sqlalchemy import select
from sqlalchemy.sql.functions import count

from src.dependencies.database import DBAsyncSession
from src.database.base import Base
from src.schemas import PaginatorGenerator
from src.settings import settings

__all__ = [
    "get_next_url",
    "get_previous_url",
    "get_list_response",
    "create_access_token",
    "decode_access_token"
]


def get_next_url(
    offset: int, limit: int, count: int, request: Request
) -> Optional[str]:
    if count == 0:
        return None
    if offset + limit >= count:
        return None
    return str(request.url.include_query_params(limit=limit, offset=offset + limit))


def get_previous_url(
    offset: int, limit: int, count: int, request: Request
) -> Optional[str]:
    if count == 0:
        return None
    if offset <= 0:
        return None
    if offset - limit <= 0:
        return str(request.url.remove_query_params(keys=["offset"]))
    return str(request.url.include_query_params(limit=limit, offset=offset - limit))


async def get_list_response(
    session: DBAsyncSession,
    model: Type[Base],
    model_schema: Type[BaseModel],
    limit: int,
    offset: int,
    request: Request,
    schema_context: Optional[dict] = None
) -> PaginatorGenerator:
    obj_count = await session.scalar(select(count("*")).select_from(model))
    obj_result = await session.scalars(select(model).limit(limit).offset(offset))
    objects = obj_result.all()

    prepared_response_data = {
        "next": get_next_url(offset, limit, obj_count, request),
        "previous": get_previous_url(offset, limit, obj_count, request),
        "count": obj_count,
        "result": [
            model_schema.model_validate(
                obj=obj, from_attributes=True, context=schema_context
            )
            for obj in objects
        ],
    }
    return PaginatorGenerator[model_schema].model_validate(prepared_response_data) # noqa


def create_access_token(data: dict) -> str:
    return jwt.encode(payload=data,
               key=settings.SECRET_KEY.get_secret_value(),
               algorithm="HS256")



def decode_access_token(token: str) -> dict:
    return jwt.decode(jwt=token,
                      key=settings.SECRET_KEY.get_secret_value(),
                      algorithms=["HS256"])

