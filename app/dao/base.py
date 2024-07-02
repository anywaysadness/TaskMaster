from core.database_connect import async_session_maker
from sqlalchemy import select, insert


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        """
        Поиск конкретной записи в Бд по ID
        :param model_id: ID записи
        :return: Одно найденное совпадение или None
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """
        Поиск одного совпадения или его отсутствия в БД по фильтру
        :param filter_by: Переданные параметры для фильтрации
        :return: Одно найденное совпадение или None
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        """
        Поиск всех совпадений модели в БД по фильтру
        :param filter_by: Переданные параметры для фильтрации
        :return: Все найденные совпадения
        """
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_new_record(cls, **data):
        """
        Добавление новой записи в БД
        :param data: Переданные параметры
        :return: None
        """
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
