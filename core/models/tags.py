"""

Этот файл служит для создания моделей sqlalchemy
"""
from core.models import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
# from app.tasks.tag_task_association import tag_task_association_table
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import Task


class Tag(Base):
    """
    Класс модели sqlalchemy Role
    """

    # Название таблицы
    __tablename__ = "tags"

    # Первичный ключ - идентификатор
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    # Название тега
    tag_name: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
        default="Пользователь",
        server_default="Пользователь"
    )

    # Обратная связь с tasks
    # back_tasks: Mapped[list["Task"]] = relationship(back_populates="back_tags")

    # Строковое представление
    def __str__(self):
        return f"Тег:" \
               f"{self.tag_name}"
