from core.models import Task
from app.dao.base import BaseDAO
from sqlalchemy.ext.asyncio import AsyncSession


class TaskDAO(BaseDAO):
    model = Task

    @classmethod
    async def create_task_for_user(
            cls,
            user_id: int,
            task_name,
            session: AsyncSession
    ):
        # task = Task(task_name=task_name, task_body=task_body, user_id=user_id)
        pass

