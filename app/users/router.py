from fastapi import APIRouter
from app.users.schemas import SUser
from app.users.dao import UserDAO

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("")
async def get_all_users() -> list[SUser]:
    """

    :return: Получить список всех пользователи
    """
    return await UserDAO.find_all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> SUser | None:
    """

    :return: Получить пользователя по id
    """
    return await UserDAO.find_by_id(user_id)

