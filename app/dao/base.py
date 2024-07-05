from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(
            cls,
            model_id: int,
            session: AsyncSession
    ):
        query = select(cls.model).filter_by(id=model_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(
            cls,
            session: AsyncSession,
            **filter_by
    ):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            **filter_by
    ):
        query = select(cls.model.__table__.columns).filter_by(**filter_by).order_by("id")
        result = await session.execute(query)
        return result.mappings().all()

    @classmethod
    async def add_new_record(
            cls,
            session: AsyncSession,
            **data
    ):
        query = insert(cls.model).values(**data)
        await session.execute(query)
        await session.commit()

    @classmethod
    async def update_info(
            cls,
            update_user_info,
            current_user,
            session: AsyncSession,
            partial: bool = False,  # False = put, True = patch
    ):
        for name, value in update_user_info.model_dump(exclude_unset=partial).items():
            print(name)
            setattr(current_user, name, value)
        await session.commit()
        await session.refresh(current_user)
        return current_user
