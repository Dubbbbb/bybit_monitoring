from pydantic import Field, PositiveInt

from src.schemas.base import DTO


__all__ = [
    "ExampleSchema",
]


class ExampleSchema(DTO):
    id: PositiveInt = Field(
        default=...,
        title="Model ID",
    )
    name: str = Field(
        default=...,
        title="Model name",
        min_length=1
    )
    email: str = Field(
        default=...,
        title="Model email",
        min_length=1
    )
    password: str = Field(
        default=...,
        title="Model password",
        ge=0
    )
    created_at: PositiveInt = Field(
        default=...,
        title="Model created timestamp",
        ge=0
    )
