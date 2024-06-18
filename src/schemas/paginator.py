from typing import Optional, Type

from pydantic import Field, HttpUrl, create_model

from src.schemas.base import DTO

__all__ = [
    "PaginatorGenerator"
]


class PaginatorGenerator:

    def __class_getitem__(cls, schema: Type[DTO]):
        return create_model(
            f"{schema.__name__}Paginator",
            next=(Optional[HttpUrl], Field(default=None, title="Next Page Url")),
            previous=(Optional[HttpUrl], Field(default=None, title="Previous Page Url")),
            count=(int, Field(default=..., ge=0)),
            result=(list[schema], Field(default=...))
        )