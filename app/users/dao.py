from core.models import User
from app.dao.base import BaseDAO
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def change_password_current_user(
            cls,
            current_user: User,
            user_pass: str,
            session: AsyncSession

    ):
        current_user.user_pass = user_pass
        await session.commit()
        await session.refresh(current_user)
        return current_user

    @classmethod
    async def get_roles_with_user(
            cls,
            model_id: int,
            session: AsyncSession
    ):
        query = select(User).options(selectinload(User.back_roles)).filter_by(id=model_id)
        result = await session.execute(query)
        roles_with_user = result.scalars().all()
        return roles_with_user

    @classmethod
    async def get_all_roles_with_all_users(
            cls,
            session: AsyncSession
    ):
        query = select(User).options(selectinload(User.back_roles)).order_by(User.id)
        result = await session.execute(query)
        all_roles_with_all_users = result.scalars().all()
        return all_roles_with_all_users

    @classmethod
    async def get_tasks_with_user(
            cls,
            model_id: int,
            session: AsyncSession
    ):
        query = select(User).options(selectinload(User.back_tasks)).filter_by(id=model_id)
        result = await session.execute(query)
        tasks_with_user = result.scalars().all()
        return tasks_with_user

    @classmethod
    async def get_all_tasks_with_all_users(
            cls,
            session: AsyncSession
    ):
        query = select(User).options(selectinload(User.back_tasks)).order_by(User.id)
        result = await session.execute(query)
        all_tasks_with_all_users = result.scalars().all()
        return all_tasks_with_all_users
