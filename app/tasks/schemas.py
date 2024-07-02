from pydantic import BaseModel, ConfigDict
from datetime import datetime


class STask(BaseModel):
    """
    Схема pydantic для Task
    """
    id: int
    task_date_create: datetime
    task_name: str
    task_body: str
    status: str

    model_config = ConfigDict(from_attributes=True)


class SAddTask(BaseModel):
    """
    Схема pydantic для создания Task
    """
    task_name: str
    task_body: str

    model_config = ConfigDict(from_attributes=True)