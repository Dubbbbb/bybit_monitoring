# from abc import ABC, abstractmethod
# from pathlib import Path
#
# __all__ = [
#     "AbstractFileStorage",
#     "FileSystemStorage",
# ]
#
#
# class AbstractFileStorage(ABC):
#
#     @abstractmethod
#     def save(self, filename: str, file: bytes) -> str:
#         ...
#
#
# class FileSystemStorage(AbstractFileStorage):
#
#     def __init__(self, upload_to: str | Path) -> None:
#         if isinstance(upload_to, str):
#             upload_to = Path(upload_to)
#
#         if not upload_to.exists():
#             upload_to.mkdir(mode=777, exist_ok=True)
#         elif not upload_to.is_dir():
#             raise ValueError
#
#         self.upload_to = upload_to
#
#     def _save(self, filename: str, file: bytes) -> None:
#         with self.upload_to.joinpath(filename).open(mode="wb") as f:
#             f.write(file)
#
#     def save(self, filename: str, file: bytes) -> str:
#         self._save(filename=filename, file=file)
#         return f"{self.upload_to.joinpath(filename)}"
