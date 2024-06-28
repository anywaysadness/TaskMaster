"""

Этот файл служит для создания моделей sqlalchemy
"""
from app.database_connect import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


class Role(Base):
    """
    Класс модели sqlalchemy Role
    """

    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True, autoincrement=True)     # Первичный ключ - идентификатор
    role_name = Column(String(100), nullable=False, default="Пользователь")     # Название роли

    users = relationship("User", back_populates="roles")

