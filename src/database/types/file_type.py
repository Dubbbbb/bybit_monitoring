# from typing import Any
#
# from sqlalchemy import VARCHAR, Dialect
# from sqlalchemy.types import TypeDecorator
#
# from .file_storage import AbstractFileStorage
#
# __all__ = [
#     "FileType",
# ]
#
#
# class FileType(TypeDecorator):
#     impl = VARCHAR
#     cache_ok = True
#
#     def __init__(self, storage: AbstractFileStorage, *args: Any, **kwargs: Any):
#         super().__init__(*args, **kwargs)
#         self.storage = storage
#
#     def process_bind_param(self, value: tuple[str, bytes], dialect: Dialect) -> str:
#         return self.storage.save(*value)
#
#     def process_result_value(self, value: str, dialect: Dialect) -> str:
#         return value
