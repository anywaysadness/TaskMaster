from fastapi import APIRouter, Depends, HTTPException, status, Path
from app.tasks import TaskDAO
from app.tasks import STask, SAddTask
from core.models import User
from app.users import get_current_user, get_current_admin_user
from core.db_helper import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.get("/", response_model=list[STask])
async def get_all_tasks(
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await TaskDAO.find_all(session=session)


@router.get("/{task_id}/", response_model=STask)
async def get_task_by_id(
        task_id: Annotated[int, Path(ge=1)],    # Параметр пути типа int >= 1
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        current_user: User = Depends(get_current_user)  # Проверка на аутентификацию пользователя
):
    task = await TaskDAO.find_by_id(task_id, session=session)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return task


@router.post("/add_task/")
async def add_task(
        user_data: SAddTask,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await TaskDAO.add_new_record(
        task_name=user_data.task_name,
        task_body=user_data.task_body,
        user_id=user_data.user_id,
        session=session
    )
    return f"{current_user.user_email} добавил задачу: {user_data.task_name} для {user_data.user_id}"
