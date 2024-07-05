"""
Этот файл служит для подключения к базе данных и создания сессий
"""
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    async_scoped_session
)
from core.config import settings
from asyncio import current_task


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        # создаем движок для подключения
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        # создаем фабрику для генерации сессий
        self.async_session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.async_session_maker,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.async_session_maker() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.DATABASE_URL,
    echo=settings.DB_ECHO
)

