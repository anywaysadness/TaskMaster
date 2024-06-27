"""

Этот файл служит для создания моделей sqlalchemy
"""
from app.database_connect import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


class Task(Base):
    """
    Класс модели sqlalchemy Task
    """

    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, autoincrement=True)     # Первичный ключ - идентификатор
    task_date_create = Column(DateTime, nullable=False, default=func.now())
    task_name = Column(String(length=255), nullable=False, default="Задача")    # Имя задачи
    task_body = Column(Text)    # Описание задачи
    status = Column(String(length=50), nullable=False, default="Не выполнена")  # Статус задачи

    user = relationship("User", secondary="user_task_association", back_populates="tasks")  # обратная связь с user
    tag = relationship("Tag", secondary="tag_task_association", back_populates="tasks")     # обратная связь с tag


class UserTaskAssociation(Base):
    """
    Класс модели sqlalchemy для связи Task и User
    """
    __tablename__ = "user_task_association"
    user_task_id = Column(Integer, primary_key=True)    # Первичный ключ - идентификатор
    user_id = Column(Integer, ForeignKey("users.user_id"))  # Внешний ключ для user
    task_id = Column(Integer, ForeignKey("tasks.task_id"))  # Внешний ключ для task
