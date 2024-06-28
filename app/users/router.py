from fastapi import APIRouter
from app.database_connect import async_session_maker
from app.users.models import User
from sqlalchemy import select

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("")
async def get_all_users():
    """

    :return: Все пользователи
    """
    async with async_session_maker() as session:
        query = select(User).order_by("user_id")   # SELECT * FROM users
        result = await session.execute(query)
        return result.scalars().all()


@router.get("/{user_id}")
async def get_user_by_id():
    """

    :return: Пользователь по id
    """
    pass

