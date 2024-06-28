"""

Этот файл служит для создания моделей sqlalchemy
"""
from app.database_connect import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.users.user_task_association import user_task_association_table


class User(Base):
    """
    Класс модели sqlalchemy Users
    """

    __tablename__ = "users"     # Название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)     # Первичный ключ - идентификатор
    user_first_name = Column(String(length=15), nullable=False, default="Максим")   # Имя пользователя
    user_second_name = Column(String(length=20), nullable=False, default="Максимов")    # Фамилия пользователя
    user_middle_name = Column(String(length=25), nullable=False, default="Максимович")  # Отчество пользователя
    user_email = Column(String(length=255), nullable=False, unique=True)   # Почтовый ящик пользователя
    user_pass = Column(String(length=255), nullable=False)    # Пароль пользователя
    user_position = Column(String(length=255), nullable=True)    # Должность пользователя
    user_date_creation = Column(DateTime, nullable=False, default=func.now())
    role_id = Column(ForeignKey("roles.id"), default=2)  # Роль пользователя
    image_id = Column(ForeignKey("images.id"), nullable=True)    # Фотография пользователя

    tasks = relationship("Task", secondary=user_task_association_table, back_populates="users")     # обратная связь с tasks
    roles = relationship("Role", back_populates="users")   # обратная связь с roles


