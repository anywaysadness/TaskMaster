"""

Этот файл служит для создания моделей sqlalchemy
"""
#
from core.models import Base

from sqlalchemy import Column, ForeignKey, Table, Integer, UniqueConstraint


user_task_association_table = Table(
    "user_task_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),   # Первичный ключ - идентификатор
    Column("user_id", ForeignKey("users.id"), nullable=False,),   # Внешний ключ для user
    Column("task_id", ForeignKey("tasks.id"), nullable=False),   # Внешний ключ для task
    UniqueConstraint("user_id", "task_id", name="idx_unique_user_task")
)
