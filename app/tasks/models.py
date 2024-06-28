"""

Этот файл служит для создания моделей sqlalchemy
"""
from app.database_connect import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.users.user_task_association import user_task_association_table
from app.tasks.tag_task_association import tag_task_association_table


class Task(Base):
    """
    Класс модели sqlalchemy Task
    """
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)     # Первичный ключ - идентификатор
    task_date_create = Column(DateTime, nullable=False, server_default=func.now())
    task_name = Column(String(length=255), nullable=False, default="Задача")    # Имя задачи
    task_body = Column(Text)    # Описание задачи
    status = Column(String(length=50), nullable=False, default="Не выполнена")  # Статус задачи

    users = relationship("User", secondary=user_task_association_table, back_populates="tasks")  # обратная связь с user
    tags = relationship("Tag", secondary=tag_task_association_table, back_populates="tasks")     # обратная связь с tag

