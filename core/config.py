"""
Этот файл служит для задания чувствительных файлов
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from os import getenv

# Явная загрузка файла .env
load_dotenv()


class Settings(BaseSettings):
    """
    Класс настроек проекта с переменными окружения
    """
    DB_HOST: str    # IP-адрес для подключения к БД
    DB_PORT: int    # PORT для подключения к БД
    DB_USER: str    # Логин для подключения к БД
    DB_PASS: str    # Пароль для подключения к БД
    DB_NAME: str    # Имя БД
    DB_ECHO: bool = False   # Параметр echo для просмотра SQL запросов к БД
    SECRET_KEY: str  # Сгенерированный ключ для JWT
    ALGORITHM: str  # Алгоритм шифрования для JWT

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Чтение чувствительных данных из .envs
    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()

