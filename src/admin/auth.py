import bcrypt

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.settings import settings
from src.utils import create_access_token, decode_access_token

__all__ = [
    "AdminAuth",
]


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        if (
                username == settings.ADMIN_USERNAME.get_secret_value()
                and
                bcrypt.checkpw(password.encode('utf-8'), settings.ADMIN_PASSWORD)
        ):
            token = create_access_token({
                "username": username,
            })
            request.session.update({"token": token})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        decode_token = decode_access_token(token)
        username = decode_token.get('username')
        if (
                username != settings.ADMIN_USERNAME.get_secret_value()
                # or
                # not bcrypt.checkpw(password.encode('utf-8'), settings.ADMIN_PASSWORD)
        ):
            return False
        return True
