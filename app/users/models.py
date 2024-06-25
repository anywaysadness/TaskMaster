"""

Этот файл служит для создания моделей sqlalchemy
"""
from app.database_connect import Base
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey


class User(Base):
    """
    Класс модели sqlalchemy Users
    """

    __tablename__ = "users" # Название таблицы
    user_id = Column(Integer, primary_key=True, autoincrement=True) # Первичный ключ - идентификатор
    user_first_name = Column(String(length=15), nullable=False, default="Максим")   # Имя пользователя
    user_second_name = Column(String(length=20), nullable=False, default="Максимов")    # Фамилия пользователя
    user_middle_name = Column(String(length=25), nullable=False, default="Максимович")  # Отчество пользователя
    user_email = Column(String(length=255), nullable=False, unique=True)   # Почтовый ящик пользователя
    user_pass = Column(String(length=255), nullable=False)    # Пароль пользователя
    user_position = Column(String(length=255), nullable=True)    # Должность пользователя
    # role_id = Column()  # Роль пользователя
    # image_id = Column() # Фотография пользователя



