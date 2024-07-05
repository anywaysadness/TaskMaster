"""
Этот файл служит для создания моделей sqlalchemy
"""
from typing import TYPE_CHECKING
from core.models import Base
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
if TYPE_CHECKING:
    from core.models import User


class Image(Base):
    """
    Класс модели sqlalchemy Image
    """
    # Название таблицы
    __tablename__ = "images"

    # Первичный ключ - идентификатор
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    # Путь к картинке
    image_path: Mapped[str] = mapped_column(
        String(length=200),
    )
    # Дата создания картинки
    image_date_create: Mapped[str] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=func.now()
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # Обратная связь с users
    back_users: Mapped["User"] = relationship(back_populates="back_images")

    # Строковое представление
    def __str__(self):
        return f"Картинка:" \
               f"{self.image_path}"\
               f"{self.image_date_create}"
