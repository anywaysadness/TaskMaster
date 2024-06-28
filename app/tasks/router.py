from fastapi import APIRouter
from app.database_connect import async_session_maker
from app.tasks.models import Task
from sqlalchemy import select

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.get("")
async def get_all_tasks():
    """

    :return: Все задачи
    """
    async with async_session_maker() as session:
        query = select(Task)    # SELECT * FROM tasks
        result = await session.execute(query)
        return result.scalars().all()


@router.get("/{task_id}")
async def get_task_by_id():
    """

    :return: Задача по id
    """
    pass
