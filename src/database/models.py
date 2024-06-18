from datetime import datetime, UTC

from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, Text, TIMESTAMP, Boolean, VARCHAR, inspect

__all__ = [
    "Base",
    "ExampleModel",
]


class ExampleModel(Base):
    __tablename__ = "example_models"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    password = Column(VARCHAR(128), nullable=False)

    created_at = Column(TIMESTAMP, default=lambda: datetime.now(tz=UTC), nullable=False)
