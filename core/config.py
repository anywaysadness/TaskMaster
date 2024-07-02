"""
Этот файл служит для задания чувствительных файлов
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс настроек проекта с переменными окружения
    """
    DB_HOST: str    # IP-адрес для подключения к БД
    DB_PORT: int    # PORT для подключения к БД
    DB_USER: str    # Логин для подключения к БД
    DB_PASS: str    # Пароль для подключения к БД
    DB_NAME: str    # Имя БД
    DB_ECHO: str    # Параметр echo для просмотра SQL запросов к БД

    @property
    def DATABASE_URL(self):
        """
        :return: Путь к БД
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str     # Сгенерированный ключ для JWT
    ALGORITHM: str      # Алгоритм шифрования для JWT

    # Чтение чувствительных данных из .env
    model_config = SettingsConfigDict(env_file=".env")


# Создание экземпляр класса
settings = Settings()
