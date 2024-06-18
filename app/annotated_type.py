from typing import Annotated

from fastapi import Query, Path

__all__ = [
    "LimitQueryInt",
    "OffsetQueryInt",
]


LimitQueryInt = Annotated[int, Query(ge=1, alias="limit")]
OffsetQueryInt = Annotated[int, Query(ge=1, alias="offset")]
