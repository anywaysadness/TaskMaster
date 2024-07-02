"""

Этот файл служит для создания моделей sqlalchemy
"""
from core.models import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Role(Base):
    """
    Класс модели sqlalchemy Role
    """

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)     # Первичный ключ - идентификатор
    role_name = Column(String(100), nullable=False, default="Пользователь")     # Название роли

    users = relationship("User", back_populates="roles")

