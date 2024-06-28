from fastapi import APIRouter
from app.tasks.dao import TaskDAO
from app.tasks.shemas import STask


router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.get("")
async def get_all_tasks() -> list[STask]:
    """

    :return: Получить список всех задач
    """
    return await TaskDAO.find_all()


@router.get("/{task_id}")
async def get_task_by_id(task_id: int) -> STask | None:
    """

    :return: Получить задачу по id
    """
    return await TaskDAO.find_by_id(task_id)
