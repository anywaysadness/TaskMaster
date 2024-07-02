from fastapi import APIRouter, HTTPException, status, Response, Depends, Path

from app.users import UserDAO
from app.users import SUser, SUserRegister, SUserAuth
from app.users import get_password_hash, create_access_token, authenticate_user
from app.users import get_current_user, get_current_admin_user
from app.users import User
from typing import Annotated

router = APIRouter(
    prefix="/users",
    tags=["Auth & Пользователи"],
)


@router.get("/")
async def get_all_users(current_user: User = Depends(get_current_admin_user)) -> list[SUser]:
    """
    Получить список всех пользователей. Доступно только admin
    :return: Список всех пользователи
    """
    return await UserDAO.find_all()


@router.get("/{user_id}/")
async def get_user_by_id(
        user_id: Annotated[int, Path(ge=1)],    # Параметр пути типа int >= 1
        current_user: User = Depends(get_current_user)  # Проверка на аутентификацию пользователя
) -> SUser | None:
    """
    Получение User по id
    :param user_id:
    :param current_user:
    :return: Пользователь
    """
    user = await UserDAO.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.get("/me/")
async def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Текущий юзер
    :param current_user:
    :return:
    """
    return current_user


@router.post("/login/")
async def login_user(response: Response, user_data: SUserAuth):
    """
    Аутентификация User
    :param response:
    :param user_data:
    :return:
    """
    user = await authenticate_user(user_data.user_email, user_data.user_pass)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("auth_access_token", access_token)
    return {"auth_access_token": access_token}


@router.post("/logout/")
async def logout_user(response: Response):
    """
    Выход User - удаление куки
    :param response:
    :return:
    """
    response.delete_cookie("auth_access_token")


@router.post("/register/")
async def add_user(user_data: SUserRegister):
    """
    Регистрация нового User
    :param user_data: Словарь переданных пользователем значений
    :return: Статус код регистрации пользователя
    """
    existing_user: SUser = await UserDAO.find_one_or_none(user_email=user_data.user_email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.user_pass)
    await UserDAO.add_new_record(
        user_first_name=user_data.user_first_name,
        user_second_name=user_data.user_second_name,
        user_middle_name=user_data.user_middle_name,
        user_email=user_data.user_email,
        user_pass=hashed_password,
    )
