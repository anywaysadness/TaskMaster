"""
Этот файл служит для подключения к базе данных и создания сессий
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

# создаем движок для подключения
engine = create_async_engine(settings.DATABASE_URL)

# создаем фабрику для генерации сессий
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    """
    Базовый класс для создания наследования под все модели.
    """
    pass
