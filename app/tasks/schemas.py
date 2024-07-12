from pydantic import BaseModel, ConfigDict
from datetime import datetime


class STaskBase(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STask(STaskBase):
    """
    Схема pydantic для Task
    """
    task_date_create: datetime
    task_name: str
    task_body: str
    task_status: str


class SAddTask(BaseModel):
    """
    Схема pydantic для создания Task
    """
    task_name: str = "Задача"
    task_body: str = "Описание задачи"
    user_id: int

    model_config = ConfigDict(from_attributes=True)
