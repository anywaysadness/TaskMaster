"""

Этот файл служит для создания моделей sqlalchemy
"""
from core.models import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .user_task_association import user_task_association_table
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.models import User, Tag


class Task(Base):
    """
    Класс модели sqlalchemy Task
    """

    # Название таблицы
    __tablename__ = "tasks"

    # Первичный ключ - идентификатор
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    # Дата создания задачи
    task_date_create: Mapped[str] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=func.now()
    )
    # Имя задачи
    task_name: Mapped[str] = mapped_column(
        nullable=False,
        default="Задача",
        server_default="Задача"
    )
    # Описание задачи
    task_body: Mapped[str] = mapped_column(Text)
    # Статус задачи
    task_status: Mapped[str] = mapped_column(
        String(length=50),
        nullable=False,
        default="Не выполнена",
        server_default="Не выполнена"
    )

    # Обратная связь с users
    back_users: Mapped[list["User"]] = relationship(
        secondary=user_task_association_table,
        back_populates="back_tasks"
    )
    # обратная связь с tag
    # back_tags: Mapped[list["Tag"]] = relationship(back_populates="back_tasks")

    # Строковое представление
    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, " \
               f"task_name={self.task_name}, " \
               f"task_status={self.task_status} "
