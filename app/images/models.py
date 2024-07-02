"""

Этот файл служит для создания моделей sqlalchemy
"""
from core.models import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Image(Base):
    """
    Класс модели sqlalchemy Image
    """
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, autoincrement=True)  # Первичный ключ - идентификатор
    image_path = Column(String())  # Путь к картинке
    image_date_create = Column(DateTime, nullable=False, default=func.now())    # Дата создания картинки
