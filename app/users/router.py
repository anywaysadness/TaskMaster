from fastapi import APIRouter, HTTPException, status, Response, Depends, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.users import UserDAO
from app.users import SUser, SUserAuth, SUserRegister, SUserResponse, SUserUpdate, SUserUpdatePartial
from core.models import User
from app.users import get_current_user, get_current_admin_user, get_password_hash
from app.users import authenticate_user, create_access_token
from typing import Annotated
from core.db_helper import db_helper


router = APIRouter(
    prefix="/users",
    tags=["Auth & Пользователи"],
)


@router.get("/", response_model=list[SUserResponse])
async def get_all_users(
        current_user: User = Depends(get_current_user),    # Проверка на аутентификацию пользователя
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await UserDAO.find_all(session=session)


@router.get("/me/", response_model=SUserResponse)
async def read_current_user(
        current_user: User = Depends(get_current_user)  # Проверка на аутентификацию пользователя
):
    return current_user


@router.get("/role_with_current_user/")
async def show_roles_with_current_user(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user),  # Проверка на аутентификацию пользователя
):
    roles_with_current_user = await UserDAO.get_roles_with_user(
        model_id=current_user.id,
        session=session
    )
    return roles_with_current_user


@router.get("/all_roles_with_all_users/")
async def show_all_roles_with_all_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user),
):
    all_roles_with_all_users = await UserDAO.get_all_roles_with_all_users(
        session=session
    )
    return all_roles_with_all_users


@router.get("/tasks_with_current_user/")
async def show_tasks_with_current_user(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user),  # Проверка на аутентификацию пользователя
):
    tasks = await UserDAO.get_tasks_with_user(
        model_id=current_user.id,
        session=session
    )
    return tasks


@router.get("/all_tasks_with_all_users/")
async def show_all_tasks_with_all_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user),
):
    all_tasks_with_all_users = await UserDAO.get_all_tasks_with_all_users(
        session=session
    )
    return all_tasks_with_all_users


@router.get("/{user_id}/", response_model=SUserResponse)
async def get_user_by_id(
        user_id: Annotated[int, Path(ge=1)],    # Параметр пути типа int >= 1
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user)  # Проверка на аутентификацию пользователя
):
    user = await UserDAO.find_by_id(user_id, session=session)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.put("/change_info/", response_model=SUserResponse)
async def update_info_user(
        update_user_info: SUserUpdate,   # Полученные данные для обновления
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user),  # Проверка на аутентификацию пользователя
):
    update_user = await UserDAO.update_info(
        update_user_info=update_user_info,
        current_user=current_user,
        partial=False,
        session=session
    )
    return update_user


@router.patch("/change_info/", response_model=SUserResponse)
async def update_info_user(
        update_user_info: SUserUpdatePartial,   # Полученные данные для обновления
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user),  # Проверка на аутентификацию пользователя
):
    update_user = await UserDAO.update_info(
        update_user_info=update_user_info,
        current_user=current_user,
        partial=True,
        session=session
    )
    return update_user


@router.patch("/change_password/")
async def change_password(
        new_password: int | str,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user),  # Проверка на аутентификацию пользователя
):
    hashed_password = get_password_hash(str(new_password))
    await UserDAO.change_password_current_user(
        user_pass=hashed_password,
        current_user=current_user,
        session=session,
    )
    return f"password changed"


@router.post("/login/")
async def login_user(
        response: Response,
        user_data: SUserAuth,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await authenticate_user(user_data.user_email, user_data.user_pass, session=session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("auth_access_token", access_token)
    return {"auth_access_token": access_token}


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie("auth_access_token")


@router.post("/register/")
async def add_user(
        user_data: SUserRegister,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    existing_user: User | None = await UserDAO.find_one_or_none(user_email=user_data.user_email, session=session)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.user_pass)
    await UserDAO.add_new_record(
        session=session,
        user_first_name=user_data.user_first_name,
        user_second_name=user_data.user_second_name,
        user_middle_name=user_data.user_middle_name,
        user_email=user_data.user_email,
        user_pass=hashed_password
    )






