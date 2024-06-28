"""

Этот файл служит для создания моделей sqlalchemy
"""

from app.database_connect import Base
from sqlalchemy import Column, ForeignKey, Table, Integer, UniqueConstraint


tag_task_association_table = Table(
    "tag_task_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),   # Первичный ключ - идентификатор
    Column("tag_id", ForeignKey("tags.id"), nullable=False),   # Внешний ключ для tag
    Column("task_id", ForeignKey("tasks.id"), nullable=False),   # Внешний ключ для task
    UniqueConstraint("tag_id", "task_id", name="idx_unique_tag_task")
)
