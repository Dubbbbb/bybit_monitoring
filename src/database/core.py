from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from src.settings import settings


async_engine = create_async_engine(settings.database_dsn.unicode_string(), echo=False)

async_session_maker = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False
)


async def get_async_session():
    async with async_session_maker() as session:  # type: AsyncSession
        yield session