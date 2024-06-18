from fastapi import FastAPI
from src.settings import settings
from src.setup import setup
from app.api import api_router
from sqladmin import Admin
from src.database.core import async_engine
from src.admin.views import ExampleAdmin
from src.admin.auth import AdminAuth

app = FastAPI(
    debug=settings.DEBUG,
)
app.include_router(api_router)
setup(app=app, settings=settings)


admin = Admin(
    app=app,
    engine=async_engine,
    title="ADMIN-NAME",
    authentication_backend=AdminAuth(
        secret_key=settings.SECRET_KEY.get_secret_value(),
    )
)
admin.add_view(ExampleAdmin)


if __name__ == '__main__':
    from uvicorn import run
    run(
        app=app,
        loop="uvloop",
        http="httptools",
        interface="asgi3",
        **settings.server.model_dump()
    )
