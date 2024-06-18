import bcrypt

from http import HTTPMethod
from pathlib import Path
from re import Pattern
from typing import List, Literal, Union, Optional, Type

from pydantic import PositiveInt, BaseModel, ConfigDict, Field, PostgresDsn, HttpUrl, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from yaml import safe_load


class SettingsDTO(BaseModel):
    model_config = ConfigDict(frozen=True)


class ServerSettings(SettingsDTO):
    host: str = "0.0.0.0"
    port: PositiveInt = 80
    workers: PositiveInt = 1


class CORSMiddlewareSettings(SettingsDTO):
    middleware_class: Type = CORSMiddleware
    allow_origins: List[str] = ["*"]
    allow_methods: List[Union[HTTPMethod, Literal["*"]]] = ["*"]
    allow_headers: List[str] = ["*"]
    allow_credentials: bool = False
    allow_origin_regex: Optional[Pattern[str]] = None
    expose_headers: List[str] = []
    max_age: PositiveInt = 600


class GZipMiddlewareSettings(SettingsDTO):
    middleware_class: Type = GZipMiddleware
    minimum_size: PositiveInt
    compresslevel: PositiveInt = Field(le=9)


class TrustedHostMiddlewareSettings(SettingsDTO):
    middleware_class: Type = TrustedHostMiddleware
    allowed_hosts: List[str] = ["*"]
    www_redirect: bool = True


class ProxyHeadersMiddlewareSettings(BaseSettings):
    middleware_class: Type = ProxyHeadersMiddleware
    trusted_hosts: List[str] = ["*"]


class MiddlewaresSettings(SettingsDTO):
    cors: CORSMiddlewareSettings
    gzip: GZipMiddlewareSettings
    trusted_host: TrustedHostMiddlewareSettings
    proxy_headers: ProxyHeadersMiddlewareSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(frozen=True)

    # general
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DEBUG: bool = True

    # db
    database_dsn: PostgresDsn

    # admin panel creds
    ADMIN_USERNAME: SecretStr
    ADMIN_PASSWORD: SecretStr

    # secret
    SECRET_KEY: SecretStr

    # server settings
    server: ServerSettings

    # middlewares settings
    middlewares: MiddlewaresSettings


    @field_validator("ADMIN_PASSWORD")
    @classmethod
    def hash_password(cls, password: SecretStr) -> bytes:
        password = password.get_secret_value().encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt)

    @classmethod
    def from_yaml(cls, file: str = "config.yaml") -> "Settings":
        with open(file=file, mode="rt", encoding="utf-8") as file:
            yaml_data = safe_load(file)
        return yaml_data

    def __init__(self, **kwargs):
        yaml_data = self.from_yaml()
        data = {**yaml_data, **kwargs}
        super().__init__(**data)


settings = Settings()

