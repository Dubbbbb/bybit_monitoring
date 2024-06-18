from fastapi import FastAPI
from pydantic import BaseModel

from src.settings import Settings

__all__ = [
    "setup",
    "setup_middlewares",
]


def setup_middlewares(app: FastAPI, settings: BaseModel) -> None:
    for _, middleware_settings in settings.middlewares:  # type: str, BaseModel
        app.add_middleware(**middleware_settings.model_dump())


def setup(app: FastAPI, settings: Settings):
    setup_middlewares(app=app, settings=settings)
