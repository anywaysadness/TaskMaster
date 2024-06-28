from fastapi import APIRouter
from app.database_connect import async_session_maker
from app.users.dao import UserDAO

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("")
async def get_all_users():
    """

    :return: Получить всех пользователи
    """
    return await UserDAO.find_all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    """

    :return: Получить пользователя по id
    """
    return await UserDAO.find_by_id(user_id)

