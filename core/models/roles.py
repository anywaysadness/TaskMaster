"""

Этот файл служит для создания моделей sqlalchemy
"""
from core.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import User


class Role(Base):
    """
    Класс модели sqlalchemy Role
    """

    # Название таблицы
    __tablename__ = "roles"

    # Первичный ключ - идентификатор
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    # Название роли
    role_name: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
        default="Пользователь",
        server_default="Пользователь"
    )
    # Внешний ключ на user
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    # Обратная связь с users
    back_users: Mapped[list["User"]] = relationship(back_populates="back_roles")

    # Строковое представление
    def __str__(self):
        return f"Роль:" \
               f"{self.role_name}"
