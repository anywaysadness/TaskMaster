"""

Этот файл служит для создания моделей sqlalchemy
"""
from app.database_connect import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.tasks.tag_task_association import tag_task_association_table


class Tag(Base):
    """
    Класс модели sqlalchemy Role
    """

    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)     # Первичный ключ - идентификатор
    tag_name = Column(String(100), nullable=False, default="Пользователь")     # Название тэга

    tasks = relationship("Task", secondary=tag_task_association_table, back_populates="tags")   # Обратная связь с tasks
