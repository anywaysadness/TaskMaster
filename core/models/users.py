"""

Этот файл служит для создания моделей sqlalchemy
"""
from typing import TYPE_CHECKING
from core.models import Base
from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
# from app.users.user_task_association import user_task_association_table

if TYPE_CHECKING:
    from core.models import Image, Task, Role


class User(Base):
    """
    Класс модели sqlalchemy Users
    """
    # Название таблицы
    __tablename__ = "users"

    # Первичный ключ - идентификатор
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    # Имя пользователя
    user_first_name: Mapped[str] = mapped_column(
        String(length=15),
        nullable=False,
        default="Максим",
        server_default="Максим"
    )
    # Фамилия пользователя
    user_second_name: Mapped[str] = mapped_column(
        String(length=20),
        nullable=False,
        default="Максимов",
        server_default="Максимов"
    )
    # Отчество пользователя
    user_middle_name: Mapped[str] = mapped_column(
        String(length=25),
        nullable=False,
        default="Максимович",
        server_default="Максимович"
    )
    # Почтовый ящик пользователя
    user_email: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
        unique=True
    )
    # Пароль пользователя
    user_pass: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False
    )
    # Должность пользователя
    user_position: Mapped[str | None] = mapped_column(
        String(length=255),
        nullable=True
    )
    # Дата создания пользователя
    user_date_creation: Mapped[str] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=func.now()
    )

    # обратная связь с images
    back_images: Mapped["Image"] = relationship(back_populates="back_users")
    # обратная связь с roles
    back_roles: Mapped["Role"] = relationship(back_populates="back_users")
    # обратная связь с tasks
    back_tasks: Mapped[list["Task"]] = relationship(back_populates="back_users")

    # Строковое представление
    def __str__(self):
        return f"Пользователь:" \
               f"{self.user_email}" \
               f"{self.user_second_name}" \
               f"{self.user_first_name}" \
               f"{self.user_middle_name}"
