from fastapi import APIRouter, Depends
from app.tasks import TaskDAO
from app.tasks import STask, SAddTask
from app.users.models import User
from app.users.dependencies import get_current_user, get_current_admin_user

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.get("/")
async def get_all_tasks(user: User = Depends(get_current_user)):
    """

    :return: Получить список всех задач
    """
    return await TaskDAO.find_all(id=user.id)


@router.get("/{task_id}/")
async def get_task_by_id(task_id: int) -> STask | None:
    """

    :return: Получить задачу по id
    """
    return await TaskDAO.find_by_id(task_id)


@router.post("/add_task/")
async def add_task(user_data: SAddTask, user: User = Depends(get_current_admin_user)):
    await TaskDAO.add_new_record()
