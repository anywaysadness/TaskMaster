"""

Этот файл служит для создания моделей sqlalchemy
"""
from app.database_connect import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


class Tag(Base):
    """
    Класс модели sqlalchemy Role
    """

    __tablename__ = "tags"
    tag_id = Column(Integer, primary_key=True, autoincrement=True)     # Первичный ключ - идентификатор
    tag_name = Column(String(100), nullable=False, default="Пользователь")     # Название тэга

    task = relationship("Task", secondary="tag_task_association", back_populates="tags")


class TagsTaskAssociation(Base):
    """
    Класс модели sqlalchemy для связи Task и Tags
    """
    __tablename__ = "tag_task_association"
    tag_task_id = Column(Integer, primary_key=True)    # Первичный ключ - идентификатор
    tag_id = Column(Integer, ForeignKey("tags.tag_id"))  # Внешний ключ для tag
    task_id = Column(Integer, ForeignKey("tasks.task_id"))  # Внешний ключ для task

