from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from server.core.settings import settings

engine = create_async_engine(settings.database_url, future=True, echo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Сгенерировать асинхронную сессию."""
    async with async_session() as session:
        yield session
