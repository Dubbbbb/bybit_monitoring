from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

__all__ = ("Base",)


class Base(DeclarativeBase):
    metadata = MetaData(schema="public", quote_schema=True)
